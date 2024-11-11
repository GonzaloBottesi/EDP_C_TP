import csv
import datetime
from TP_EDP import Telefono


class Central():
    
    def __init__(self):
        
        self.telefonos=self.extraer_archivo('telefonos.csv')
        self.registro_llamadas=dict()
        self.registro_sms = dict()
        
    #Verificar si van todos los atributos del l
    
    def extraer_archivo(self, archivo_csv):
        telefonos=dict()
        try:
            with open(archivo_csv, mode='r', newline='', encoding = 'utf-8') as archivo:
                lector_csv = csv.reader(archivo)
                next(lector_csv)
                for telefono in lector_csv:
                    telefonos[telefono[0]]=Telefono(telefono[0],telefono[1],telefono[2],telefono[3],
                                                    telefono[4],telefono[5],telefono[6],telefono[7])      
            print("Todos los teléfonos han sido registrados desde el archivo CSV.")
            return telefonos
        except FileNotFoundError:
            print("El archivo CSV no fue encontrado.")
        except KeyError as e:
            print(f"Error en el archivo CSV. Faltan columnas: {e}")
        except Exception as e:
            print(f"Se produjo un error al leer el archivo CSV: {e}")

    def eliminar_dispositivo(self,telefono:Telefono):
        if telefono.id in self.telefonos:
            self.telefonos.pop(telefono.id)
            print (f"Se elimino el telefono con el id {telefono.id}")
        else:
            print (f"No se encuentra registrado el telefono con el id {telefono.id}")
        
    def registrar_telefono(self, telefono:Telefono):
        if telefono.id not in self.telefonos: 
            self.telefonos.update({telefono.id : telefono})
            print (f"Se registro el telefono con el id {telefono.id}")
        else:
            print (f"Ya se encuentra registrado el telefono con el id {telefono.id}")
    
    
    def verificar_disponibilidad_de_red(self, numero):
        
        if numero not in self.telefonos:
            print(f"El telefono con numero {numero} no esta registrado.")
            return False

        dispositivo = self.telefonos[numero]
        
        if dispositivo.encendido and dispositivo.configParameters.red:
            print(f"El telefono con numero {numero} esta disponible.")
            return True
        else:
            print(f"El telefono con numero {numero} no esta disponible.")
            return False
        
    
    def verificar_acceso_internet(self, numero):
        
        if numero not in self.telefonos:
            print(f"El telefono con numero {numero} no tiene acceso a internet.")
            return False
        
        dispositivo = self.telefonos[numero]
        if dispositivo.encendido and dispositivo.datos:
            print(f"El telefono con numero {numero} tiene acceso a internet.")
            return True
        else:
            print(f"El telefono con numero {numero} no tiene acceso a internet.")
            return False
    
    def receivePakcet(self, packet : list):
        types = ['SMS', 'LLAMADA']
        
        if packet[0] not in types:
            print ('CENTRAL: Error al procesar paquete, tipo erroneo')
            return False
        
        if packet[0] == 'LLAMADA':
            newPacket = self.manejarLlamada(packet)
            return newPacket
        else:
            pass ##Manejar SMS
    
    def manejarSMS (self, packet : list):
        receptor = packet[2]
        if not receptor in self.telefonos:
            packet[4] = None ##Distinto de un caracter vacio '' asi que nunca puede entrar por error
            return packet
    
## Modelo de paquete a enviar: ['LLAMADA', Emisor , Receptor, datetime , pedido]. R = REQUEST ; B = BUSY ; N = NOT FOUND ; K = OK ; S = STOP ; F = RECHAZADO
    
    def manejarLlamada(self, packet : list):
        """Inicia la llamada verificando la disponibilidad de ambos teléfonos."""
        
        numero_origen = packet[1]
        numero_destino = packet[2]
        
        if not (numero_origen in self.telefonos and numero_destino in self.telefonos):
            print(f"El teléfono con número {numero_destino} no está registrado en la central.")
            packet[4] = 'N'
            return packet
        
        #Ambos estan registrados en la central
        telefono_origen = self.telefonos[numero_origen]
        telefono_destino = self.telefonos[numero_destino]
        
        if packet[4] == 'R':
            # Verificar si ambos teléfonos están disponibles para la llamada
            if not (self.verificar_disponibilidad_de_red(numero_origen) and self.verificar_disponibilidad_de_red(numero_destino)):
                print("Uno o ambos teléfonos no están disponibles para la llamada.")
                return False

            if telefono_destino.ocupado:
                print(f"No se puede realizar la llamada. El número {numero_destino} está ocupado.")
                packet[4] = 'B'
                return packet
            else:
                #['LLAMADA', Emisor , Receptor, datetime , 'R']
                return packet
        elif packet[4] == 'K':
            return packet
        elif packet[4] == 'F':
            #['LLAMADA', Emisor , Receptor, datetime , 'F']
            header = packet[1] + ' - ' + packet[2] +' , ' + packet[3]
            self.registro_llamadas.update({header : 'Rechazada'})    
            return packet
        elif packet[4] == 'S':
            header = packet[1] + ' - ' + packet[2] +' , ' + packet[3]
            time1 = datetime.datetime.strptime(packet[3],"%d/%m/%Y, %H:%M:%S") ##Inicio de comunicacion
            time2 = datetime.datetime.now().replace(microsecond = 0) #Fin de comunicacion
            delta = time2 - time1
            self.registro_llamadas.update({header : 'Duracion: ' + str(delta)})
            return packet

'''       PRUEBA DE LLAMADA, RECEPCION Y CORTE   
test = Central()

santi = Telefono(2,'Santi', 'S22', 'Android', '3.0.0', '16 G', '256 G', '1122857835')
gonza = Telefono(3,'Gonza', 'S22', 'Android', '3.0.0', '16 G', '256 G', '1159369841')

##El numero como clave porque no se va a repetir / no se deberia repetir para la central
test.telefonos.update({santi.id : santi,
                       gonza.id : gonza})


gonza.encendido = True
santi.encendido = True

gonza.bloqueado = False
santi.bloqueado = False

gonza.configParameters.red = True
gonza.configParameters.datos = True

santi.configParameters.red = True
santi.configParameters.datos = True

gonza.openApp()
santi.openApp()


##ENVIAR LLAMADA
paquete = gonza.aplicacionActual.sendCallRequest(gonza.numero) 
paquete2 = test.receivePakcet(paquete)

##RESPONDER LLAMADA
paquete3 = santi.aplicacionActual.receivePacket(paquete2)
paquete4 = test.receivePakcet(paquete3)
paquete5 = gonza.aplicacionActual.receivePacket(paquete4)

##CORTAR LLAMADA
respuesta = santi.aplicacionActual.endCallRequest(santi.numero)
respuesta2 = test.receivePakcet(respuesta)
respuesta3 = gonza.aplicacionActual.receivePacket(respuesta2)

print('fin') '''
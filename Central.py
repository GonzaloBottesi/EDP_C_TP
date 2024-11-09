import csv
from TP_EDP import Telefono
import datetime

class Central():
    
    def __init__(self):
        self.telefonos=self.extraer_archivo('NOMBRE DEL ARCHIVO')
        self.registro_comunicaciones=()
        
    #Verificar si van todos los atributos del l
    
    def extraer_archivo(self, archivo_csv):
        telefonos=dict()
        try:
            with open(archivo_csv, mode='r', newline='') as archivo:
                lector_csv = csv.reader(archivo)
                next(lector_csv)
                for telefono in lector_csv:
                    telefonos[telefono[0]]=Telefono[telefono[0],telefono[1],telefono[2],telefono[3],
                                                    telefono[4],telefono[5],telefono[6],telefono[7]]
                
                    
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
            del self.telefonos[telefono.id]
            print (f"Se elimino el telefono con el id {telefono.id}")
        else:
            print (f"No se encuentra registrado el telefono con el numero {telefono.id}")
        
    def registrar_telefono(self, telefono:Telefono):
        if telefono.id not in self.telefonos: 
            self.telefonos[telefono.id]=telefono
            print (f"Se registro el telefono con el id {telefono.id}")
        else:
            print (f"Ya se encuentra registrado el telefono con el numero {telefono.id}")
    
    
    def verificar_disponibilidad_de_red(self, numero):
        if numero in self.telefonos:
            dispositivo = self.telefonos[numero]
            if dispositivo.encendido and dispositivo.red:
                print(f"El telefono con numero {numero} esta disponible.")
                return True
            else:
                print(f"El telefono con numero {numero} no esta disponible.")
                return False
        else:
            print(f"El telefono con numero {numero} no esta registrado.")
            return False
    
    def verificar_acceso_internet(self, numero):
        if numero in self.telefonos:
            dispositivo = self.telefonos[numero]
            if dispositivo.encendido and dispositivo.datos:
                print(f"El telefono con numero {numero} tiene acceso a internet.")
                return True
            else:
                print(f"El telefono con numero {numero} no tiene acceso a internet.")
                return False
        else:
            print(f"El telefono con numero {numero} no esta registrado.")
            return False
    def realizar_llamada(self, paquete_llamada):
        """Gestiona la llamada verificando la disponibilidad de Tel2 y notificando a Tel1 según la respuesta."""
        
        numero_origen = paquete_llamada[1]
        numero_destino = paquete_llamada[2]
        
        # Paso 1: Verificar si Tel2 está disponible
        if not self.verificar_disponibilidad_de_red(numero_destino):
            print(f"No se puede realizar la llamada. El número {numero_destino} está ocupado o sin red.")
            print(f"Notificando a {numero_origen} que {numero_destino} no está disponible.")
            self.registrar_comunicacion("no realizado", numero_origen, numero_destino)
            return
        
        # Paso 2: Enviar solicitud de llamada a Tel2
        print(f"Enviando solicitud de llamada de {numero_origen} a {numero_destino}.")
        respuesta = input(f"{numero_destino}, ¿acepta la llamada? (SI/NO): ").upper()
        
        # Paso 3: Evaluar respuesta de Tel2 y notificar a Tel1
        if respuesta == "SI":
            print(f"Llamada aceptada por {numero_destino}. Conectando...")
            self.telefonos[numero_origen].ocupado = True
            self.telefonos[numero_destino].ocupado = True
            self.registrar_comunicacion("realizada", numero_origen, numero_destino)
        else:
            print(f"Llamada rechazada por {numero_destino}. Notificando a {numero_origen}.")
            self.registrar_comunicacion("rechazada", numero_origen, numero_destino)
    
    def registrar_comunicacion(self, tipo, numero_origen, numero_destino, contenido=None):
        """Registra las comunicaciones según el tipo de respuesta de la llamada."""
        
        # Solo se registra la llamada si fue realizada o rechazada
        if tipo == "realizada":
            log = {
                'tipo': 'llamada',
                'numero_origen': numero_origen,
                'numero_destino': numero_destino,
                'fecha': datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                'contenido': "Llamada conectada"
            }
        elif tipo == "rechazada":
            log = {
                'tipo': 'llamada rechazada',
                'numero_origen': numero_origen,
                'numero_destino': numero_destino,
                'fecha': datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                'contenido': "Llamada rechazada"
            }
        else:
            log = {
                'tipo': 'no realizado',
                'numero_origen': numero_origen,
                'numero_destino': numero_destino,
                'fecha': datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                'contenido': "La llamada no se pudo realizar"
            }

        self.registro_comunicaciones.append(log)
        print(f"Comunicación registrada: {log}")
    
    def recibir_sms(self, paquete_sms):
        """Recibe un paquete SMS y lo procesa, verificando si el teléfono está registrado."""
        
        numero_origen = paquete_sms[1]
        numero_destino = paquete_sms[2]
        mensaje = paquete_sms[4]
        
        # Verificar si ambos teléfonos están registrados
        if numero_origen not in self.telefonos:
            print(f"El teléfono de origen {numero_origen} no está registrado en la central.")
            return
        
        if numero_destino not in self.telefonos:
            print(f"El teléfono de destino {numero_destino} no está registrado en la central.")
            return
        
        # Verificar si el teléfono origen está disponible para enviar el mensaje
        telefono_origen = self.telefonos[numero_origen]
        telefono_destino = self.telefonos[numero_destino]
        
        if not telefono_origen.encendido:
            print(f"El teléfono de origen {numero_origen} está apagado.")
            return
        
        if not telefono_destino.encendido:
            print(f"El teléfono de destino {numero_destino} está apagado.")
            return
        
        # Si todo está en orden, se recibe el mensaje
        print(f"Mensaje recibido de {numero_origen} a {numero_destino}: {mensaje}")
        self.registrar_comunicacion_sms("recibido", numero_origen, numero_destino, mensaje)






class Lista():
    def __init__(self):
        self.inicio = None
        
    def addStart (self,dato):
        if self.inicio == None:
            self.inicio = Nodo(dato)
    
class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

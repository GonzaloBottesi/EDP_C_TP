import datetime
from Aplicacion import Aplicacion


##Esta clase fue comentada para poder probar otra cosa. Sin embargo, no creo que tenga que tener ambos telefonos si hablamos de la aplicacion de llamadas
##En mi opinion, la aplicacion solo tiene que enviarle un paquete a la central y recibir un paquete de la central, toda la logistica de la llamada 
# se encarga la central (ver clase SMS para referencia)
##Ademas, si tuvieramos que importar el telefono entero volveriamos a un error de import ciclico asi que no se puede
##Toda la logistica de quien esta ocupado se tiene que encargar la central, ya que tiene la lista de telefonos conectados a la misma
## por eso, en caso de que un telefono este ocupado, le podria llegar al remitente un mensaje de la central indicandole que el destinatario esta ocupado
## Leer la parte de la comunicacion del TP. La dinamica es algo asi:
##              Tel1 solicita llamada con tel2 
#               central confirma que tel2 esta libre, si no esta le avisa a tel1
#               central le manda la llamada a tel2
#               tel2 recibe la llamada y le manda un paquete a la central con su respuesta [SI / NO]
#               la central le informa a tel1 de la respuesta de tel2 [Conecta la llamada / Termina]

## Cualquier cosa mandenme un mensaje al grupo y lo explico de vuelta, perdon por el testamento pero me parecio necesario



# class Llamadas(Aplicacion):
    
#     def __init__(self, telefono_origen, telefono_destino, peso):
#         super().__init__(peso)
#         self.telefono_origen = telefono_origen
#         self.telefono_destino = telefono_destino
#         self.en_curso = False

#     def iniciar(self):
#         if not self.abierto:
#             print("La aplicación Llamadas no está abierta.")
#             return False

#         if not (self.telefono_origen.ocupado or self.telefono_destino.ocupado):
#             self.telefono_origen.ocupado = True
#             self.telefono_destino.ocupado = True
#             self.en_curso = True
#             print(f"Llamada iniciada entre {self.telefono_origen.numero} y {self.telefono_destino.numero}.")
#             return True
#         else:
#             print("No se puede iniciar la llamada, uno de los teléfonos está ocupado.")
#             return False

#     def finalizar(self):
#         if self.en_curso:
#             self.telefono_origen.ocupado = False
#             self.telefono_destino.ocupado = False
#             self.en_curso = False
#             print(f"Llamada finalizada entre {self.telefono_origen.numero} y {self.telefono_destino.numero}.")
#             return True
#         else:
#             print("No hay una llamada en curso para finalizar.")
#             return False

#     def registrar(self, central):
#         central.registrar_comunicacion(
#             tipo="llamada",
#             numero_origen=self.telefono_origen.numero,
#             numero_destino=self.telefono_destino.numero
#         )


## Modelo de paquete a enviar: ['LLAMADA', Emisor , Receptor, datetime , pedido]. R = REQUEST ; B = BUSY ; N = NOT FOUND ; K = OK ; S = STOP ; F = RECHAZADO

class Llamadas(Aplicacion):
    def __init__(self, peso) -> None:
        super().__init__(peso)
        self.callHistory = dict()
        
    def sendCallRequest (self, tel1 : str):
        
        if 'En curso' in self.callHistory.values():
            print('Ya tiene una llamada en curso')
            return None
        
        tel2 = input('Ingrese el numero de telefono a llamar: ')
        
        packet = ['LLAMADA', tel1 , tel2 , datetime.datetime.now().replace(microsecond = 0).strftime("%d/%m/%Y, %H:%M:%S") ,'R']
        
        return packet
    
    def receivePacket(self, packet : list):
            
        if len(packet) != 5:
            print('Error en el largo del paquete')
            return False
        
        if packet[0] != 'LLAMADA':
            print(f'Error de paquete: no se puede procesar {packet[0]}')
            return False
        
        if not packet[4] in ['R' , 'B' , 'N' , 'K' , 'S']:
            print('Error al recibir el paquete: codigo de estado erroneo')
            return False
        
        if packet[4] == 'B':
            header = packet[2] + '-' + packet[3]
            self.callHistory.update({ header : 'Ocupado'})
            
        elif packet[4] == 'N':
            print ('El telefono no se encuentra en linea')
            
        elif packet[4] == 'K':
            header = packet[2] + '-' + packet[3]
            self.callHistory.update({ header : 'En curso'})
            
        elif packet [4] == 'S': ##Esto asume que tu propio numero de telefono esta en packet[1]
            header = packet[1] + '-' + packet[3]
            time1 = datetime.datetime.strptime(packet[3],"%d/%m/%Y, %H:%M:%S") ##Inicio de comunicacion
            time2 = datetime.datetime.now().replace(microsecond = 0) #Fin de comunicacion
            delta = time2 - time1
            self.callHistory.update({header : 'Duracion: ' + str(delta)})
            
        elif packet[4] == 'R':
            choice = None
            choice = input(f'Llamada entrante de {packet[1]} \n Aceptar? (Y/N)')
            choice.upper()
            while not choice in ['Y', 'N']:
                choice = input('Error, ingrese una opcion valida (Y/N)')
                choice.upper()
                    
            if choice == 'N':
                packet[4] = 'F'
                return packet
            else:
                header = packet[1] + '-' + packet[3]
                self.callHistory.update({header : 'En curso'})
                packet[4] = 'K'
                return packet
           
    def endCallRequest (self, tel1 : str):
        
        if 'En curso' not in self.callHistory.values():
            print('No hay llamada en curso')
            return False
        
        target = None
        
        for header in self.callHistory.keys():
            if self.callHistory[header] == 'En curso':
                target = header
                
        target = target.split('-')
        
        packet = ['LLAMADA', tel1 , target[0] , target[1] , 'S' ]
  
        time1 = datetime.datetime.strptime(target[1],"%d/%m/%Y, %H:%M:%S") ##Inicio de comunicacion
        time2 = datetime.datetime.now().replace(microsecond = 0) #Fin de comunicacion
        delta = time2 - time1
        
        self.callHistory.update({target[0] + '-' + target[1] : 'Duracion: ' + str(delta)})
        
        return packet
       
    def getCallHistory(self):
        
        if len(self.callHistory.keys()) == 0:
            print('No hay llamadas en el historial')
            return None
        
        for header, status in self.callHistory.items():
            print(f'{header}        {status}')
            return True
    
    @staticmethod
    def getDatetimeFromHeader (header : str):
        
        header.split(',')
        date = datetime.datetime.strptime(header[1], format = "%d/%m/%Y, %H:%M:%S")
        
        return date
  
Joaco = Llamadas(0) #Joaco 1162491238
Gonza = Llamadas(0) #Gonza 1159369841

packet = Joaco.sendCallRequest('1162491238')
response = Gonza.receivePacket(packet)
Joaco.receivePacket(response)

endPacket = Gonza.endCallRequest('1159369841')

Joaco.receivePacket(endPacket)

print(Gonza.callHistory)
print(Joaco.callHistory)

packet = Joaco.sendCallRequest('1162491238')
response = Gonza.receivePacket(packet)
Joaco.receivePacket(response)

endPacket = Joaco.endCallRequest('1162491238')

Gonza.receivePacket(endPacket)

print(Gonza.callHistory)
print(Joaco.callHistory)
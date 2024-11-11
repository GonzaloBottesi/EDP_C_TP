import datetime
from Aplicacion import Aplicacion
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
        
        if not packet[4] in ['R' , 'B' , 'N' , 'K' , 'S', 'F']: ##hacer caso F
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
        elif packet[4] == 'F':
            header = packet[1] + '-' + packet[3]
            self.callHistory.update({header : 'Rechazada'})
           
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
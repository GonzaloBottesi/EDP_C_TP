from Aplicacion import Aplicacion
from Stack import Stack
from TP_EDP import Telefono
import datetime

class SMS (Aplicacion):
    def __init__(self, peso) -> None:
        super().__init__(peso)
        self.bandeja = Stack()
        
    def sendMessage(self, tel : Telefono):
        
        """Arma el paquete de datos que envia a la central

        Returns:
            Packet: _Paquete de datos con orden ['SMS', Nro. Origen, Nro. Destino, Fecha y hora, Mensaje, Nombre (Si esta en contactos) / APODO]_
        """        
        
        destiny = input('Ingrese el numero del destinatario: ')
        message = input('Ingrese el mensaje:')
        
        packet = ['SMS',tel.numero , destiny, 'Fecha y hora' , message]
        
        return packet
    
    def receiveMessage (self, packet):
        
        if not isinstance(packet, list):
            raise TypeError ("Error en el tipo del paquete")
        
        if len(packet) < 4:
            raise   ValueError("El paquete no cuenta con los componentes minimos")
        
        if packet[0] != 'SMS':
            print ("El paquete no se puede procesar")
            return False
        
        for i in packet:
            if not isinstance(i, str):
                raise ValueError(f"Error en el dato {i} del paquete")
            
        
        if len(packet) == 6:
            header = packet[5] + ',' + packet[3]
        else:
            header = packet[1] + ',' + packet[3]
        message = packet
        
        filteredPacket = (header,message)
        
        self.bandeja.push(filteredPacket)
        
    def viewMessage():
        
        #Mostrar todos los mensajes de la bandeja, preferentemente paginada
        #Elegir un mensaje
        #Dentro del mensaje, dar la opcion de borrar
        
        pass

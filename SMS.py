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
            Packet: _Paquete de datos con orden [Nro. Origen, Nro. Destino, Fecha y hora, Mensaje]_
        """        
        
        destiny = input('Ingrese el numero del destinatario: ')
        message = input('Ingrese el mensaje:')
        
        packet = [tel.numero , destiny, 'Fecha y hora' , message]
        
        return packet
    
    def receiveMessage (self, packet):
        self.bandeja.push(packet)
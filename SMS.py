from Aplicacion import Aplicacion
import datetime

class SMS (Aplicacion):
    def __init__(self, peso) -> None:
        super().__init__(peso)
        self.bandeja = dict()
        
    def sendMessage(self, telNumber : str):
        
        """Arma el paquete de datos que envia a la central
        Args:
            telNumber: numero del telefono emisor
        Returns:
            Packet: _Paquete de datos con orden ['SMS', Nro. Origen, Nro. Destino, Fecha y hora, Mensaje, Nombre (Si esta en contactos) / APODO]_
        """        
        
        destiny = input('Ingrese el numero del destinatario: ')
        message = input('Ingrese el mensaje:')
        packet = ['SMS', telNumber , destiny, datetime.datetime.now().replace(microsecond = 0).strftime("%d/%m/%Y, %H:%M:%S") , message]
        return packet
    
    def receiveMessage (self, packet):
        """Recibe el mensaje y lo coloca en la bandeja de entrada

        Raises:
            TypeError: Salta si el paquete no es una lista
            ValueError: Salta si el paquete no cumple con los datos minimos o alguno de los datos no es de tipo str
            

        Returns:
            False: En caso de que el paquete no sea un mensaje SMS
        """        
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

        if len(packet) == 6: ##Tiene un apodo / esta en contactos (OPCIONAL, NO IMPLEMENTADO)
            header = packet[5] + ',' + packet[3]
        else:
            header = packet[1] + ',' + packet[3]
        message = packet[4]
        
        if message is None:
            print('El telefono no se encuentra en linea')
        else:
            self.bandeja.update({header : message})
    
    def eraseMessage(self):
        
        """Borra el mensaje, define si borra por numero de mensaje o por contenido del encabezado
        """        
        options = ['Y', 'N']
        choice = input('Quiere borrar multiples mensajes (Y/N)')
        choice = choice.upper()
        if not choice in options:
            print ('Error, por favor ingrese una opcion correcta')
          
        qty = self.viewMessage()  
            ##numero,fecha,hora
        if choice == 'Y':
            toErase = input('Ingrese el encabezado de los mensajes a borrar. Si ingresa una parte, se borraran todos aquellos que la contengan')
            self.eraseMessageBulk(toErase)
        else:
            toErase = input('Ingrese el numero del mensaje')
        
            if toErase.isdigit() and int(toErase) <= qty:
                self.eraseMessageSingle(int(toErase) - 1)
            else:
                print('Error: no existe el mensaje')
            
    def eraseMessageSingle(self, number):
    
        headerList = [* self.bandeja.keys()]
        self.bandeja.pop(headerList[number])
        print('Mensaje eliminado exitosamente')
        return 1
    
    def eraseMessageBulk(self, header):
            
        if not any(header in i for i in self.bandeja):
            print("No existe un encabezado con esos datos")
            return 0
                
        i = 0
        eraseList = []
        for hd in self.bandeja:
            if header in hd:
                i += 1
                eraseList.append(hd)
                
        for erase in eraseList:
            self.bandeja.pop(erase)
            
        print(f"Se eliminaron {i} mensajes")
        return i
      
    def viewMessage(self):
        
        ##El paginado se deja como extra en caso de que haya tiempo
        
        number = 1
        for header,message in self.bandeja.items():
            print(f'{number}. {header}: {message}')
            number += 1
        return number
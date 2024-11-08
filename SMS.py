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
        
        packet = ['SMS',telNumber , destiny, 'Fecha y hora' , message]
        
        return packet
    
    def receiveMessage (self, packet):
        
        #Falta codear el manejo de un paquete de error
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
            
        
        if len(packet) == 6: ##Tiene un apodo / esta en contactos
            header = packet[5] + ',' + packet[3]
        else:
            header = packet[1] + ',' + packet[3]
        message = packet[4]
        

        
        self.bandeja.update({header : message})
    
    def eraseMessage(self):
        self.viewMessage()
        
        toErase = input('Si desea eliminar un solo mensaje, ingrese el numero del mensaje.\n Si desea eliminar por encabezado, ingreselo.')
        
        if toErase.isdigit():
            self.eraseMessageSingle(int(toErase) - 1)
        else:
            self.eraseMessageBulk(toErase)
            
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
            
        return None
        
        ##Revisar codigo
        
        
        
        
        
        
        
        # Configuración para paginación
        page_size = 5  # Cantidad de mensajes por página
        total_messages = len(self.bandeja.items())
        
        if total_messages == 0:
            print("La bandeja de entrada está vacía.")
            return
        
        # Índice de inicio para la paginación
        start = 0
        
        while True:
            end = min(start + page_size, total_messages)
            print(f"\nMostrando mensajes {start + 1} a {end} de {total_messages}")
            
            # Mostrar encabezado de cada mensaje en la página actual
            for i in range(start, end):
                header, _ = self.bandeja.items[i]
                print(f"{i + 1}. {header}")
            
            # Opciones de navegación y selección, menu para la visualiza
            print("\nOpciones:")
            print("1. Elegir un mensaje para ver su contenido")
            print("2. Siguiente página")
            print("3. Página anterior")
            print("4. Salir de la bandeja")
            
            choice = input("Seleccione una opción: ")
            
            if choice == "1":
                # Seleccionar un mensaje para ver y dar opción de borrar
                index = int(input("Ingrese el número del mensaje para ver: ")) - 1
                if 0 <= index < total_messages:
                    header, message = self.bandeja.items[index]
                    print(f"\nMensaje de {header}:")
                    print(f"Contenido: {message}")
                    
                    # Opción de borrar el mensaje
                    delete_choice = input("¿Desea eliminar este mensaje? (s/n): ").lower()
                    if delete_choice == "s":
                        del self.bandeja.items[index]
                        total_messages -= 1
                        print("Mensaje eliminado.")
                        # Ajustar página en caso de que sea necesario
                        if start >= total_messages:
                            start = max(0, start - page_size)
                else:
                    print("Número de mensaje no válido.")
            
            elif choice == "2":
                # Siguiente página
                if end < total_messages:
                    start += page_size
                else:
                    print("No hay más páginas.")
            
            elif choice == "3":
                # Página anterior
                if start > 0:
                    start -= page_size
                else:
                    print("Ya está en la primera página.")
            
            elif choice == "4":
                # Salir de la vista de mensajes
                print("Saliendo de la bandeja de entrada.")
                break
            
            else:
                print("Opción no válida.")

            pass

test = SMS('0 k')
test.bandeja = {
  "brand": "Ford",
  "model": "Mustang",
  "year": '1964'
}
test.eraseMessage()
test.eraseMessage()
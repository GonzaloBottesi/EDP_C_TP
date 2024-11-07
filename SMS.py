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
        
    def viewMessage(self):
        
            #Mostrar todos los mensajes de la bandeja, preferentemente paginada
            #Elegir un mensaje
            #Dentro del mensaje, dar la opcion de borrar
        
        for header in self.bandeja:
            print(f'{number}. {header}: {self.bandeja[header]}')
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

    def menu():
        match input('¿Qué quiere hacer con los SMS?\n1. Enviar mensaje de SMS\n2. Recibir(?)\n3. Ver bandeja de entrada\n4. Ver historial de llamadas\n.5 Eliminar mensajes\n'):
            case '1':
                pass #COMPLETAR
            case '2':
                pass #COMPLETAR


testnumber = '1159369841'

test = SMS('0k')
message = test.sendMessage(testnumber)
test.receiveMessage(message)
test.viewMessage()
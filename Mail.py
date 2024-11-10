import csv
from Aplicacion import Aplicacion
from funciones_auxiliares import crear_archivo_no_existe, ListaEnlazada
from datetime import datetime

class Mail(Aplicacion):
    
    def __init__(self, peso):
        super().__init__(peso)
        crear_archivo_no_existe('mails.csv',['ID','DE','PARA','FECHA','MENSAJE','LECTURA'])
        self.mails=self.extraer_archivo('mails.csv')
     
    def extraer_archivo(self, archivo_csv):
        mails = {0:['-','-','-','Bienvenido a Mails','Leido']}
        try:
            with open(archivo_csv, mode='r', newline='', encoding= 'utf-8') as archivo:
                lector_csv = csv.reader(archivo)
                next(lector_csv)  # Saltar encabezados
                for mail in lector_csv:
                    mails[mail[0]] = (mail[1],mail[2],mail[3],mail[4]) 
            print("Todos los mails han sido registrados desde el archivo CSV.")
            return mails
        except FileNotFoundError:
            print("El archivo CSV no fue encontrado.")
        except KeyError as e:
            print(f"Error en el archivo CSV. Faltan columnas: {e}")
        except Exception as e:
            print(f"Se produjo un error al leer el archivo CSV: {e}")
    
    ''' Comentado para que no rompa, igualmente es funcion opcional
    def enviar_mail(self): # como se sabe que celular estas usando(?)
        id=input('Ingrese el ID del telefono que quiere enviar un mail')
        while id not in 'hola': # deberia chequear que el celular este en Fabrica de Telefonos que no se como hacerlo
            id=input('Ingrese el ID del telefono que quiere enviar un mail')
        mensaje=input('Ingrese el mensaje que le quiere enviar') 
        self.mails[self.mails.max()+1]=[self.mails.max()+1,'hola',id,datetime.now().strftime("%Y-%m-%d"),mensaje,'No leido'] # hola seria el ID del celular que se esta usando ahora
        print('Se envio el mail')
       '''  
       
    def ver_mail_por_no_leidos(self):
        lista_enlazada_ordenada = ListaEnlazada()
        
        # Primero agregamos los correos "No Leídos"
        for mail in self.mails:
            if self.mails[mail][4].strip().lower() == 'no leido':  # Comparación insensible a mayúsculas
                lista_enlazada_ordenada.add_to_end(self.mails[mail])
        
        # Luego agregamos los correos "Leídos"
        for mail in self.mails:
            if self.mails[mail][4].strip().lower() == 'leido':  # Comparación insensible a mayúsculas
                lista_enlazada_ordenada.add_to_end(self.mails[mail])
                
        for mail in lista_enlazada_ordenada:
            print(mail)
                
    def ver_mail_por_fecha(self): #value seria el mail
        lista_enlazada_desc = sorted(
        [value for key,value in self.mails if value[1] == 'hola'], # ID del usuario que esta usando la aplicacion
        key=lambda x: x[3],  
        reverse=True
    )
        for mail in lista_enlazada_desc:
            print(mail)

    #Falta responder los comentarios y si se hace esto, guardar el archivo al final

'''self.mails = [
    ["Informe Mensual", "2024-10-01", "No leído", 15],
    ["Actualización del Proyecto", "2024-10-05", "Leído", 7],
    ["Reunión de Seguimiento", "2024-10-10", "No leído", 12],
    ["Oferta Especial", "2024-10-12", "No leído", 3],
    ["Agenda de la Semana", "2024-10-15", "Leído", 20],
    ["Resumen Anual", "2024-10-18", "No leído", 10],
    ["Recordatorio de Pago", "2024-10-20", "No leído", 5],
    ["Invitación al Evento", "2024-10-22", "Leído", 18],
    ["Actualización de Seguridad", "2024-10-25", "No leído", 2],
    ["Nuevo Protocolo", "2024-10-28", "Leído", 9]]
    viejo self.mail() si es muy dificil, se vuelve a esto'''
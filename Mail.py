from Aplicacion import Aplicacion
from funciones_auxiliares import ListaEnlazada

class Mail(Aplicacion):
    
    def __init__(self, peso):
        super().__init__(peso)
        self.mails= [
        ["Informe Mensual", "2024-10-01", "No leído", 15],
        ["Actualización del Proyecto", "2024-10-05", "Leído", 7],
        ["Reunión de Seguimiento", "2024-10-10", "No leído", 12],
        ["Oferta Especial", "2024-10-12", "No leído", 3],
        ["Agenda de la Semana", "2024-10-15", "Leído", 20],
        ["Resumen Anual", "2024-10-18", "No leído", 10],
        ["Recordatorio de Pago", "2024-10-20", "No leído", 5],
        ["Invitación al Evento", "2024-10-22", "Leído", 18],
        ["Actualización de Seguridad", "2024-10-25", "No leído", 2],
        ["Nuevo Protocolo", "2024-10-28", "Leído", 9] # poner esto en la clase MAILS #titulo,fecha,leido,quien lo envio
        ]
        
    def ver_mail_por_no_leidos(self):
        lista_enlazada_ordenada = ListaEnlazada()
        
        for mail in self.mails:
            if mail[2].strip().lower() == 'no leido':  # Comparación insensible a mayúsculas
                lista_enlazada_ordenada.add_to_end(mail)
        
        for mail in self.mails:
            if mail[2].strip().lower() == 'leido':  # Comparación insensible a mayúsculas
                lista_enlazada_ordenada.add_to_end(mail)
                
    def ver_mail_por_fecha(self):
        lista_enlazada_desc= ListaEnlazada()
        lista_enlazada_desc = sorted(self.mails, key=lambda x: x[1], reverse=True)
        for mail in lista_enlazada_desc:
            print(mail)
        

        
        
        
        
 
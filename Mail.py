from Aplicacion import Aplicacion

class Mail(Aplicacion):
    
    def __init__(self, peso):
        super().__init__(peso)
        self.mails=[]
    def agregar_mail(self, asunto, fecha, leido=False):
            
            self.mails.append({
                'asunto': asunto,
                'fecha': fecha,
                'leido': leido
                })

    def obtener_mail(self,criterio='no leidos'):
        if criterio=='no leido':
            mails_ordenados= sorted(self.mails, key=lambda x: (x['leido'], x['fecha']),reverse=True)
        
        elif criterio == 'fecha':
            mails_ordenados = sorted(self.mails,key=lambda x: x['fecha'],reverse=True)
        
        else:
            raise ValueError('criterio solo puede ser "no leido" o "fecha"')
        for m in mails_ordenados:
            leido = "Leido" if m['leido'] else "No leido"
            print(f"Asunto: {m['asunto']}, Fecha: {m['fecha']}, Estado: {leido}")

    
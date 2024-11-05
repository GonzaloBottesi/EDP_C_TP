#Clase aplicacion y derivados
from TP_EDP import Telefono
import csv

class Aplicacion:
    def __init__(self, peso : int) -> None: # Peso en bytes 
        self.abierto = False
        self.peso = peso

    def onOff (self):
        self.abierto = not self.abierto
    
class Config(Aplicacion):
    def __init__(self, peso):
        super().__init__(peso)
    
    def changePassword(self, tel : Telefono): ##Hay que pasarle el telefono sobre el que esta actuando
        
        if not isinstance(tel, Telefono):
            raise TypeError ("Clase incorrecta")
        
        password = input ("Ingrese contraseña actual")
        
        if tel.pin != password:
            print ("Contraseña incorrecta")
            return False
        
        newpassword = input("Ingrese contraseña nueva")
        
        if input("Ingrese nuevamente") != newpassword:
            print("Contraseña incorrecta")
            return False
        
        tel.pin = newpassword
        return True
        
        
    def setName (self, tel : Telefono):
        
        if not isinstance(tel, Telefono):
            raise TypeError ("Clase incorrecta")
        
        password = input("ingrese contraseña actual")
        
        if tel.pin == password:
            newname = input ("Ingrese nombre nuevo")
            tel.nombre = newname
            return True
        else:
            print("Contraseña incorrecta")
            return False
        
    def red(self, tel : Telefono):
        if isinstance(tel, Telefono):
            tel.red = not tel.red
               
        else:
            raise TypeError ("Clase incorrecta")
        
    def datos(self, tel : Telefono):
        if isinstance(tel, Telefono):
            tel.datos = not tel.datos
               
        else:
            raise TypeError ("Clase incorrecta")
    def menu(self):
        match input('¿Qué quiere hacer con ?'):
            case '1':
                pass #COMPLETAR
            case '2':
                pass #COMPLETAR
        
class AppStore (Aplicacion):
    def __init__(self, peso):
        super().__init__(peso)
        self.listaAppsDisponibles = []
    
    
    def getApps(self):
        """
        Lee el archivo csv para obtener las aplicaciones de la app store
        
        Returns:
            Pares [Nombre,peso(bytes)] del csv
        
        """
        
        pass #COMPLET
    
        
    def installApp (self, tel : Telefono, nombre):
        
        """
        Instala la aplicacion dado el nombre
        
        Args:
            tel: Instancia de Telefono donde instalar la app
            nombre: Nombre de la aplicación
            listaApps: Lista con todas las aplicaciones descargables, junto con 
            su respectivo peso en bytes
            
        Notes:
            Cuidado con la instancia de Telefono que se pasa, asi se evita
            instalar en un telefono incorrecto
         """
        
        
        if not isinstance(tel, Telefono):       #Busca si se paso una clase incorrecta
            raise TypeError("Clase Incorrecta")
        
        if not tel.datos:                       #Se fija que este conectado a internet
            print("No hay conexion a internet")
        
        if nombre in tel.listaApps.keys():      #Evita que se instale una aplicacion ya instalada
            print("Aplicacion ya instalada")
            
        elif nombre in self.listaAppsDisponibles:
            
            i = 0
            while self.listaAppsDisponibles[i] != nombre:
                i +=1 
            peso = None #
            if tel.almacenamiento <= peso :
                tel.listaApps.update({nombre : Aplicacion(peso)})
                tel.almacenamiento -= peso
            else:
                print("Espacio insuficiente")
        else:
            print("No existe esa aplicacion en la tienda")

        
    def uninstallApp (self, tel : Telefono, nombre):
        
        if isinstance(tel, Telefono):
            if nombre in tel.listaApps.keys():
                app : Aplicacion = tel.listaApps.get(nombre)
                tel.almacenamiento += app.peso
                tel.listaApps.pop(nombre)
            else:
                print("Aplicacion no instalada")
     
        else:
            raise TypeError ("Clase Incorrecta")
        
    def menu(self):
        match input('¿Qué quiere hacer con la AppStore?'):
            case '1':
                pass #COMPLETAR
            case '2':
                pass #COMPLETAR
        
class Contactos(Aplicacion):
    def __init__(self, peso):
        super().__init__(peso)
        self.listaContactos = dict() # Acceso mas facil a los contactos, se puede guardar un CSV para cada telefono
        
    
    def addContact(self, name, number):
        
        if name in self.listaContactos.keys():
            print("Ya existe un contacto con ese nombre")
        
        if isinstance(name, str) and isinstance(number, int):
            self.listaContactos.update({name : number}) 
        else:
            if isinstance (name, str):
                raise ValueError("Error al ingresar el nombre, por favor ingrese")
            else:
                raise ValueError("Error al ingresar el numero, ingrese un numero valido")
    
    def deleteContact (self, name):
        try:
            self.listaContactos.pop(name)
        except KeyError:
            print ("Error, no existe un contacto con ese nombre")
            return 0
    
    def updateContact (self, name, value):
        
        if not name in self.listaContactos.keys():
            print ("El contacto no existe")
        else:
            self.listaContactos.update({name : value})

    def menu(self):
        match input('¿Qué quiere hacer con la aplicacion Contactos?'):
            case '1':
                pass #COMPLETAR
            case '2':
                pass #COMPLETAR



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

    def menu(self):
        match input('¿Qué quiere hacer con su Mail?'):
            case '1':
                pass #COMPLETAR
            case '2':
                pass #COMPLETAR
        
    
            
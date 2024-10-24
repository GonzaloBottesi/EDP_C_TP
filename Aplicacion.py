#Clase aplicacion y derivados
from TP_EDP import Telefono


class Aplicacion():
    def __init__(self, peso) -> None:
        self.abierto = False
        self.peso = peso

    def onOff (self):
        self.encendido = not self.encendido
    
class Config(Aplicacion):
    def __init__(self, peso):
        super().__init__(peso)
    
    def changePassword(self, tel : Telefono): ##Pasar a la app Configuracion
        
        if isinstance(tel,Telefono):
            password = input("ingrese contraseña actual")
            
            if tel.pin == password:
                newpassword = input ("Ingrese contraseña nueva")
                if input ("Ingrese nuevamente") == newpassword:
                    tel.pin = newpassword
                    return True
                else:
                    print ("Contraseña incorrecta")
                    return False
            else:
                print("Contraseña incorrecta")
                return False   
        else:
            raise TypeError ("Clase incorrecta")
        
    def setName (self, tel : Telefono):
        if isinstance(tel,Telefono):
            password = input("ingrese contraseña actual")
            if tel.pin == password:
                newname = input ("Ingrese nombre nuevo")
                tel.nombre = newname
                return True
            else:
                print("Contraseña incorrecta")
                return False
                
        else:
            raise TypeError ("Clase incorrecta")
        
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
        
class AppStore (Aplicacion):
    def __init__(self, peso):
        super().__init__(peso)
        self.listaApps = []
        
    def installApp (self, tel : Telefono, nombre):
        if isinstance (tel, Telefono):
            if tel.datos:
                if nombre in tel.listaApps.keys():
                    print("Aplicacion ya instalada")
                elif nombre in self.listaApps:
                    
                    i = 0
                    while self.listaApps[i] != nombre:
                        i +=1 
                    peso = None
                    if tel.almacenamiento <= peso :
                        tel.listaApps.update({nombre : Aplicacion(peso)})
                        tel.almacenamiento -= peso
                    else:
                        print("Espacio insuficiente")
                else:
                    print("No existe esa aplicacion en la tienda")
            else:
                print("No hay conexion a internet")
        else:
            raise TypeError("Clase incorrecta")
        
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
from Aplicacion import Aplicacion
from Parametros import ConfigParameters

#Estoy importando Telefono a cada metodo para evitar un import circular

class Config(Aplicacion):
    """Subclase de Aplicacion con los metodos para congifurar el telefono

    Args:
        Aplicacion (_Clase_ _padre_)
    """    
    def __init__(self, peso):
        super().__init__(peso)
    
    def changePassword(self, tel : ConfigParameters): ##Hay que pasarle el telefono sobre el que esta actuando
        
        
        if not isinstance(tel, ConfigParameters):
            raise TypeError ("Clase incorrecta")
        
        password = input ("Ingrese contraseña actual")
        
        if self.telefono.pin != password:
            print ("Contraseña incorrecta")
            return False
        
        newpassword = input("Ingrese contraseña nueva")
        
        if input("Ingrese nuevamente") != newpassword:
            print("Contraseña incorrecta")
            return False
        
        tel.pin = newpassword
        return True
        
        
    def setName (self, tel):
        
        
        if not isinstance(tel, ConfigParameters):
            raise TypeError ("Clase incorrecta")
        
        password = input("ingrese contraseña actual")
        
        if tel.pin == password:
            newname = input ("Ingrese nombre nuevo")
            tel.nombre = newname
            return True
        else:
            print("Contraseña incorrecta")
            return False
        
    def red(self, tel):
        
        if isinstance(tel, ConfigParameters):
            tel.red = not tel.red

        else:
            raise TypeError ("Clase incorrecta")

    def datos(self, tel : ConfigParameters):


        if isinstance(tel, ConfigParameters):
            tel.datos = not tel.datos

        else:
            raise TypeError ("Clase incorrecta")

    def menu(self,tel):
        match input('¿Qué quiere hacer con la configuracion?\n1. Cambiar nombre de telefono\n2. Cambiar codigo de desbloqueo\n3. Activar red movil\n4. Desactivar red movil\n5. Activar datos\n6. Desactivar datos\n'):
            case '1':
                self.setName(tel)
            case '2':
                self.changePassword(tel)
            case '3':
                self.red() # diferencia entre 3 y 4
            case '4':
                self.red()# diferenciar entre 3 y 4
            case '5':
                self.datos() # diferenciar entre 5 y 6
            case '6':
                self.datos() # diferenciar entre 5 y 6

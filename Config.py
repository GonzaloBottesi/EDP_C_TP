from Aplicacion import Aplicacion
#Estoy importando Telefono a cada metodo para evitar un import circular

class Config(Aplicacion):
    """Subclase de Aplicacion con los metodos para congifurar el telefono

    Args:
        Aplicacion (_Clase_ _padre_)
    """    
    def __init__(self, peso):
        super().__init__(peso)
    
    def changePassword(self, tel): ##Hay que pasarle el telefono sobre el que esta actuando
        
        from TP_EDP import Telefono
        
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
        
        
    def setName (self, tel):
        
        from TP_EDP import Telefono
        
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
        
    def red(self, tel):
        from TP_EDP import Telefono
        
        if isinstance(tel, Telefono):
            tel.red = not tel.red

        else:
            raise TypeError ("Clase incorrecta")

    def datos(self, tel):

        from TP_EDP import Telefono

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
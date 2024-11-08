from Aplicacion import Aplicacion

class Contactos(Aplicacion):
    def __init__(self, peso):
        super().__init__(peso)
        self.listaContactos = dict()
        
    
    def addContact(self, name : str, number : str):
        
        if name in self.listaContactos.keys():
            print("Ya existe un contacto con ese nombre")
        
        if isinstance(name, str) and number.isnumeric():
            self.listaContactos.update({name : number}) 
        else:
            if not isinstance (name, str):
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

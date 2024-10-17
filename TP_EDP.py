class Telefono():
    
    def __init__(self, nombre, modelo) -> None:
        
        #self.id
        self.nombre = nombre
        self.modelo = modelo
        #self.os
        #self.version
        #self.ram
        #self.almacenamiento
        #self.numero
        self.encendido = False
        self.bloqueado = True
        self.pin = None
        
        return None
        
    def powerButton(self):       
        self.encendido = not self.encendido
    
    def setPassword(self, password):
        self.pin = password
    
    def unlock(self, password = None):
        
        if self.encendido:
    
            if not self.bloqueado:
                print ("El telefono ya se encuentra desbloqueado")
            elif self.pin == None:
                self.bloqueado = False
            else:
                if self.pin == password:
                    self.bloqueado = False
                else:
                    print("Contraseña incorrecta")
        
        
        else:
            print("El telefono esta apagado")    
    
        
               
class Aplicacion():
    def __init__(self, peso) -> None:
        self.encendido = False
        self.peso = peso
        

class Apple():
    def __init__(self,nroiphone) -> None:
        self.nroiphone=nroiphone
        
        
tel1 = Telefono("Gonzalo","Samsung S22")

tel1.setPassword('1234')
tel1.powerButton()
tel1.unlock()

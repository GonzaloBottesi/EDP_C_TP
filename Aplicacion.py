#Clase aplicacion y derivados

class Aplicacion:
    def __init__(self, peso : int) -> None: # Peso en bytes 
        self.abierto = False
        self.peso = self.tamanio_a_bytes(peso)

    def onOff (self):
        self.abierto = not self.abierto
<<<<<<< HEAD
    
class Config(Aplicacion):
    def __init__(self, peso):
        super().__init__(peso)
    
    def changePassword(self, tel : Telefono): ##Hay que pasarle el telefono sobre el que esta actuando
        
        if not isinstance(tel, Telefono):
            raise TypeError ("Clase incorrecta")
        
        password = input ("Ingrese contraseña actual:\n")
        
        if tel.pin != password:
            print ("Contraseña incorrecta")
            return False
        
        newpassword = input("Ingrese contraseña nueva:\n")
        
        if input("Ingrese nuevamente") != newpassword:
            print("Contraseña incorrecta")
            return False
        
        tel.pin = newpassword
        return True
        
        
    def setName (self, tel : Telefono):
        
        if not isinstance(tel, Telefono):
            raise TypeError ("Clase incorrecta")
        
        password = input("Ingrese contraseña actual:\n")
        
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
            if tel.red == True:
                print('Se activo la red')
            elif tel.red == False:
                print('Se desactivo la red')
                
               
        else:
            raise TypeError ("Clase incorrecta")
        
    def datos(self, tel : Telefono):
        if isinstance(tel, Telefono):
            tel.datos = not tel.datos
            if tel.datos == True:
                print('Se activaron los datos')
            elif tel.red == False:
                print('Se desactivaron los datos')
               
        else:
            raise TypeError ("Clase incorrecta")
    def menu(self,tel: Telefono):
        match input('¿Qué quiere hacer con la configuracion?\n1. Cambiar el nombre del telefono\n2. Cambiar el codigo de desbloqueo\n3. Desactivar red movil\n4. Acivar\Desactivar datos\n5. Salir\n'):
            case '1':
                self.setName(tel)
                self.menu(tel)
            case '2':
                self.changePassword(tel)
                self.menu(tel)
            case '3':
                self.red(tel)
                self.menu(tel)
            case '4':
                self.datos(tel)
                self.menu(tel)
            case '5':
                Telefono.menu()
            case other:
                print('Esta opcion no esta dispoible')
                self.menu(self)
                
            
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
=======
>>>>>>> fb521e65bcb0d8341f148f4af333a51684d9dcdd
        
    @staticmethod
    def tamanio_a_bytes(tamanio_formateado):
        """Convierte una cadena de tamaño formateado (ej. "117.74 MB") a su valor en bytes.

        Args:
            tamanio_formateado (str): Tamaño en formato de cadena con sufijo (ej. "1.5 GB").

        Returns:
            int: El tamaño convertido a bytes.

        Raises:
            ValueError: Si el formato de entrada no es válido.
        """
        # Arreglo temporal, posiblemente se altere el csv
        if tamanio_formateado == 'Varies with device':
            tamanio_formateado = '0 K'
            
        if isinstance(tamanio_formateado, int):
           return int(float(tamanio_formateado))
        
        # Quitar espacios, convertir a mayúsculas, y eliminar la letra "B" si existe
        tamanio_formateado = tamanio_formateado.replace(" ", "").upper().replace("B", "")

<<<<<<< HEAD
        
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
        
    def menu(self,tel:Telefono):
        match input('¿Qué quiere hacer con la AppStore?\n1. Descargar una app\n2. Eliminar una app'):
            case '1':
                self.installApp(tel)
                self.menu(tel)
            case '2':
                self.uninstallApp(tel)
                self.menu(tel)
            case '3':
                Telefono.menu()
            case other:
                print('Esta opcion no esta disponible')
                self.menu()
        
class Contactos(Aplicacion):
    def __init__(self, peso):
        super().__init__(peso)
        self.listaContactos = dict() # Acceso mas facil a los contactos, se puede guardar un CSV para cada telefono
        #leer archivo
        
    
    def addContact(self):
        name= input('Ingrese el nombre del contacto que quiere agregar:\n')
        if name in self.listaContactos.keys():
            print("Ya existe un contacto con ese nombre")
        
        number=input('Ingrese el numero del contacto que quiere agregar:\n')
        
        if isinstance(name, str) and isinstance(number, int): # no habria que verificar que no exista el numero de celular?
            self.listaContactos.update({name : number}) 
        else:
            if isinstance (name, str):
                raise ValueError("Error al ingresar el nombre, por favor ingrese")
            else:
                raise ValueError("Error al ingresar el numero, ingrese un numero valido")
    
    def deleteContact (self, name):
        name= input('Ingrese el nombre del contacto que quiere eliminar:\n')
        try:
            self.listaContactos.pop(name)
        except KeyError:
            print ("Error, no existe un contacto con ese nombre")
            return 0
    
    def updateContact (self, name, value):
        name = input('Ingrese el nombre del contacto:\n')
        value= input('Ingrese el nombre de su valor:\n') #cambiar lo del valor
        if not name in self.listaContactos.keys():
            print ("El contacto no existe")
        else:
            self.listaContactos.update({name : value})

    def menu(self, tel :Telefono): #porque en contactos no hace falta saber que telefono usas?
        match input('¿Qué quiere hacer con la aplicacion Contactos?\n1. Agregar contactos\n2. Borrar contactos\n3. Actualizar contactos\n4. Salir '):
            case '1':
                self.addContact()
                self.menu()
            case '2':
                self.deleteContact()
                self.menu()
            case '3':
                self.updateContact() # que seria update contactos?? 
                self.menu()
            case '4':
                # actualizar los contactos (ver si es lo mismo que update)
                Telefono.menu()
            case other:
                print('Esta opcion no esta dispoible')
                self.menu()
                
=======
        # Diccionario de sufijos y su potencia de 1024 correspondiente
        sufijos = {"K": 1, "M": 2, "G": 3, "T": 4, "P": 5}

        # Recorrer el diccionario para encontrar el sufijo que coincida al final de la cadena
        for sufijo, potencia in sufijos.items():
            if tamanio_formateado.endswith(sufijo):
                # Extraer la parte numérica y convertirla a float
                valor = float(tamanio_formateado[:-len(sufijo)])
                # Calcular el tamaño en bytes usando la potencia de 1024
                return int(valor * (1024 ** potencia))

        # Si no hay sufijo (es decir, el valor está en bytes), convertir directamente
        return int(float(tamanio_formateado))
>>>>>>> fb521e65bcb0d8341f148f4af333a51684d9dcdd


########## Metodo tambien esta en TP_EDP (en la clase telefono)
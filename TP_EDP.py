import csv
from Config import Config
from Parametros import ConfigParameters
from Aplicacion import Aplicacion
from Appstore import AppStore
from Mail import Mail
from Contactos import Contactos
from LLamadas import Llamadas
from SMS import SMS

class Telefono:
    
    def __init__(self, id, nombre, modelo, os, version, ram, almacenamiento: int, numero) -> None:
        
        self.listaApps = dict()
        self.listaApps.update({"AppStore" : AppStore('0 K'), 
                               "Config" : Config('0 K'), 
                               "Llamadas" : Llamadas('0 K'), 
                               "Mail" : Mail('0 K'), 
                               "SMS" : SMS('0 K') , 
                               "Contactos" : Contactos('0 K')})
        self.id = id
        self.nombre = nombre
        self.modelo = modelo
        self.os = os
        self.ram = ram

        self.configParameters = ConfigParameters(nombre, password = '', datos = False, red = True, 
                                           almacenamiento = self.tamanio_a_bytes(almacenamiento), version = version)
        
        self.numero = numero    
        self.encendido = False
        self.bloqueado = True
        
        self.aplicacionActual = None
        self.ocupado = False

    def powerButton(self):
        """
        Prende y apaga el telefono
        """        
        if self.bloqueado:    
            self.encendido = True
        print('Se prendio el celular')
    
    def Apagar(self):
        if self.encendido :
            self.encendido = False
            print('Se apago el Telefono')
        
    def lock(self):
        self.bloqueado = True
            
    def unlock(self, password=None):
        
        """Desbloquea el telefono
        
        Args:
            Password: Clave del telefono, valor default None

        Returns:
            Bool: True si se desbloqueo, False si no
        """        """
        
        
        """        
        
        if self.encendido:
            if not self.bloqueado:
                print("El teléfono ya se encuentra desbloqueado")
                return True
            elif self.configParameters.pin is None:
                self.bloqueado = False
                return True
            else:
                if self.configParameters.pin == password:
                    self.bloqueado = False
                    return True
                else:
                    print("Contraseña incorrecta")
                    return False
        else:
            print("El teléfono está apagado")
            return False   
    
    def openApp(self):
        
        """Abre la aplicacion y le asigna a self.aplicacionActual el puntero a la aplicacion abierta
            Para usar una aplicacion, usar el atributo aplicacionActual y ckequear que la clase sea la que necesiten
        Returns:
            type: Clase de la aplicacion abierta, si es descargada de la Appstore, tiene la clase Aplicacion
        """        
        
        nameList = self.listaApps.keys()
        
        print('Aplicaciones instaladas: \n')
        
        i = 1
        for app in nameList:
            print(f'{i}. {app}')
            i += 1
            
        selectedApp = input('Escriba el nombre de la aplicacion')
            
        
        self.aplicacionActual = self.listaApps.get(selectedApp)
        
        return type(self.listaApps.get(selectedApp))
    
    
    def mostrar_estado(self):
        red_estado = "activa" if self.configParameters.red else "desactivada"
        datos_estado = "activados" if self.configParameters.datos else "desactivados"
        print(f"Red móvil: {red_estado}, Datos móviles: {datos_estado}")


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
        if isinstance(tamanio_formateado, int):
            return int(float(tamanio_formateado))
        
        # Quitar espacios, convertir a mayúsculas, y eliminar la letra "B" si existe
        tamanio_formateado = tamanio_formateado.replace(" ", "").upper().replace("B", "")

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

    def __str__(self) -> str:
        string = f'Telefono de {self.nombre}; Num: {self.numero} ; Modelo {self.modelo}'
        return string
    
    
class FabricaDeTelefonos:
    def __init__(self):
        self.crear_archivo_no_existe('telefonos.csv', ['ID', 'NOMBRE', 'MODELO', 'OS', 'VERSION', 'RAM', 'ALMACENAMIENTO', 'NUMERO'])
        self.telefonos = self.extraer_archivo('telefonos.csv')

    def crear_archivo_no_existe(self, archivo, filas_iniciales): # ESTA EN FUNCIONES AUXILIARES
        try:
            with open(archivo, 'x', encoding='utf-8', newline='') as arch:
                escritor = csv.writer(arch)
                escritor.writerow(filas_iniciales)  # Escribir encabezados
                return 
        except FileExistsError:
            return
  
    def extraer_archivo(self, archivo_csv): # ESTA EN FUNCIONES AUXILIARES
        telefonos = dict()
        try:
            with open(archivo_csv, mode='r', newline='', encoding='utf-8') as archivo:
                lector_csv = csv.reader(archivo)
                next(lector_csv)  # Saltar encabezados
                for telefono in lector_csv:
                    telefonos[telefono[0]] = Telefono(telefono[0], telefono[1], telefono[2], telefono[3],
                                                       telefono[4], telefono[5], int(telefono[6]), telefono[7]) #ver cuales son ints
                  
            print("Todos los teléfonos han sido registrados desde el archivo CSV.")
            return telefonos
        except FileNotFoundError:
            print("El archivo CSV no fue encontrado.")
        except KeyError as e:
            print(f"Error en el archivo CSV. Faltan columnas: {e}")
        except Exception as e:
            print(f"Se produjo un error al leer el archivo CSV: {e}")

    def crear_telefono(self):
        id = input('Ingrese el ID de su teléfono: ')
        while id in self.telefonos or not id.isdigit():
            id = input('Error en la introducción del ID\nIngrese el ID de su teléfono:')
        nombre = input('Ingrese el nombre de su teléfono: ')
        modelo = input('Ingrese el modelo de su teléfono: ')
        os = input('Ingrese el sistema operativo: ')
        version = input ('Ingrese la version: ')
        ram = input('Ingrese la RAM: ')
        almacenamiento = input('Ingrese el tamaño de almacenamiento: ')
        #while not almacenamiento.isdigit():
         #   almacenamiento = input('Error en el ingreso del almacenamiento.\nIngrese el tamaño de almacenamiento:')
        telefono = Telefono(id, nombre, modelo, os, version, ram, almacenamiento, None)  # Asigna None o un valor a `numero`
        self.telefonos[id] = telefono

    def eliminar_telefono(self):
        if self.telefonos:
            id = input('Ingrese el ID del celular que quiere eliminar: ')
            while id not in self.telefonos:
                id = input('No existe ese ID\nIngrese el ID del celular que quiere eliminar: ')
            del self.telefonos[id]
        else:
            print('No hay telefonos creados')
     
    def elegir_telefono(self):
        if self.telefonos:
            id = input('Ingrese el ID del celular que quiere usar: ')
            while id not in self.telefonos:
                id = input('No existe ese ID\nIngrese el ID del celular que quiere usar: ')
            return self.telefonos[id]
        else:
            print('No hay telefonos creados ')
    
    def actualizar_archivos(self): # ESTA EN FUNCIONES AUXILIARES
        with open('telefonos.csv', 'w', encoding='utf-8', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(['ID', 'NOMBRE', 'MODELO', 'OS', 'VERSION', 'RAM', 'ALMACENAMIENTO', 'NUMERO'])  # Escribir encabezados
            for telefono in self.telefonos.values():
                escritor.writerow([telefono.id, telefono.configParameters.nombre, telefono.modelo, telefono.os,
                                   telefono.configParameters.version, telefono.ram, telefono.configParameters.almacenamiento, telefono.numero])
    

# Crear una instancia de FabricaDeTelefonos y llamar al menú
# mi_fabrica = FabricaDeTelefonos()  # Crear la instancia
# mi_fabrica.menu_de_telefonos()  # Llamar al método del menú
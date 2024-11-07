import csv
import Config
import Aplicacion
import AppStore
import Mail
import Contactos

class Telefono:
    
    def __init__(self, id, nombre, modelo, os, version, ram, almacenamiento: int, numero) -> None:
        self.listaApps = dict()
        self.id = id
        self.nombre = nombre
        self.modelo = modelo
        self.os = os
        self.version = version
        self.ram = ram
        self.almacenamiento = almacenamiento
        self.numero = numero
        
        self.encendido = False
        self.bloqueado = True
        self.pin = None
        self.aplicacionActual = None
        self.red = False
        self.datos = False
        self.ocupado = False

    def powerButton(self):
        """
        Prende y apaga el telefono
        """        
        if self.bloqueado:    
            self.encendido = True
    
    def Apagar(self):
        if self.encendido and self.bloqueado:
            self.encendido = False
        elif self.encendido and not self.bloqueado:
            self.encendido = False
            self.bloqueado = True 
        
            

    def unlock(self, password=None):
        
        """
        Desbloquea el telefono
        
        Args:
            Password: Clave del telefono, valor default None
        
        """        
        
        if self.encendido:
            if not self.bloqueado:
                print("El teléfono ya se encuentra desbloqueado")
            elif self.pin is None:
                self.bloqueado = False
            else:
                if self.pin == password:
                    self.bloqueado = False
                else:
                    print("Contraseña incorrecta")
        else:
            print("El teléfono está apagado")    
    
    def mostrar_estado(self):
        red_estado = "activa" if self.red else "desactivada"
        datos_estado = "activados" if self.datos else "desactivados"
        print(f"Red móvil: {red_estado}, Datos móviles: {datos_estado}")

    def menu(self):
        self.powerButton() # Al entrar al menu se prende solo el celular
        
        if self.encendido and self.bloqueado: # Si el celular esta bloqueado
            match input('¿Qué quiere hacer con el celular?\n1. Desbloquear\n2. Apagar '):
                case '1':
                    self.unlock()
                    self.menu()
                case '2':
                    self.Apagar()
                    FabricaDeTelefonos.menu_de_telefonos()
                case other:
                    print('Esta opción no está disponible')
                    self.menu()

        elif self.encendido and not self.bloqueado: # Si el celular esta desbloqueado
            match input('''¿Qué aplicación quiere utilizar?\n1. Llamadas\n2. Contactos\n3. Mensaje de texto\n4. Mail\n5. App store\n6. Configuración\n7. Apagar'''):
                case '1':
                    #Llamadas.menu() todavia no creado
                    pass
                case '2':
                    Contactos.menu()
                case '3':
                    #Sms.menu() todavia no creado
                    pass
                case '4':
                    Mail.menu()
                case '5':
                    AppStore.menu()
                case '6':
                    Config.menu()
                case '7':
                    self.Apagar()
                case other:
                    print('Esa opción no está disponible en este momento')
                    self.menu()
        else:
            print('Algo funciona mal')

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

class FabricaDeTelefonos:
    def __init__(self):
        self.crear_archivo_no_existe('telefonos.csv', ['ID', 'NOMBRE', 'MODELO', 'OS', 'VERSION', 'RAM', 'ALMACENAMIENTO', 'NUMERO'])
        self.telefonos = self.extraer_archivo('telefonos.csv')

    def crear_archivo_no_existe(self, archivo, filas_iniciales):
        try:
            with open(archivo, 'x', encoding='utf-8', newline='') as arch:
                escritor = csv.writer(arch)
                escritor.writerow(filas_iniciales)  # Escribir encabezados
                return 
        except FileExistsError:
            return
  
    def extraer_archivo(self, archivo_csv):
        telefonos = dict()
        try:
            with open(archivo_csv, mode='r', newline='') as archivo:
                lector_csv = csv.reader(archivo)
                next(lector_csv)  # Saltar encabezados
                for telefono in lector_csv:
                    telefonos[telefono[0]] = Telefono(telefono[0], telefono[1], telefono[2], telefono[3],
                                                       telefono[4], telefono[5], int(telefono[6]), telefono[7])
                  
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
        ram = input('Ingrese la RAM: ')
        almacenamiento = input('Ingrese el tamaño de almacenamiento: ')
        while not almacenamiento.isdigit():
            almacenamiento = input('Error en el ingreso del almacenamiento.\nIngrese el tamaño de almacenamiento:')
        telefono = Telefono(id, nombre, modelo, os, None, ram, int(almacenamiento), None)  # Asigna None o un valor a `numero`
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
    
    def actualizar_archivos(self):
        with open('telefonos.csv', 'w', encoding='utf-8', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(['ID', 'NOMBRE', 'MODELO', 'OS', 'VERSION', 'RAM', 'ALMACENAMIENTO', 'NUMERO'])  # Escribir encabezados
            for telefono in self.telefonos.values():
                escritor.writerow([telefono.id, telefono.nombre, telefono.modelo, telefono.os,
                                   telefono.version, telefono.ram, telefono.almacenamiento, telefono.numero])
    
    def menu_de_telefonos(self):
        match input('¿Qué quiere hacer con los teléfonos?\n1. Crear Teléfono\n2. Eliminar Teléfono\n3. Elegir qué teléfono usar\n4. Salir '):
            case '1':
                self.crear_telefono()
                self.menu_de_telefonos()  # Volver al menú
            case '2':
                self.eliminar_telefono()
                self.menu_de_telefonos()  # Volver al menú
            case '3':
                telefono = self.elegir_telefono()
                telefono.menu()  # Llamar al método de menú del teléfono elegido
                self.menu_de_telefonos()  # Volver al menú
            case '4':
                print('Salir')
                self.actualizar_archivos()
            case other:
                print('Esta opción no está disponible en este momento')
                self.menu_de_telefonos()


# Crear una instancia de FabricaDeTelefonos y llamar al menú
# mi_fabrica = FabricaDeTelefonos()  # Crear la instancia
# mi_fabrica.menu_de_telefonos()  # Llamar al método del menú
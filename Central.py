import csv
from TP_EDP import Telefono
from LLamadas import Llamadas


class Central():
    
    def __init__(self):
        self.telefonos=self.extraer_archivo('NOMBRE DEL ARCHIVO')
        self.registro_comunicaciones=()
        
    #Verificar si van todos los atributos del l
    
    def extraer_archivo(self, archivo_csv):
        telefonos=dict()
        try:
            with open(archivo_csv, mode='r', newline='') as archivo:
                lector_csv = csv.reader(archivo)
                next(lector_csv)
                for telefono in lector_csv:
                    telefonos[telefono[0]]=Telefono[telefono[0],telefono[1],telefono[2],telefono[3],
                                                    telefono[4],telefono[5],telefono[6],telefono[7]]
                
                    
            print("Todos los teléfonos han sido registrados desde el archivo CSV.")
            return telefonos
        except FileNotFoundError:
            print("El archivo CSV no fue encontrado.")
        except KeyError as e:
            print(f"Error en el archivo CSV. Faltan columnas: {e}")
        except Exception as e:
            print(f"Se produjo un error al leer el archivo CSV: {e}")

    def eliminar_dispositivo(self,telefono:Telefono):
        if telefono.id in self.telefonos:
            del self.telefonos[telefono.id]
            print (f"Se elimino el telefono con el id {telefono.id}")
        else:
            print (f"No se encuentra registrado el telefono con el numero {telefono.id}")
        
    def registrar_telefono(self, telefono:Telefono):
        if telefono.id not in self.telefonos: 
            self.telefonos[telefono.id]=telefono
            print (f"Se registro el telefono con el id {telefono.id}")
        else:
            print (f"Ya se encuentra registrado el telefono con el numero {telefono.id}")
    
    
    def verificar_disponibilidad_de_red(self, numero):
        if numero in self.telefonos:
            dispositivo = self.telefonos[numero]
            if dispositivo.encendido and dispositivo.red:
                print(f"El telefono con numero {numero} esta disponible.")
                return True
            else:
                print(f"El telefono con numero {numero} no esta disponible.")
                return False
        else:
            print(f"El telefono con numero {numero} no esta registrado.")
            return False
    
    def verificar_acceso_internet(self, numero):
        if numero in self.telefonos:
            dispositivo = self.telefonos[numero]
            if dispositivo.encendido and dispositivo.datos:
                print(f"El telefono con numero {numero} tiene acceso a internet.")
                return True
            else:
                print(f"El telefono con numero {numero} no tiene acceso a internet.")
                return False
        else:
            print(f"El telefono con numero {numero} no esta registrado.")
            return False

    def realizar_llamada(self, numero_origen, numero_destino):
        """Inicia la llamada verificando la disponibilidad de ambos teléfonos."""
        if numero_origen in self.telefonos and numero_destino in self.telefonos:
            telefono_origen = self.telefonos[numero_origen]
            telefono_destino = self.telefonos[numero_destino]
            
            # Verificar si ambos teléfonos están disponibles para la llamada
            if self.verificar_disponibilidad_de_red(numero_origen) and self.verificar_disponibilidad_de_red(numero_destino):
                if telefono_destino.ocupado:
                    print(f"No se puede realizar la llamada. El número {numero_destino} está ocupado.")
                else:
                    # Crear una instancia de Llamadas y gestionar el inicio y final de la llamada
                    llamada = Llamadas(telefono_origen, telefono_destino, peso=5000)  # Peso en bytes como ejemplo
                    llamada.onOff()  # Abrir la aplicación de llamadas
                    
                    if llamada.iniciar():
                        llamada.registrar(self)  # Registrar la llamada en la central
                        llamada.finalizar()      # Finalizar la llamada después de registrar
                    llamada.onOff()  # Cerrar la aplicación de llamadas
            else:
                print("Uno o ambos teléfonos no están disponibles para la llamada.")
        else:
            print(f"El teléfono con número {numero_destino} no está registrado en la central.")

    def registrar_comunicacion(self, tipo, numero_origen, numero_destino, contenido=None):
        log = {
            'tipo': tipo,
            'numero_origen': numero_origen,
            'numero_destino': numero_destino,
            'contenido': contenido
        }
        self.registro_comunicaciones.append(log)
        print(f"Comunicación registrada: {log}")





class Lista():
    def __init__(self):
        self.inicio = None
        
    def addStart (self,dato):
        if self.inicio == None:
            self.inicio = Nodo(dato)
    
class Nodo():
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

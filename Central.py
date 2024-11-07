import csv
from TP_EDP import Telefono

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

    def registrar_comunicacion(self, tipo, numero_origen, numero_destino, contenido=None):
        log = {
            'tipo': tipo,
            'numero_origen': numero_origen,
            'numero_destino': numero_destino,
            'contenido': contenido
        }
        self.registro_comunicaciones.append(log)
        print(f"Comunicacion registrada: {log}")

    def terminar_llamada(self, telefono_origen, telefono_destino):
        print(f"Llamada finalizada entre {telefono_origen.numero_telefonico} y {telefono_destino.numero_telefonico}.")
        telefono_origen.ocupado = False
        telefono_destino.ocupado = False

    def realizar_llamada(self, numero_origen, numero_destino):
        if numero_destino in self.telefonos:
            telefono_destino = self.telefonos[numero_destino]
            
            if telefono_destino.encendido and telefono_destino.red:
                if telefono_destino.ocupado:
                    print(f"No se puede realizar la llamada. El numero {numero_destino} esta ocupado.")
                else:
                    telefono_origen = self.telefonos[numero_origen]
                    telefono_origen.ocupado = True
                    telefono_destino.ocupado = True
                    
                    print(f"Estableciendo llamada de {numero_origen} a {numero_destino}...")

                    self.registrar_comunicacion("llamada", numero_origen, numero_destino)

                    self.terminar_llamada(telefono_origen, telefono_destino)
            else:
                print(f"El telefono con numero {numero_destino} no esta disponible.")
        else:
            print(f"El telefono con numero {numero_destino} no esta registrado.")





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

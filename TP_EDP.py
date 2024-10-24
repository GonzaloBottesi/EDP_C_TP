import csv 

# Hacer clase de fabrica de telefonos con un random
class Telefono():
    
    def __init__(self,id,nombre,modelo,os,version,ram,almacenamiento,numero) -> None:
        
        self.listaApps = dict()
        
        self.id = id
        self.nombre = nombre
        self.modelo = modelo
        self.os=os
        self.version=version
        self.ram=ram
        self.almacenamiento=almacenamiento
        self.numero=numero
        
        self.encendido = False
        self.bloqueado = True
        self.pin = None
        self.aplicacionActual = None ##Asignar el objeto Aplicacion para poder llamar a sus metodos
        self.red = False
        self.datos = False
        self.ocupado = False
        

        return None

        
        
    def powerButton(self):
        if self.bloqueado:    
            self.encendido = True
        else:
            print('Su celular ya esta prendido\n')
    
    def Apagar(self):
        if self.encendido:
            self.encendido = False
        else : print('Su celular esta apagado ')
    
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
    
    def mostrar_estado(self):
        red_estado = "activa" if self.red else "desactivada"
        datos_estado = "activados" if self.datos else "desactivados"
        print(f"Red movil: {red_estado}, Datos moviles: {datos_estado}")
    
    def menu(self, telefono : Telefono ):
        if isinstance(telefono, Telefono):
            # hacer un menu que elige que celular usar
            if telefono.bloqueado:
                match input('Quiere prender el celular?\n1. Si\n2. No'):
                    case '1':
                        self.powerButton()
                    case '2':
                        pass
            elif telefono.encendido:
                match input('Que quiere hacer con el celular?\n1. Desbloquear\n2. Apagar '):
                    case '1':
                        self.unlock()
                    case '2':
                        self.Apagar()
                        #apagar
                
                if telefono.encendido and not telefono.bloqueado:
                    #match


                    

    

# class FabricaDeTelefonos(): #ver que hacer con esto
#     def __init__(self,nombre):
#         self.telefonos=self.extraer_archivo()
#         pass
    
#     def crear_archivo(archivo, filas_iniciales  ):
#         try :
#             with open( archivo , 'x' , encoding='utf-8' , newline='' ) as arch :
#                 escritor = csv.writer(arch)
#                 for fila in filas_iniciales :
#                     escritor.writerow(fila)
#                 return 
#         except FileExistsError :
#             return
    
#     def extraer_archivo(self, archivo_csv):
#         telefonos=dict()
#         try:
#             with open(archivo_csv, mode='r', newline='') as archivo:
#                 lector_csv = csv.reader(archivo)
#                 next(lector_csv)
#                 for telefono in lector_csv:
#                     telefonos[telefono[0]]=[telefono[0],telefono[1],telefono[2],telefono[3],
#                                                     telefono[4],telefono[5],telefono[6],telefono[7]]
                    
#             print("Todos los teléfonos han sido registrados desde el archivo CSV.")
#             return telefonos
#         except FileNotFoundError:
#             print("El archivo CSV no fue encontrado.")
#         except KeyError as e:
#             print(f"Error en el archivo CSV. Faltan columnas: {e}")
#         except Exception as e:
#             print(f"Se produjo un error al leer el archivo CSV: {e}")

#     def agregar_telefono(self,telefono:Telefono):
#         if telefono.id not in self.telefonos:
#             pass




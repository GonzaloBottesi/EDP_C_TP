import csv

def crear_archivo_no_existe(archivo, filas_iniciales):
        try:
            with open(archivo, 'x', encoding='utf-8', newline='') as arch:
                escritor = csv.writer(arch)
                escritor.writerow(filas_iniciales)  # Escribir encabezados
                return 
        except FileExistsError:
            return
  
def extraer_archivo(archivo_csv):
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

def actualizar_archivos():
        with open('telefonos.csv', 'w', encoding='utf-8', newline='') as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(['ID', 'NOMBRE', 'MODELO', 'OS', 'VERSION', 'RAM', 'ALMACENAMIENTO', 'NUMERO'])  # Escribir encabezados
            for telefono in self.telefonos.values():
                escritor.writerow([telefono.id, telefono.nombre, telefono.modelo, telefono.os,
                                   telefono.version, telefono.ram, telefono.almacenamiento, telefono.numero])
from Aplicacion import Aplicacion


class Llamadas(Aplicacion):
    def __init__(self, telefono_origen, telefono_destino, peso):
        super().__init__(peso)
        self.telefono_origen = telefono_origen
        self.telefono_destino = telefono_destino
        self.en_curso = False

    def iniciar(self):
        if not self.abierto:
            print("La aplicación Llamadas no está abierta.")
            return False

        if not (self.telefono_origen.ocupado or self.telefono_destino.ocupado):
            self.telefono_origen.ocupado = True
            self.telefono_destino.ocupado = True
            self.en_curso = True
            print(f"Llamada iniciada entre {self.telefono_origen.numero} y {self.telefono_destino.numero}.")
            return True
        else:
            print("No se puede iniciar la llamada, uno de los teléfonos está ocupado.")
            return False

    def finalizar(self):
        if self.en_curso:
            self.telefono_origen.ocupado = False
            self.telefono_destino.ocupado = False
            self.en_curso = False
            print(f"Llamada finalizada entre {self.telefono_origen.numero} y {self.telefono_destino.numero}.")
            return True
        else:
            print("No hay una llamada en curso para finalizar.")
            return False

    def registrar(self, central):
        central.registrar_comunicacion(
            tipo="llamada",
            numero_origen=self.telefono_origen.numero,
            numero_destino=self.telefono_destino.numero
        )

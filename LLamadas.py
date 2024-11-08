from Aplicacion import Aplicacion

##Esta clase fue comentada para poder probar otra cosa. Sin embargo, no creo que tenga que tener ambos telefonos si hablamos de la aplicacion de llamadas
##En mi opinion, la aplicacion solo tiene que enviarle un paquete a la central y recibir un paquete de la central, toda la logistica de la llamada 
# se encarga la central (ver clase SMS para referencia)
##Ademas, si tuvieramos que importar el telefono entero volveriamos a un error de import ciclico asi que no se puede
##Toda la logistica de quien esta ocupado se tiene que encargar la central, ya que tiene la lista de telefonos conectados a la misma
## por eso, en caso de que un telefono este ocupado, le podria llegar al remitente un mensaje de la central indicandole que el destinatario esta ocupado
## Leer la parte de la comunicacion del TP. La dinamica es algo asi:

##              Tel1 solicita llamada con tel2 
#               central confirma que tel2 esta libre, si no esta le avisa a tel1
#               central le manda la llamada a tel2
#               tel2 recibe la llamada y le manda un paquete a la central con su respuesta [SI / NO]
#               la central le informa a tel1 de la respuesta de tel2 [Conecta la llamada / Termina]

## Cualquier cosa mandenme un mensaje al grupo y lo explico de vuelta, perdon por el testamento pero me parecio necesario

# class Llamadas(Aplicacion):
    
#     def __init__(self, telefono_origen, telefono_destino, peso):
#         super().__init__(peso)
#         self.telefono_origen = telefono_origen
#         self.telefono_destino = telefono_destino
#         self.en_curso = False

#     def iniciar(self):
#         if not self.abierto:
#             print("La aplicación Llamadas no está abierta.")
#             return False

#         if not (self.telefono_origen.ocupado or self.telefono_destino.ocupado):
#             self.telefono_origen.ocupado = True
#             self.telefono_destino.ocupado = True
#             self.en_curso = True
#             print(f"Llamada iniciada entre {self.telefono_origen.numero} y {self.telefono_destino.numero}.")
#             return True
#         else:
#             print("No se puede iniciar la llamada, uno de los teléfonos está ocupado.")
#             return False

#     def finalizar(self):
#         if self.en_curso:
#             self.telefono_origen.ocupado = False
#             self.telefono_destino.ocupado = False
#             self.en_curso = False
#             print(f"Llamada finalizada entre {self.telefono_origen.numero} y {self.telefono_destino.numero}.")
#             return True
#         else:
#             print("No hay una llamada en curso para finalizar.")
#             return False

#     def registrar(self, central):
#         central.registrar_comunicacion(
#             tipo="llamada",
#             numero_origen=self.telefono_origen.numero,
#             numero_destino=self.telefono_destino.numero
#         )


class Llamadas(Aplicacion):
    def __init__(self, peso) -> None:
        super().__init__(peso)
        
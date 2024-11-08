#pruebaaaaaaa a ver si funciona


# MAIN
from TP_EDP import *
from Central import *
from SMS import *
from funciones_auxiliares import *
from Aplicacion import *
from Appstore import *
from Config import *
from Contactos import *
from Mail import *
from SMS import *
from Stack import *
from lista_enlazada import *


central = Central()
lista_telefonos = []



def menu1():
    match input('¿Qué quiere hacer con el menu\n1. Ir a la central de Telefonos\n2. Ir a la fabrica de telefonos\n3. Salir\n '):
        case '1':
            menu_central_de_telefonos()
            # llamar a la central
        case '2':
            menu_fabrica_de_telefonos()
        case '3':
            print('Salir')
           


def menu_central_de_telefonos():
    pass


def menu_fabrica_de_telefonos():
    match input('¿Qué quiere hacer con los teléfonos?\n1. Crear Teléfono\n2. Eliminar Teléfono\n3. Elegir qué teléfono usar\n4. Salir '):
        case '1':
            FabricaDeTelefonos.crear_telefono()  # Volver al menú
            menu_fabrica_de_telefonos()
        case '2':
            FabricaDeTelefonos.eliminar_telefono() # Volver al menú
            menu_fabrica_de_telefonos()
        case '3':
            telefono = FabricaDeTelefonos.elegir_telefono()
            menu_telefono(telefono)  # Llamar al método de menú del teléfono elegido
             # Vte lleva al telefono
        case '4':
            print('Salir')
            menu1()
        case other:
            print('Esta opción no está disponible en este momento')
            menu_fabrica_de_telefonos()

def menu_telefono(telefono: Telefono): 
    telefono.powerButton() # Al entrar al menu se prende solo el celular
    
    if telefono.encendido and telefono.bloqueado: # Si el celular esta bloqueado
        match input('¿Qué quiere hacer con el celular?\n1. Desbloquear\n2. Apagar '):
            case '1':
                telefono.unlock()
                menu_telefono_prendido(telefono)
            case '2':
                telefono.Apagar()
                telefono.lock()
                menu_telefono()
            case other:
                print('Esta opción no está disponible')
                menu_fabrica_de_telefonos()
    else: print('ERROR')

def menu_telefono_prendido(telefono: Telefono):
    if telefono.encendido and not telefono.bloqueado: # Si el celular esta desbloqueado
    
        match input('''¿Qué aplicación quiere utilizar?\n1. Llamadas\n2. Contactos\n3. Mensaje de texto\n4. Mail\n5. App store\n6. Configuración\n7. Apagar'''):
            case '1':
                menu_llamadas()
                pass
            case '2':
                menu_contactos()
            case '3':
                menu_sms() 
                pass
            case '4':
                menu_mail()
            case '5':
                menu_appstore()
            case '6':
                menu_config(telefono)
            case '7':
                telefono.Apagar()
                telefono.lock()
                menu_fabrica_de_telefonos()
                
            case other:
                print('Esa opción no está disponible en este momento')
                telefono.menu()
    else:
        print('Algo funciona mal')
        


def menu_llamadas():
    pass

def menu_contactos():
    match input('¿Qué quiere hacer con la aplicacion Contactos?\n1. Agregar contactos\n2. Eliminar contactos\n3. Actualizar contactos\n4. Salir'): # pedirle el nombre y el celular en contacos NO ACA
            case '1':
                Contactos.addContact('name','number') # pedirselo en contactos, QUE NO TENGA ESTAS 2 COSAS COMO PARAMETROS
                menu_contactos()
            case '2':
                Contactos.deleteContact('name') # lo mismo de arriba
                menu_contactos()
            case '3':
                Contactos.updateContact('name','value') # preguntar lo que es
                menu_contactos()
            case '4':
                menu_telefono_prendido()
            case other:
                print('Esta opcion no esta dispoible')
                menu_contactos()
                
def menu_mail():
    match input('¿Qué quiere hacer con su Mail?\n1. Ver email por no leidos\n2. Ver email por orden de fecha\n3. Salir'):
        case '1':
            pass # FALTA
        case '2':
            pass # FALTA
def menu_sms():
    match input('Que quiere hacer con los SMS?\n1. Enviar mensaje de SMS\n2. Recibir(?)\n3. Ver bandeja de entrada\n4. Ver historial de llamadas\n.5 Eliminar mensajes\n6. Salir'):
            case '1':
                pass #COMPLETAR
            case '2':
                pass #COMPLETAR
def menu_appstore():
    match input('¿Qué quiere hacer con la AppStore?'):
        case '1':
            pass #COMPLETAR
        case '2':
            pass #COMPLETAR

def menu_config(telefono):
     match input('¿Qué quiere hacer con la configuracion?\n1. Cambiar nombre de telefono\n2. Cambiar codigo de desbloqueo\n3. Activar red movil\n4. Desactivar red movil\n5. Activar datos\n6. Desactivar datos\n7. Salir'):
            case '1':
                Config.setName(telefono)
                menu_config()
            case '2':
                Config.changePassword(telefono)
                menu_config()
            case '3':
                Config.red() # diferencia entre 3 y 4
                menu_config()
            case '4':
                Config.red()# diferenciar entre 3 y 4
                menu_config()
            case '5':
                Config.datos() # diferenciar entre 5 y 6
                menu_config()
            case '6':
                Config.datos() # diferenciar entre 5 y 6
                menu_config()
            case '7':
                menu_telefono_prendido()


#agregar en mail
'''def __init__(self, peso):
        super().__init__(peso)
        self.mails= [
    ["Informe Mensual", "2024-10-01", "No leído", 15],
    ["Actualización del Proyecto", "2024-10-05", "Leído", 7],
    ["Reunión de Seguimiento", "2024-10-10", "No leído", 12],
    ["Oferta Especial", "2024-10-12", "No leído", 3],
    ["Agenda de la Semana", "2024-10-15", "Leído", 20],
    ["Resumen Anual", "2024-10-18", "No leído", 10],
    ["Recordatorio de Pago", "2024-10-20", "No leído", 5],
    ["Invitación al Evento", "2024-10-22", "Leído", 18],
    ["Actualización de Seguridad", "2024-10-25", "No leído", 2],
    ["Nuevo Protocolo", "2024-10-28", "Leído", 9] # poner esto en la clase MAILS
    ]'''

lista_enlazada=ListaEnlazada()
for mail in mails:
    lista_enlazada.add_to_end(mail) # add_to_start o add_to_end
lista_enlazada_no_leidos=lista_enlazada()
    for mail in mails:
        if mail[2]=='Leido':
            lista_enlazada_no_leidos.add_to_start(mail)
        elif mail[3]=='No leido':
            lista_enlazada_no_leidos.add_to_end(mail) # ponerlo en mail

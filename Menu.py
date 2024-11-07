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

def menu_telefono_prendido(telefono):
    if telefono.encendido and not telefono.bloqueado: # Si el celular esta desbloqueado
    
        match input('''¿Qué aplicación quiere utilizar?\n1. Llamadas\n2. Contactos\n3. Mensaje de texto\n4. Mail\n5. App store\n6. Configuración\n7. Apagar'''):
            case '1':
                menu_llamadas()
                pass
            case '2':
                menu_contactos()
            case '3':
                #Sms.menu() todavia no creado
                pass
            case '4':
                menu_mail()
            case '5':
                menu_appstore()
            case '6':
                menu_config()
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
    match input('¿Qué quiere hacer con la aplicacion Contactos?'):
        case '1':
            pass #COMPLETAR
        case '2':
            pass #COMPLETAR
    
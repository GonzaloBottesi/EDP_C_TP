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

#crear_archivo_no_existe('telefonos.csv',['ID','NOMBRE','MODELO','OS','VERSION','RAM','ALMACENAMIENTO','NUMERO']) #crearlo las veces que sea neceario (es decir las veces que se usan archivos)

central = Central()
lista_telefonos = dict()
fabrica_de_telefonos = FabricaDeTelefonos()

# no se si falta alguna ams


def menu1():
    match input('¿Qué quiere hacer con el menu\n1. Ir a la central de Telefonos\n2. Ir a la fabrica de telefonos\n3. Salir\n '):
        case '1':
            menu_central_de_telefonos()
            
        case '2':
            menu_fabrica_de_telefonos()
        case '3':
            print('Salir')
           


def menu_central_de_telefonos():
    
    match input('¿Qué quiere hacer en la Central?\n1. Registrar un telefono\n2. Dar de baja un telefono\n3. Salir\n '):
        case '1':
            mostrar_lista_telefonos(lista_telefonos)
            id = input('Seleccione el telefono a registrar introduciendo el numero de la lista: ')
            central.registrar_telefono(lista_telefonos[id])
            menu_central_de_telefonos()
        case '2':
            mostrar_lista_telefonos(lista_telefonos)
            id = input('Seleccione el telefono a registrar introduciendo el numero de la lista: ')
            central.eliminar_dispositivo(lista_telefonos[id])
            menu_central_de_telefonos()
        case '3':
            menu1()


def menu_fabrica_de_telefonos():
    salir = False
    while not salir:
        match input('¿Qué quiere hacer con los teléfonos?\n1. Crear Teléfono\n2. Eliminar Teléfono\n3. Elegir qué teléfono usar\n4. Salir '):
            case '1':
                newPhoneEntry = fabrica_de_telefonos.crear_telefono()  # Volver al menú
                lista_telefonos.update(newPhoneEntry)
                #menu_fabrica_de_telefonos()
            case '2':
                id = fabrica_de_telefonos.eliminar_telefono() # Volver al menú
                if id is not False:
                    lista_telefonos.pop(id)
                #menu_fabrica_de_telefonos()
            case '3':
                telefono = fabrica_de_telefonos.elegir_telefono()
                if isinstance(telefono, Telefono):
                    lista_telefonos.update({telefono.id : telefono})
                    telefono.powerButton() # Al entrar al menu se prende solo el celular
                    print('Telefono encendido')
                    menu_telefono(telefono)  # Llamar al método de menú del teléfono elegido # Vte lleva al telefono
                else:
                    pass
                   # menu_fabrica_de_telefonos()
            case '4':
                salir = True
                print('Salir')
                fabrica_de_telefonos.actualizar_archivos()
                #menu1()
            case other:
                print('Esta opción no está disponible en este momento')
                #menu_fabrica_de_telefonos()

    menu1()


def menu_telefono(telefono: Telefono): 
    
    if telefono.encendido and telefono.bloqueado: # Si el celular esta bloqueado
        match input('¿Qué quiere hacer con el celular?\n1. Desbloquear\n2. Apagar '):
            case '1':
                password = input('Ingrese la contraseña: ')
                if telefono.unlock(password):
                    menu_telefono_prendido(telefono)
                else:
                    menu_telefono(telefono)
            case '2':
                telefono.Apagar()
                telefono.lock()
                menu_fabrica_de_telefonos()
            case other:
                print('Esta opción no está disponible')
                menu_telefono(telefono)
    else: print('ERROR')

def menu_telefono_prendido(telefono: Telefono):
    if telefono.encendido and not telefono.bloqueado: # Si el celular esta desbloqueado
    
        match input('''¿Qué quiere hacer?\n1. Abrir una aplicacion\n2. Apagar\n'''):
            case '1':               
                telefono.openApp()
                
                if isinstance(telefono.aplicacionActual, AppStore):
                    menu_appstore(telefono)
                    
                elif isinstance(telefono.aplicacionActual, Config):
                    menu_config(telefono)
                    
                elif isinstance(telefono.aplicacionActual, Contactos):
                    menu_contactos(telefono)
                    
                elif isinstance(telefono.aplicacionActual, Llamadas):
                    pass ##Completar dpes de hacer clase llamadas
                
                elif isinstance(telefono.aplicacionActual, Mail):
                    menu_mail(telefono)
                    
                elif isinstance(telefono.aplicacionActual, SMS):
                    menu_sms(telefono)
                
                
                pass
            case '2':
                telefono.Apagar()
                telefono.lock()
                menu_fabrica_de_telefonos()
                
            case other:
                print('Esa opción no está disponible en este momento')
                menu_telefono_prendido(telefono)
    else:
        print('Algo funciona mal')
        


def menu_llamadas():
    pass

def menu_contactos(telefono: Telefono):
    match input('¿Qué quiere hacer con la aplicacion Contactos?\n1. Agregar contactos\n2. Eliminar contactos\n3. Actualizar contactos\n4. Salir'): # pedirle el nombre y el celular en contacos NO ACA
            case '1': ## Mover los inputs a los metodos
                telefono.aplicacionActual.addContact('name','number') # pedirselo en contactos, QUE NO TENGA ESTAS 2 COSAS COMO PARAMETROS

            case '2':
                telefono.aplicacionActual.deleteContact('name') # lo mismo de arriba

            case '3':
                telefono.aplicacionActual.updateContact('name','value') # preguntar lo que es

            case '4':
                menu_telefono_prendido(telefono)
            case other:
                print('Esta opcion no esta dispoible')

    
    menu_contactos(telefono)
            
def menu_mail(telefono: Telefono):
    match input('¿Qué quiere hacer con su Mail?\n1. Ver email por no leidos\n2. Ver email por orden de fecha\n3. Salir'):
        case '1':
            telefono.aplicacionActual.ver_mail_por_no_leidos()
            menu_mail(telefono)
        case '2':
            telefono.aplicacionActual.ver_mail_por_fecha()
            menu_mail(telefono)
        case '3':
            menu_telefono(telefono)
    
    
def menu_sms(telefono : Telefono):
    match input('Que quiere hacer con los SMS?\n1. Enviar mensaje de SMS\n2. Recibir(?)\n3. Ver bandeja de entrada\n4. Ver historial de llamadas\n.5 Eliminar mensajes\n6. Salir'):
            case '1':
                
                menu_sms(telefono)
                pass #COMPLETAR
            case '2':
                
                menu_sms(telefono)
                pass #COMPLETAR
    
def menu_appstore(telefono: Telefono):
    match input('¿Qué quiere hacer con la AppStore?'):
        case '1':
            
            menu_appstore(telefono)
            pass #COMPLETAR
        case '2':
            
            menu_appstore(telefono)
            pass #COMPLETAR


def menu_config(telefono: Telefono):
    salir = False
    while not salir:
        if isinstance(telefono.aplicacionActual, Config):
            match input('¿Qué quiere hacer con la configuracion?\n1. Cambiar nombre de telefono\n2. Cambiar codigo de desbloqueo\n3. Activar red movil\n4. Desactivar red movil\n5. Activar datos\n6. Desactivar datos\n7. Salir'):
                    case '1':
                        telefono.aplicacionActual.setName(telefono.configParameters)
                        #menu_config(telefono)

                    case '2':
                        telefono.aplicacionActual.changePassword(telefono.configParameters)
                        #menu_config(telefono)

                    case '3':
                        telefono.aplicacionActual.red(telefono.configParameters) # diferencia entre 3 y 4
                        #menu_config(telefono)

                    case '4':
                        telefono.aplicacionActual.red(telefono.configParameters)# diferenciar entre 3 y 4
                        #menu_config(telefono)

                    case '5':
                        telefono.aplicacionActual.datos(telefono.configParameters) # diferenciar entre 5 y 6
                        #menu_config(telefono)

                    case '6':
                        telefono.aplicacionActual.datos(telefono.configParameters) # diferenciar entre 5 y 6
                        #menu_config(telefono)
                    case '7':
                        #menu_telefono_prendido(telefono)
                        
                    case other:
                        pass
        else:
            salir = True
            
    menu_telefono_prendido(telefono)

def mostrar_lista_telefonos(telefonos : dict):
    
    print('Los telefonos en el programa son:')
    for key in telefonos.keys():
        print(f'{key} : {telefonos[key]}')

menu1()
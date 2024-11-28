#pruebaaaaaaa a ver si funciona
# MAIN
import datetime
from TP_EDP import *
from Central import Central
##from funciones_auxiliares import *
from Aplicacion import Aplicacion
from Appstore import AppStore
from Config import Config
from Contactos import Contactos
from Mail import Mail
from SMS import SMS
from DataAnalysis import DataAnalysis
#crear_archivo_no_existe('telefonos.csv',['ID','NOMBRE','MODELO','OS','VERSION','RAM','ALMACENAMIENTO','NUMERO']) #crearlo las veces que sea neceario (es decir las veces que se usan archivos)

central = Central()
lista_telefonos = dict()
fabrica_de_telefonos = FabricaDeTelefonos()
# no se si falta alguna ams


def menu1():
    salir = False
    while not salir:
        match input('¿Qué quiere hacer con el menu\n1. Ir a la central de Telefonos\n2. Ir a la fabrica de telefonos\n3. Ver el analisis de Play Store Data\n4. Salir\n '):
            case '1':
                phoneCentralMenu()
                
            case '2':
                phoneFactoryMenu()
            case '3':
                dataAnalysisMenu()
            case '4':
                salir = True
                print('Salir')
            case other:
                print('Error, por favor ingrese una opcion valida \n')

def dataAnalysisMenu():
    analysis = DataAnalysis()
    salir = False
    while not salir:
        print('Se analizaron los datos de Play Store Data.csv y se obtuvieron los siguientes resultados:\n\n1.Las categorias con mayor porcentaje de las apps pagas\n2.El precio mas recurrente en las apps pagas\n3.Las descargas por categoria con su top 5')
        match input('Ingrese el resultado que desea ver (pulse enter para salir): '):
            case '1':
                analysis.paidPieChart()
            case '2':
                analysis.paidMedian()
            case '3':
                analysis.installsPerCategory()
            case '':
                salir = True
            case other:
                print('No se admine ese ingreso')
                


def phoneCentralMenu():
    salir = False
    while not salir:
        match input('¿Qué quiere hacer en la Central?\n1. Registrar un telefono\n2. Dar de baja un telefono\n3. Salir\n '):
            case '1':
                showPhoneList(fabrica_de_telefonos.telefonos)
                key = input('Seleccione el telefono a registrar introduciendo el numero de la lista: ')
                while key not in fabrica_de_telefonos.telefonos:
                    key = input('Por favor, ingrese un numero valido: ')
                central.registerDevice(fabrica_de_telefonos.telefonos[key])
            case '2':
                showPhoneList(fabrica_de_telefonos.telefonos)
                key = input('Seleccione el telefono a registrar introduciendo el numero de la lista: ')
                while key not in fabrica_de_telefonos.telefonos:
                    key = input('Por favor, ingrese un numero valido: ')
                central.eraseDevice(fabrica_de_telefonos.telefonos[key])
            case '3':
                salir = True
            case other:
                print('Error, por favor ingrese una opcion valida \n')
    #menu1()

def phoneFactoryMenu():
    salir = False
    while not salir:
        match input('¿Qué quiere hacer con los teléfonos?\n1. Crear Teléfono\n2. Eliminar Teléfono\n3. Elegir qué teléfono usar\n4. Salir '):
            case '1':
                newPhoneEntry = fabrica_de_telefonos.createPhone()  # Volver al menú
                lista_telefonos.update(newPhoneEntry)
                #phoneFactoryMenu()
            case '2':
                key = fabrica_de_telefonos.erasePhone() # Volver al menú
                if key is not False:
                    lista_telefonos.pop(key)
                #phoneFactoryMenu()
            case '3':
                telefono = fabrica_de_telefonos.choosePhone()
                if isinstance(telefono, Telefono):
                    lista_telefonos.update({telefono.id : telefono})
                    telefono.powerButton() # Al entrar al menu se prende solo el celular
                    print('Telefono encendido')
                    phoneMenu(telefono)  # Llamar al método de menú del teléfono elegido # Vte lleva al telefono
                else:
                    pass
                   # phoneFactoryMenu()
            case '4':
                salir = True
                print('Salir')
                fabrica_de_telefonos.updateFiles()
                #menu1()
            case other:
                print('Esta opción no está disponible en este momento')
                #phoneFactoryMenu()

    #menu1()

def phoneMenu(telefono: Telefono): 
    salir = False
    if telefono.encendido and telefono.bloqueado: # Si el celular esta bloqueado
        while not salir:
            match input('¿Qué quiere hacer con el celular?\n1. Desbloquear\n2. Apagar '):
                case '1':
                    password = input('Ingrese la contraseña: ')
                    if telefono.unlock(password):
                        poweredPhoneMenu(telefono)
                    else:
                        pass
                        #phoneMenu(telefono)
                case '2':
                    salir = True
                    telefono.Apagar()
                    telefono.lock()
                case other:
                    print('Esta opción no está disponible')
                    #phoneMenu(telefono)
        #phoneFactoryMenu()
    else:
        print('ERROR')

def poweredPhoneMenu(telefono: Telefono):
    if telefono.encendido and not telefono.bloqueado: # Si el celular esta desbloqueado
        salir = False
        while not salir:
            match input('''¿Qué quiere hacer?\n1. Abrir una aplicacion\n2. Apagar\n'''):
                case '1':               
                    telefono.openApp()
                    
                    if isinstance(telefono.aplicacionActual, AppStore):
                        appstoreMenu(telefono)
                        
                    elif isinstance(telefono.aplicacionActual, Config):
                        configMenu(telefono)
                        
                    elif isinstance(telefono.aplicacionActual, Contactos):
                        contactsMenu(telefono)
                        
                    elif isinstance(telefono.aplicacionActual, Llamadas):
                        callMenu(telefono) ##Completar dpes de hacer clase llamadas
                    
                    elif isinstance(telefono.aplicacionActual, Mail):
                        mailsMenu(telefono)
                        
                    elif isinstance(telefono.aplicacionActual, SMS):
                        SMSMenu(telefono)
                    else:
                        print('Lo siento, de momento la aplicacion esta en desarrollo y no se puede abrir')
                case '2':
                    telefono.Apagar()
                    telefono.lock()
                    salir = True
                    #phoneFactoryMenu()
                    
                case other:
                    print('Esa opción no está disponible en este momento')
                    #poweredPhoneMenu(telefono)
    else:
        print('Algo funciona mal')


def callMenu(telefono : Telefono):
    paquete_ejemplo = ['LLAMADA', '1123456789', telefono.numero, datetime.datetime.now().replace(microsecond = 0).strftime("%d/%m/%Y, %H:%M:%S") , 'R']
    salir = False
    while not salir:
        match input('''¿Qué quiere hacer en Llamadas?\n1. Llamar\n2. Atender llamada\n3. Cortar llamada\n4. Ver historial de llamadas\n5.Volver\n'''):
            case '1':
                paquete_llamada = telefono.aplicacionActual.sendCallRequest(telefono.numero)
                print(paquete_llamada)
            case '2':
                paquete_recepcion = telefono.aplicacionActual.receivePacket(paquete_ejemplo) #Pensar en un paquete de ejemplo
                print(paquete_recepcion)
            case '3':
                paquete_cortar = telefono.aplicacionActual.endCallRequest(telefono.numero) ##Ingresar el numero de ejemplo
                print(paquete_cortar)
            case '4':
                telefono.aplicacionActual.getCallHistory()
            case '5':
                salir = True
            case other:
                print('Error, por favor ingrese una opcion valida \n')
    #poweredPhoneMenu(telefono)

def contactsMenu(telefono: Telefono):
    salir = False
    while not salir:
        match input('''¿Qué quiere hacer en Contactos?\n1. Agregar contacto\n2. Actualizar contecto\n3. Eliminar contacto\n4.Volver\n'''):
            case '1':
                number = input('Ingrese el numero de telefono: ')
                while not number.isnumeric():
                    number = input('Error, ingrese un numero de telefono valido: ')
                name = input('Ingrese el nombre')
                telefono.aplicacionActual.addContact(name,number)
            case '2':
                name = input('Ingrese el nombre del contacto a actualizar')
                number = input('Ingrese el nuevo numero de telefono: ')
                while not number.isnumeric():
                    number = input('Error, ingrese un numero de telefono valido: ')
                telefono.aplicacionActual.updateContact(name,number)
            case '3':
                name = input('Ingrese el nombre del contacto: ')
                telefono.aplicacionActual.deleteContact(name)
            case '4':
                salir = True
            case other:
                print('Error, por favor ingrese una opcion valida \n')
    #poweredPhoneMenu(telefono)
            
def mailsMenu(telefono: Telefono):
    salir = False
    while not salir:
        match input('¿Qué quiere hacer con su Mail?\n1. Ver email por no leidos\n2. Ver email por orden de fecha\n3. Salir\n'):
            case '1':
                telefono.aplicacionActual.sortMailByUnread()
                #mailsMenu(telefono)
            case '2':
                telefono.aplicacionActual.sortMailByDate()
                #mailsMenu(telefono)
            case '3':
                salir = True
                #phoneMenu(telefono)
            case other:
                print('Error, por favor ingrese una opcion valida \n')
    
def SMSMenu(telefono : Telefono):
    mensaje_ejemplo = ['SMS', '1123456789' , telefono.numero, datetime.datetime.now().replace(microsecond = 0).strftime("%d/%m/%Y, %H:%M:%S") , 'Mensaje de ejemplo']
    salir = False
    while not salir:
        match input('Que quiere hacer con los SMS?\n1. Enviar mensaje de SMS\n2. Recibir un mensaje (de ejemplo)\n3. Ver bandeja de entrada\n.4 Eliminar mensajes\n5. Volver\n'):
            case '1':
                telefono.aplicacionActual.sendMessage(telefono.numero)
            case '2':
                telefono.aplicacionActual.receiveMessage(mensaje_ejemplo)
            case '3':
                telefono.aplicacionActual.viewMessage()
            case '4':
                telefono.aplicacionActual.eraseMessage()
            case '5':
                salir = True
            case other:
                print('Error, por favor ingrese una opcion valida \n')
    #poweredPhoneMenu(telefono)
    
def appstoreMenu(telefono: Telefono):
    salir = False
    while not salir:
        match input('¿Qué quiere hacer con la AppStore?\n1. Instalar una app\n2. Desinstalar una App\n3. Volver\n'):
            case '1':
                name = input('Ingrese el nombre de la aplicacion (buscar nombres en la appstore)')
                telefono.aplicacionActual.installApp(telefono.configParameters,telefono.listaApps, name)
            case '2':
                nameList = telefono.listaApps.keys()
                print('Aplicaciones instaladas: \n')
                i = 1
                for app in nameList:
                    print(f'{i}. {app}')
                    i += 1
                name = input('Ingrese el nombre tal cual como aparece')
                telefono.aplicacionActual.uninstallApp(telefono.configParameters,telefono.listaApps,name)
            case '3':
                salir = True
            case other:
                print('Error, por favor ingrese una opcion valida \n')
    #poweredPhoneMenu(telefono)
    
def configMenu(telefono: Telefono):
    salir = False
    while not salir:
        if isinstance(telefono.aplicacionActual, Config):
            match input('¿Qué quiere hacer con la configuracion?\n1. Cambiar nombre de telefono\n2. Cambiar codigo de desbloqueo\n3. Activar/Desactivar red\n4. Activar/Desactivar datos\n5. Salir\n'):
                case '1':
                    telefono.aplicacionActual.setName(telefono.configParameters)
                    #configMenu(telefono)

                case '2':
                    telefono.aplicacionActual.changePassword(telefono.configParameters)
                    #configMenu(telefono)

                case '3':
                    telefono.aplicacionActual.red(telefono.configParameters)
                    if telefono.configParameters.red:
                        print('Se activo la red')
                    else:
                        print('Se desactivo la red')
                    #configMenu(telefono)

                case '4':
                    telefono.aplicacionActual.datos(telefono.configParameters)
                    if telefono.configParameters.datos:
                        print('Se activaron los datos')
                    else:
                        print('Se desactivaron los datos')
                    #configMenu(telefono)

                case '5':
                    salir = True
                    #poweredPhoneMenu(telefono)
                    
                case other:
                    print('Error, por favor ingrese una opcion valida \n')
        else:
            salir = True
    #poweredPhoneMenu(telefono)

def showPhoneList(telefonos : dict):
    
    print('Los telefonos en el programa son:')
    for key in telefonos.keys():
        print(f'{key} : {telefonos[key]}')

menu1()

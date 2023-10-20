# Consignas:
# Funcion de registro de usuarios
# Funcion de login
# Una funcino para mostrar los datos por consola

usuarios = {'default':'12345'}

##funcion para el registro
def registrarse():
    print('Registro de usuario: Ingresar usuario y contrasenia (entre 5 y 10 caracteres)')
    obtener_datos()
    print('Registrado correctamente!')

def obtener_datos():
    # obteniendo el user
    user = 'default'            #
    while usuarios.get(user):
        user = input('Ingresar usuario:')
        if usuarios.get(user):
              print('Usuario ya registrado')
        elif ' ' in user:
            print ('No puede contener espacios')
            user = 'default'
        elif len(user) <= 4:
            print ('El usuario debe tener mas de 4 caracteres')
            user = 'default'
        elif len(user) > 10:
            print ('El usuario debe tener hasta 10 caracteres')
        else:
            print('Usuario valido')

    # obteniendo la password
    condicion = False
    while condicion == False:
        passw = (input('Ingresar constrasena: '))
        if ' ' in passw:
            print ('No puede contener espacios')
        elif len(passw) <= 4:
            print ('La contrasena debe tener mas de 4 caracteres')
        elif len(passw) > 10:
            print ('Entre 5 y 10 caracteres')
        else:
            condicion = True

    #update del diccionario
    usuarios.update({user:passw})
    return None


## Función para loguearse
def loguearse():
    print('Ingresar tus datos: ')
    user = input('Ingresar usuario: ')
    if user in usuarios:
        passw = input('Ingresar contraseña: ')
        if usuarios.get(user) == passw:
            print('Logueado correctamente!')
            return user
        else:
            print('Contraseña incorrecta')
    else:
        print('Usuario no registrado')
    return None

#Funcion para mostrar datos
def status(status_user):
    if status_user == None:
        print('No registrado')
    else:
        print('Logueado como {}'.format(status_user))

# Funcion para mostrar usuarios
def mostrar_usuarios():
    print('Usuarios registrados: ')
    for user in usuarios:
        print(user, ' ')
    return None

#Algoritmo principal
status_user = None
menu = 0
print('Bienvenido al loguin!')
print('Opciones:')
while menu != 5:
    menu = int(input("1. Registrarse\n2. Loguearse\n3. Status\n4. Ver usuarios\n 5. Salir\n->"))
    if menu == 1:
        registrarse()
    elif menu == 2:
        status_user = loguearse()
    elif menu == 3:
        status(status_user)
    elif menu == 4:
        mostrar_usuarios()
    elif menu == 5:
        print('Hasta luego!')
    else:
        print('Opcion no valida')

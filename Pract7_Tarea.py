#Juan Jose Navarrete garibay       18420470

import json

import bcrypt

arch_Est=open("Estudiantes.prn")
lista=arch_Est.readlines()

def Estudiantes (lista):
    conj = set()
    for linea in lista:
        Control = linea[0:8]
        Nombre = linea[8:-1]
        # tupla= (Control,Nombre)
        conj.add((Control, Nombre))
    return  conj

#print(Estudiantes(lista))



#2. Crear un método que regrese un conjunto de tuplas de materias.

arch_kardex=open("Kardex.txt")
listak=arch_kardex.readlines()
# print(listak)

def Materia (lista):
    conj2 = set()
    for linea in lista:
        separado=linea.split('|')
        #print(len(separado[2]))
        num=str(separado[2][0:-1])
        conj2.add((separado[0], separado[1],num))
    return conj2



'''
6. Crear un método "autenticar_usuario(usuario,contrasena)" que regrese una bandera que 
   indica si se pudo AUTENTICAR, el nombre del estudiante y un mensaje, regresar el JSON:
   {
        "Bandera": True,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Bienvenido al Sistema de Autenticación de usuarios"
   }

   ó

   {
        "Bandera": False,
        "Usuario": "",
        "Mensaje": "No existe el Usuario"
   }

   ó

    {
        "Bandera": False,
        "Usuario": "Leonardo Martínez González",
        "Mensaje": "Contraseña incorrecta"
   }


'''
arch_Usuario=open('usuarios.txt')
listaUs=arch_Usuario.readlines()


def Nombre(num_ctrol):
    arch=open("Estudiantes.prn")
    lineas = arch.readlines()
    for linea in lineas:
        if num_ctrol == linea[:8]:
            nom=linea[8:-1]
    return nom


def Autentificar():
    usuario = input("Ingrese  el usuario: ")
    contrasenia = input("Ingrese la contraseña: ")
    Band=bool
    nombre=""
    msj=""
    dicc={}
    for linea in listaUs:
        if usuario in linea:
            lista= linea.split(' ')
            sn_salto=lista[2].strip('\n')
            if bcrypt.checkpw(contrasenia.encode('utf-8'), sn_salto.encode('utf-8')):
                Band = True
                msj = "Bienvenido al Sistema de Autenticacion de usuarios"
                nombre = Nombre(usuario)
            else:
                msj = "la contraseña es incorrecta"
                Band = False
                nombre = Nombre(usuario)
            break
        else:
            Band = False
            msj = "No exite usuario"
    dicc["Bandera"]=Band
    dicc["Nombre"]=nombre
    dicc["Mensaja"]=msj
    return print(json.dumps(dicc, indent=4))


Autentificar()


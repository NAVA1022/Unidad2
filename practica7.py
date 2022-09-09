'''
Tema: Aplicación de estructuras de Python: archivos, JSON, cifrado de contraseñas
Fecha: 06 de septiembre del 2022
Autor: Leonardo Martínez González
Continuación de la práctica 6
'''


'''
Crear un programa que utilice los archivos Estudiantes.prn y kardex.txt:

1. Crear un método que regrese un conjunto de tuplas de estudiantes.
'''

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

#print(Materia(listak))
'''
3. Crear un método que dado un número de control regrese el siguiente formato JSON:
   {
        "Nombre": "Manzo Avalos Diego",
        "Materias":[
            {
                "Nombre":"Base de Datos",
                "Promedio":85
            },
            {
                "Nombre":"Inteligencia Artificial",
                "Promedio":100
            },
            . . . 
        ],
        "Promedio general": 98.4
   }
'''

import json
import random
import bcrypt


def Cons_NC(NC,conjalum,conjmat):
    diccG = {}
    listaM = []
    dicc_materias = {}
    prom_general = 0
    calum = conjalum
    cmat = conjmat

    for alum in calum:

        if NC in alum:
            diccG['Nombre'] = alum[1]

            for mate in cmat:
                if NC in mate:
                    dicc_materias['Nombre'] = mate[1]
                    dicc_materias['Promedio'] = int(mate[2])
                    prom_general += int(mate[2])
                    listaM.append(dicc_materias)
                    dicc_materias = {}
            diccG['Materias'] = listaM
            diccG['Promedio General'] = prom_general / len(listaM)
    return diccG



#NC = input("Dame el numero de Control")
#print(Cons_NC(NC,Estudiantes(lista),Materia(listak)))

'''


4. Regresar una lista de JSON con las materias de un estudiante, el formato es el siguiente:
[
    {"Nombre": "Contabilidad Financiera"},
    {"Nombre": "Dise\u00f1o UX y UI"}, 
    {"Nombre": "Base de datos distribuidas"}, 
    {"Nombre": "Finanzas internacionales IV"}, 
    {"Nombre": "Analisis y dise\u00f1o de sistemas de informacion"}, 
    {"Nombre": "Microservicios"},
    {"Nombre": "Algoritmos inteligentes"}
]
'''

def regresa_materia_por_estudiante(crot):
    promedio=Materia(listak)
    lista_maeterias=[]
    for mat in promedio:
        c,m,p=mat #Destructurar la variable mat
        if crot==c:
            lista_maeterias.append({"Nombre":m})
    return  json.dumps(lista_maeterias)
#print(regresa_materia_por_estudiante("18420465"))

'''

5. Generar un archivo de usuarios que contenga el numero de control, éste será el usuario
   y se generará una contraseña de tamaño 10 la cual debe tener:
   A. Al menos una letra mayúscula 
   B. Al menos una letra minúscula
   C. Numeros
   D. Al menos UN carácter especial, considere ( @, #, $,%,&,_,?,! )

   Considere:
    - Crear un método para generar cada caracter
    - El codigo ascii: https://elcodigoascii.com.ar/
    - Encriptar la contraseña con bcrypt, se utiliza con node.js, react, etc. Para ello:
        * Descargue la libreria bcrypt con el comando: "pip install bcrypt" desde la terminal o desde PyCharm
        * Página: https://pypi.org/project/bcrypt/
        * Video:Como Cifrar Contraseñas en Python     https://www.youtube.com/watch?v=9tEovDYSPK4

   El formato del archivo usuarios.txt será:
   control contrasena contraseña_cifrada
'''

def gen_mayuscula():
    return chr(random.randint(65,90))

def gen_minuscula():
    return chr(random.randint(97, 122))

def gen_numeros():
    return chr(random.randint(48,57))

def gen_Caracter():
    list_caracteres=['@', '#', '$','%','&','_','?','!']
    return list_caracteres[random.randint(0,7)]

def gen_contra():
    clave = ""
    for i in range(0,10):
        numero=random.randint(1,5)

        if numero==1:
            clave+=gen_mayuscula()
        elif numero==2:
            clave+=gen_minuscula()
        elif numero==3:
            clave+=gen_Caracter()
        elif numero>=4 or numero<=5:
            clave+=str(gen_numeros())

    return clave


# print(gen_contra())

def cifrar_contra(contra):
    sal = bcrypt.gensalt()
    contra_cifrada=bcrypt.hashpw(contra.encode('utf-8'),sal)
    return contra_cifrada

# clave=gen_contra()
# print(clave,cifrar_contra(clave))

def gen_arch_users():
    estudiastes=Estudiantes(lista)
    usuarios=open("usuarios.txt","w")
    cont=0
    for est in estudiastes:
        c,n =est
        clave=gen_contra()
        cv_cifrada=cifrar_contra(clave)
        registro=c+" "+clave+" "+str(cv_cifrada,'utf-8')+" \n"
        usuarios.write(registro)
        cont+=1
        print(cont)
    print("Archivo generado")

print(gen_arch_users())

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

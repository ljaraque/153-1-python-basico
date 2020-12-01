# programa principal

print("hola mundo actual")

# variables
nombre_del_curso = "Full Stack Python" # strings
numero_de_alumnos = 20 # entero
temperatura = 36.5 # flotante 
nombres = ["John", "Sarah", "Neo", 
            "Trinity", "Yoda", "Luke", 
            "Morfeo", "Wallie", "R2D2", "C3PO"]

# todas estas variables pueden ser utilizadas o "vistas" desde
# esta parte del código pues son globales definidas en programa principal
print(nombre_del_curso)
print(numero_de_alumnos)
print(temperatura)
print(nombres)


# funcion básica en python

def saludo(nombre, edad):
    mensaje = "Hola " + nombre + " tienes " + edad + " años!"
    fecha = "10 de Diciembre"
    return mensaje

mensaje_retornado_por_la_funcion = saludo("Luis", "67")
print(mensaje_retornado_por_la_funcion)

# los siguiente print() producen error pues
# las variables que se solicita imprimir no
# están presentes pues no son de alcance (scope) global
#print(mensaje)
#print(fecha)

# las variables que están dentro de una función pueden ser vistas
# desde el exterior si son explicitamente declaradas como globales
def suma(a,b):
    global edad
    edad = 100
    edad2 = 50
    return a+b

print(  suma(1, 5)  )
print(edad)
# el siguiente print produce error pues edad2 no es global
#print(edad2)

# TIPOS DE DATOS

# numeros
#enteros
numero_entero = 400

#flotantes
numero_flotante = 3.5

#binario
numero_binario = 0b11111111 # OJO: Esto es un byte!!!!!
print(bin(numero_binario))


#complejo
numero_complejo = 4 + 5j
print(numero_complejo)


# operadores numéricos
print(numero_entero * numero_complejo)
print(numero_flotante + numero_entero)
print(numero_complejo / numero_flotante)
print(numero_flotante **8)


# strings

nombre_apellido = "Matías Bravu"
cargo = "Gerente de Desarrollo"
espacio = " "
# operacion de strings
print(nombre_apellido + espacio + cargo)
print(nombre_apellido + " " + cargo + " Es muy estricto")
print(10 * nombre_apellido)


# funciones incluidas en python para strings
largo_nombre_apellido = len(nombre_apellido)
print("El largo de nombre_apellido es: ", largo_nombre_apellido)

# tuplas
amigo = ("Rocío Pérez", "Adulta", 45) # secuencia INMUTABLE de objetos
print(amigo)

print(amigo[2])
# esto produce error pues tuplas son INMUTABLES
#amigo[2] = 30

# pasar tupla a lista
amigo_en_formato_lista = list(amigo)
print("Tupla pasada a lista: ", amigo_en_formato_lista)


# listas
amigo2 = ["Francisco", "Paredes", 60]
print(amigo2)
print(amigo2[2])
amigo2[2]=30 # la lista si puedo cambiar sus elementos pues es MUTABLE
print(amigo2[2])

lista_de_objetos = [1,2,"hola", amigo2, amigo, suma, saludo]

print("Las cosas que hay en mi lista de objetos:")
for objeto in lista_de_objetos:
    print(object, type(objeto))


# diccionarios

diccionario_ejemplo= {'a': 1, 'b': 2, 'c': 3}

print(diccionario_ejemplo)
print(diccionario_ejemplo['a'])
print(diccionario_ejemplo['c'])

diccionario_ejemplo['a']="Soy un nuevo valor"
print(diccionario_ejemplo)

for nombre, valor in diccionario_ejemplo.items():
    print(nombre, valor)

print(diccionario_ejemplo.items())

# if en python
edad_adolescente = 14
edad_adulta = 18
edad_adulto_mayor = 65

for i in ["primera", "segunda", "tercera", "cuarta vez"]:
    edad = float(input("dime la edad: "))

    if edad > 0 and edad < edad_adolescente:
        print("es un niño")
    elif edad >= edad_adolescente and edad <edad_adulta:
        print("es un adolescente")
    elif edad >= edad_adulta and edad < edad_adulto_mayor:
        print("es un adulto")
    elif edad >= edad_adulto_mayor:
        print("es un adulto mayor")
    else:
        print("es algo imposible")

# for en python
for numero in range(24, 32):
    print(numero)

for elemento in ["juan", "pelota", "arroz", "america", "rosado"]:
    print(elemento)

# while

contador = 0
while contador < 10:
    print(contador)
    print("Estamos recorriendo un while")
    contador = contador + 1



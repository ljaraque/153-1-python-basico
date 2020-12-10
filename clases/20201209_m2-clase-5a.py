## LISTAS ##

# Crear una lista vacía
# forma 1
lista_vacia_1 = list()
print(lista_vacia_1)

# forma 2
lista_vacia_2 = []
print(lista_vacia_2)

# otras listas
nombres = ["Luis", "Rubén", "José", "Claudio", "Etc"]
print(nombres)
otra_lista = [10, "Hola", 40, "Este es otro texto", (3,4), [1,2,3,4,5], nombres]
print(otra_lista)

# acceder a elementos de una lista
amigos = [ 'José', 'Gloria', 'Sandra' ]
print(amigos[1])

# iterar sobre listas
print("\nRecorrer elementos de una lista con FOR: ")
for amigo in amigos:
    print(amigo)

# CONCEPTO DE MUTABILIDAD
# Si creamos la variable a=1, a es mutable? a es inmutable?

a = 1
print("La variable a es: ", a)
print("El número de serie de nuetra variable a es:", id(a))

a = 2
print(a)
print("La variable a es:", a)
print("El número de serie de nuetra variable a es:", id(a))
print("Conclusión: la variable a no mutó, la destruimos y volvimos a crear otra con el mismo nombre, pero es otra")


nombre = "Nicolás"
print(nombre)
print("La variable nombre es:", nombre)
print("El 'número de serie' de la vairbale nombre es", id(nombre))

nombre = "José"
print(nombre)
print("La variable nombre es:", nombre)
print("El 'número de serie' de la vairbale nombre es", id(nombre))

# Las listas tienen características que las hacen ser MUTABLES.

lista_de_prueba = [1,2,3,4,5]
print("variable lista_de_prueba es:", lista_de_prueba)
print("El 'número de serie' de la variable lista_de_prueba es:", id(lista_de_prueba))

# modificar un elemento de la lista_de_prueba
lista_de_prueba[2] = "Soy un reemplazante"
print("variable lista_de_prueba es:", lista_de_prueba)
print("El 'número de serie' de la variable lista_de_prueba es:", id(lista_de_prueba))
print("Conclusión: El 'número de serie' (id) de lista_de_prueba no cambió. La lista MUTÓ")

# si ustedes hacen lo mismo con una tupla no van a lograrlo!!!!! (Probarlo como ejercicio)


# Largo de una lista
largo_de_lista = len(lista_de_prueba)
print("El largo de la lista, o número de elementos que contiene es:", largo_de_lista)

# Unir listas o concatenar

lista_1 = [1,2,3,4,5]
lista_2 = [0,9,8,7,6]

lista_concatenada = lista_1 + lista_2
print("Lista 1: ", lista_1, "Lista 2: ", lista_2)
print("La concatenación de lista_1 y lista_2 es:", lista_concatenada)

# mismo resultado pero aprovechando la mutabilidad
print("Lista 1 antes del cambio:", id(lista_1))
lista_1.extend(lista_2)
print("Lista 1 después del cambio:", id(lista_1))
print("Lista 1", lista_1)

# Segmentación de lista (Lists Slicing en inglés)

lista_a_segmentar = [-2,0, 0.6, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, "Otro", "Hola", "Mundo"]

# todo lo que está a la izquierda de un elemento de indice 5
sublista = lista_a_segmentar[:5]
print(sublista)

# todo lo que está a la derecha de un elemento de indice 3
sublista = lista_a_segmentar[3:]
print(sublista)

# desde y hasta
sublista = lista_a_segmentar[4:8]
print(sublista)

# Qué más podemos hacer con listas???? Para esto exploramos el objeto lista
# usando la función dir(): 'sacamos radiografías de objetos en python'

print(  dir(lista_a_segmentar)   )
# obtenemos métodos que el objeto lista nos provée: 
# [...., 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 
# 'pop', 'remove', 'reverse', 'sort']

# probemos algunos:

# insert()
print(lista_a_segmentar)
lista_a_segmentar.insert(7, "Soy un insertado")
print(lista_a_segmentar)

lista_nueva = [23,5,6,2,43,7,2,7,6,83]
# sort()
print(lista_nueva)
lista_nueva.sort()
print(lista_nueva)

lista_strings = ["hola", "aló", "caballo", "yoyo", "Loro"]
lista_strings.sort() # "Loro estará primero pues es mayúscula"
print(lista_strings)

# verificar pertenencia a una lista de el objeto "aló"

# método manual
booleano = False
for elemento in lista_strings:
    if elemento == "aló":
        booleano = True
print(booleano)

# método python
print(  "aló" in lista_strings  )
print(  "cebolla" in lista_strings  )

# Iterar sobre listas
for elemento in lista_a_segmentar:
    print(elemento)

# ejemplo de uso de mutabilidad de una lista
# no recomendado a no ser que sean listas muy grandes
# que comprometan la memoria disponible en el sistema

import random 

def agregar_invasor(lista):
    indice = random.randint(3, 7)
    lista.insert(indice, 5.8)

lista_amigos = ["Juan", "Rocío", "Rubén", "Pancho", "Juan", "Rosita", "Pedra", "Luciano", "Josefa"]
print(lista_amigos)
print(id(lista_amigos))

agregar_invasor(lista_amigos)

print(lista_amigos)
print(id(lista_amigos))


# este ej no funciona como mismo en caso lista
def modificar_elemento(variable):
    variable = variable + 1

variable_externa = 100
print(variable_externa)
modificar_elemento(variable_externa)
print(variable_externa)

# para que fuincione debo hacer
def modificar_elemento(variable):
    variable = variable + 1
    return variable

variable_externa = 100
print(variable_externa)
print(id(variable_externa))
variable_externa = modificar_elemento(variable_externa)
print(variable_externa)
print(id(variable_externa))


# remove()
def elimina_elemento_repetido(lista, elemento):
    set_amigos = set(lista)
    lista2 = list(set_amigos)
    lista2.remove(elemento)
    return lista2

resultado = elimina_elemento_repetido(lista_amigos, "Juan")
print(resultado)
print(lista_amigos)


def elimina_elemento_repetido_mutando(lista, elemento):
    while True:
        if elemento in lista:
            lista.remove(elemento)
        else:
            break

elimina_elemento_repetido_mutando(lista_amigos, "Juan")
print(lista_amigos)



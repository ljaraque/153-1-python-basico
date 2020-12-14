# funciones preexistentes
# https://docs.python.org/3/library/functions.html
# str()
# print()
# int()
# id()
# input()
# len()
# ...

# funcion print()
# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)¶

print("Hola Loco", "Cómo te va?", 56, "Chile", sep='-->', end='')

print("Hola Loco" + "Cómo te va?" + str(56) + "Chile")

# hacer que print() no imprima en pantalla sino a un archivo
archivo = open("archivo.txt", "a")
print("Hola Loco", "Aquí estamos", "probando", file=archivo)
archivo.close()

import time

for i in range(0,4):
    print(".", end='', flush=True)
    time.sleep(0.3)
print()

# hemos mostrado el uso de todos los parámetros de la función print()

# funciones con parámetros de cantidad indefinida
# *args
def sumar(*args):
    resultado = sum(args)
    return resultado

# nuestra función opera para cualquier núemro de argumentos
print(sumar(1,2,3,4,5,6,7,8))
print(sumar(2,3,4,56,7,3))
print(sumar(1,2))

def concatenar(*cosas):
    resultado = ""
    for elemento in cosas:
        resultado += str(elemento)
    return resultado

print( concatenar("Hola", "a", "b", "Como estás",34,5,6,7))

# parametros de número indefinido con clave-valor
# python lo convertirá a diccionario internamente en la función

def genera_diccionario(**datos):
    return datos

variable = genera_diccionario(
                    nombre="Paula", 
                    apellido="Jaraquemada", 
                    edad=400, 
                    nacionalidad="Chilena", 
                    altura="170"
                    )

print(variable["nombre"])
print(variable["apellido"])

variable2 = genera_diccionario(
                        direccion_1={
                            'calle':'alameda', 
                            'numero': 456
                            }, 
                        direccion_2={
                            'calle':'teatinos', 
                            'numero': 1010
                            }
                        )

print(variable2)
print(variable2['direccion_1']['numero'])

# parentesis de anidamientos y condiciones

ficha="N"
while (ficha != "O") and (ficha != "X"):
    time.sleep(0.3)
    ficha = input("Ingrese ficha:")

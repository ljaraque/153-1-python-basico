# Programa Principal
edad = 40

# Funciones

# definir la función
def sumar_dos_numeros(numero1, numero2):
    """suma dos numeros reecibidos como
       argumentos:
       - numero1
       - numero2
    """
    # este es el mundo propio de la función
    # las variables numero1, numero2 y resultado
    # solo existen dentro de la funcion
    resultado = numero1 + numero2
    #print(resultado) # evitar prints desde dentro de la función
    return resultado

primero = 40
segundo = 30

# invocar la función
cajon_para_recibir_resultado = sumar_dos_numeros(primero, segundo)
print(cajon_para_recibir_resultado)


# Casos de violación a nuestro principios fundamentales
# de una función:
# 1. Leer variables externas (globales) sin que hayan pasado como argumento
# 2. Crear variables globales dentro de la función para que sean leidas desde
#    el exterior.

a = 10 # variable que entrará a la función "por la ventana"

def multiplica(u, v):
    global b
    b = 30
    res = u * v * a # usamos variable que entró fuera de regla
    return res

resultado_obtenido = multiplica(20, 45)
otro_resultado_bajo_la_mesa = b # estamos leyendo variable que sale por canal informal desde función
print(resultado_obtenido)
print(otro_resultado_bajo_la_mesa)

# una función es un objeto
# hacemos radiografía de sumar_dos_numeros() y de multiplica() con la función dir()

print(   dir(sumar_dos_numeros), type(sumar_dos_numeros)    )
print()
print(   dir(multiplica), type(multiplica)    )


# orden de los parametros importa
def datos_personales(nombre, apellido, run, edad):
    edad = edad + 1
    resultado = nombre + " " + apellido + " " + run + " " + str(edad) + "años"
    return resultado

print( datos_personales("Waldo", "Wayne", "12.345.987-2", 40)   )
print( datos_personales("José", "Guerra", "12.345.937-2", 18)   )

# si uso la palabra clave del parametro, entonces podría pasar los argumentos
# en otro orden
print( datos_personales(edad=40, apellido="Silva", nombre="Martín", run="23987498234"))

# valores predeterminados (por defecto) en una función

def factorial_y_saludo(numero, saludo="Aquí estamos bien los 33"):
    resultado = 1
    for i in range(1, numero+1):
        resultado = resultado * i
    return resultado, saludo

print(   factorial_y_saludo(3)   )  # utilizo el saludo por defecto / no paso el argumento
print(   factorial_y_saludo(3, saludo = "Hola cómo les va")   ) # reemplazo el saludo por defecto


# listas como parámetros

def saludar_a_todos(nombres):
    resultado = []
    for nombre in nombres:
        resultado.append("Hola " + nombre + " Bienvenido!!")
    return resultado

amigos = ["Nabucodonosor", "Papá Pitufo", "Atila", "Jesús", "Buda", "Krishna", "Krishnamurti", "Nietzsche"]

camion_que_recibe_resultado = saludar_a_todos(amigos)
for saludo in camion_que_recibe_resultado:
    print(saludo)


# ******** Caso especial: Procesar una lista con una función
# Especialmente cuando son listas con muuuuuuuuchos datos

tarjetas = [
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad",
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc","Ac",
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad",
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc","Ac",
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad",
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc","Ac",
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad",
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc","Ac",
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad",
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc","Ac",
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad",
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc","Ac",
            "2s","3s","4s","5s","6s","7s","8s","9s","10s","Js","Qs","Ks","As",
            "2h","3h","4h","5h","6h","7h","8h","9h","10h","Jh","Qh","Kh","Ah",
            "2d","3d","4d","5d","6d","7d","8d","9d","10d","Jd","Qd","Kd","Ad",
            "2c","3c","4c","5c","6c","7c","8c","9c","10c","Jc","Qc","Kc","Ac"        
           ]

# Cuando son listas a veces se usa no poner retorno pues
# las listas son mutables, y por lo tanto
# la lista original contendrá los cambios luego de ejecutada
# la función

def inyectar_invasor(una_lista):
    import random
    indice = random.randint(0,len(una_lista))
    invasor = "COVID_AWAKELAB"
    una_lista.insert(indice, invasor)

print()
print(id(tarjetas))
inyectar_invasor(tarjetas)
print(id(tarjetas))
print( tarjetas )

# lo mismo pero con return
def inyectar_invasor(una_lista):
    import random
    indice = random.randint(0,len(una_lista))
    invasor = "COVID_AWAKELAB"
    una_lista.insert(indice, invasor)
    return una_lista

print()
print("ID de lista tarjetas: ", id(tarjetas))
caja_de_recepcion = inyectar_invasor(tarjetas)
print("ID de caja de recepcion: ", id(caja_de_recepcion))
print( caja_de_recepcion )


# Preview de Clase Siguiente:
# def funcion(*args):
#
# def funcion(*kwargs):
#
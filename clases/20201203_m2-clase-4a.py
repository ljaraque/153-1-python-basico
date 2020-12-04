import time

# lavadora mala

print("Lavadora 1:")
n = 5
while n > 0 :
    print('Lavar')
    print('Enjuagar')
    n = n-1
print('Secar!')

# lavadora 2

print("Lavadora 2:")
n = 3
while n > 0 :
    print('Lavar')
    print('Enjuagar')
    time.sleep(0.3)
    n = n - 1
print('Secar!')

# preguntador para aprender Break
a = 1
while a <=3:
    print("A:", a)
    c = 1
    while c <= 4:
        print("C:", c)
        linea = input('Dime: ')
        if linea == 'fin' :
            break # interrumpe solo el while mas interno!!!!!
        print(linea)
        c += 1
    a = a + 1 
print('Fin!')

# preguntador para aprender Continue
print("Comienzo de estudio de Continue")
a = 1
while a <=3:
    print("A:", a)
    c = 1
    while c <= 4:
        print("C:", c)
        linea = input('Dime: ')
        c += 1
        if linea == 'fin' :
            # interrumpe solo la iteracion actual y pasa a la siguiente no rompe el while!!!!!
            # continue sólo omite el resto del código de la iteración actual
            continue 
        print("La iteración se cumplió completa")
    a = a + 1 
print('Fin!')


# for sólo recorre todos los elementos de la secuencia que se le pase

print("Caso lista: ")
for elemento in ["a", 3, 4, 5, "hola", "animal", 45, 900]:
    print("Estoy atendiendo a:", elemento)

print("Caso tupla: ")
for elemento in ("a", 3, 4, 5, "hola", "animal", 45, 900):
    print("Estoy atendiendo a:", elemento)

print("Caso rango: ")
for i in range(2, 20):
    print(i)

mi_nombre = "Bruce Lee"

#lista en modo "carretero"
lista_resultado = []
for elemento in mi_nombre:
    lista_resultado.append(elemento)
print(lista_resultado)

#lista por comprensión
lista_resultado2 = [letra for letra in mi_nombre]
print(lista_resultado2)


# range
import random
for i in range(0,100, random.randint(1,6)):
    print(i)

# suma de 0 a 100 con for
acumulador = 0
for raton in range(0,101):
    acumulador = acumulador + raton
print(acumulador)

# suma de 0 a 100 sin for
print(sum(list(range(0,101))))

# factorial
# factorial de 3 --> 3*2*1
# factorial de 10 --> 10*9*8*7*6*5*4*3*2*1
def factorial(numero):
    resultado = 1 
    for i in range(1, numero+1):
        resultado = resultado * i
    return resultado
print(factorial(5))


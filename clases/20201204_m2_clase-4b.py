# función range()
rango = range(3,10)
print(list(rango))

rango = range(10, 2, -1)
print(list(rango))

# bomba de tiempo en base for
for i in [5, 4, 3, 2, 1] :
    print(i)
print('Boom!')

# for en base a lista de strings

for elemento in ("Carlos", "Claudio", "Pamela", "Jonathan", "etc"):
    print("Hola " + elemento)

# busqueda del numero mayor
mayor_hasta_ahora = -1
print('Antes', mayor_hasta_ahora)
for elemento in [9, 41, 12, 3, 74, 15] :
   if elemento > mayor_hasta_ahora:
      mayor_hasta_ahora = elemento
   print(mayor_hasta_ahora, elemento)

print('Después', mayor_hasta_ahora)

# contar con un for

contador = 0
for cosa in [2, 3, 4, 5, 6, "rewre", "kjaklsd", (1,2,3,4), (1,2), [4,5,6]]:
    contador = contador + 1
print("El número de cosas es:", contador)


# sumar con for
numeros_a_sumar = (300,25,45,67,87,100)
print("La suma es: ", sum(numeros_a_sumar))

acumulador = 0
for numero in numeros_a_sumar:
    acumulador = acumulador + numero
print("La suma con for: ", acumulador)

# promedio con un loop

print("El promedio es: ", sum(numeros_a_sumar)/len(numeros_a_sumar))
acumulador = 0
contador = 0
for numero in numeros_a_sumar:
    contador = contador + 1
    acumulador = acumulador + numero

print("El promedio con for es: ", acumulador/contador)


# buscar dentro de una estructura en base a for
lista = [9, 41, 12, 3, 74, 15]

impares = list()
for numero in lista:
    if numero % 2 != 0:
        impares.append(numero)
print("Los numeros seleccionados son:", impares)


# verificar si un número está dentro de una estructura de datos

veredicto = False
numero_buscado = 1
for numero in lista:
    if numero == numero_buscado:
        veredicto = True
print("Veredicto:", veredicto)

# buscar menor numero

menor_hasta_ahora = lista[0]
for numero in lista:
    if numero < menor_hasta_ahora:
        menor_hasta_ahora = numero
print("El número menor es:", menor_hasta_ahora)


# "=="" vs "is"
numero_contagiados = 350
numero_enfermos = 350
print(id(numero_contagiados))
print(id(numero_enfermos))
print(id(350))
print("numero_contagiados == numero_enfermos ", numero_contagiados == numero_enfermos)
print("numero_contagiados is numero_enfermos", numero_contagiados is numero_enfermos)

if numero_contagiados == numero_enfermos:
    print("Son iguales según ==. Estamos a Salvo !!!!")
else:
    print("No son iguales según == !!!\nDebemos aplicar Eutanasia urgentemente")

if numero_contagiados is numero_enfermos:
    print("Son iguales según 'is'. Estamos a Salvo !!!!")
else:
    print("No son iguales según 'is' !!!\nDebemos aplicar Eutanasia urgentemente")

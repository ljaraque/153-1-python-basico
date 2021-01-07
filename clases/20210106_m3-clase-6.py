

'''
# Ejemplo1: guardar texto en un archivo
texto_a_guardar = "Nuestro primeros datos valiosos a guardar en un archivo para uso futuro\n"

# escribir en archivo de texto
archivo = open("data/datos_valiosos.txt", "w")
archivo.write(texto_a_guardar)
archivo.close()
'''

'''
# Ejemplo2: guarda dato continuamente y fecha hora en un archivo
import time
import random
import datetime

with open("data/datos_valiosos.txt", "a") as archivo:
    for i in range(0,20):
        dato = random.randint(10,50)
        linea_a_guardar = str(dato) + " " + str(datetime.datetime.now()) + "\n"
        print("Agregando datos:", linea_a_guardar)
        archivo.write(linea_a_guardar)
        time.sleep(1)
'''

'''

# Ejemplo3: Recuperar datos desde archivo
with open("data/quijote.txt") as file:
    print(len(file.read()))
    file.seek(0)
    for i in range(0, 8):
        print(file.readline())
    
    print("Buscando línea 185")
    for i, line in enumerate(file):
        if i == 185:
            print(line)
'''

'''
#Ejemplo4: Archivo CSV
import csv

with open('data/iris.csv', 'r') as file:
    reader = csv.reader(file)
    #for linea in reader:
    #    print(linea)
    datos = list(reader)
    print(datos)

    acumulador = 0
    contador = 1
    for linea in datos[1:]:
        print(linea)
        acumulador += float(linea[0])
        print("Acumulador:", acumulador)
        contador += 1
        print("Contador: ", contador)
    print("Calculado promedio de sepal_length:", acumulador/contador)
'''

import csv
with open('data/iris.csv', 'r') as file:
    reader = csv.DictReader(file)
    print(reader.__sizeof__())
    print(reader)
    lista = list(reader)
    print(lista.__sizeof__())
    file.seek(0)
    
    file.seek(6)
    for linea in reader:
        print(linea)
        break


    exit()

    linea_objetivo = 6
    for num, linea in enumerate(reader):
        if num == linea_objetivo:
            print("Linea buscada", linea)
    


    exit()
    #for linea in reader:
    #    print(linea)

    for elemento in list(reader):
        print(elemento)

    file.seek(0)
    print("Línea 100: ", list(reader)[100])
    file.seek(0)
    print("petal_length de línea 100:", list(reader)[100]['petal_length'])

    

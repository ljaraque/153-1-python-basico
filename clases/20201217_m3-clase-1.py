numero_a = 1
print(   type(numero_a)   )

numero_b = 2.5
print(   type(numero_b)    )

lista_1 = [1,2,3,4,5]
print(   type(lista_1))

tupla_1 = (1,2,3,4,5)
print(   type(tupla_1))

nombre = "Rocío de las Mercedes"
print(   type(nombre))

def sumar(a,b):
    return a + b
print(   type(sumar)   )

print( type(   print    ))

print( type(   input    ))

def alguna_funcion():
    pass

print( type(alguna_funcion)  )

#### !!!!!!! la función dir() y la función type() son esenciales para explorar objetos en python

#### definir nuestra propia clase

class SerVivo00:
    pass

trinity = SerVivo00() 
neo = SerVivo00()
morfeo = SerVivo00()

print("Tipo e id de trinity",    type(trinity), id(trinity)   )
print("Tipo e id de neo",    type(neo), id(neo)   )
print("Tipo e id de morfeo",    type(morfeo), id(morfeo)   )

#### Mas allá de nuestra comprensión en este curso
print(   type(SerVivo00)    )
print(   type(type)    )

#### las clases retornan un objeto
#### para los curiosos: Las metaclases son clases que retornan otra clase

#### Aterricemos desde el ciberespacio a casos más prácticos, aunque aún
# con seres vivos

class SerVivo:
    
    def __init__(self, especie, nombre, peso, altura):
        self.especie = especie
        self.nombre = nombre
        self.peso = peso
        self.altura = altura


def imprimir_atributos(objeto):
    print(objeto.especie)
    print(objeto.nombre)
    print(objeto.peso)
    print(objeto.altura)

luke = SerVivo(especie="Humana", nombre="Luke Skywalker", peso=80, altura=180 )

print("Dir y type de luke", dir(luke), type(luke))
imprimir_atributos(luke)

firulais = SerVivo(especie="Canina", nombre="Firulistapus Almacigus", peso=10, altura=60 )

print("Dir y type de firulais", dir(firulais), type(firulais))
imprimir_atributos(firulais)

luke.peso = 65
firulais.peso=15
imprimir_atributos(luke)
imprimir_atributos(firulais)

# le agregamos comportamientos a nuestros seres vivos

class SerVivoPlus:

    def __init__(self, especie, nombre, peso, altura):
        self.especie = especie
        self.nombre = nombre
        self.peso = peso
        self.altura = altura
        self.posicion_x = 0

    def alimentarse(self, cantidad_de_alimento):
        self.peso = self.peso + cantidad_de_alimento
        self.altura = self.altura + 0.01 * cantidad_de_alimento
        return self.peso, self.altura

    def ejercitar(self, tiempo):
        self.peso = self.peso - 0.01 * tiempo # por ejemplo pierde 1 gramo por hora
        return self.peso
    
    def eliminar_desechos(self, cantidad_de_desecho):
        self.peso = self.peso - cantidad_de_desecho
        return self.peso

    def desplazarse(self, delta_x):
        self.posicion_x = self.posicion_x + delta_x
        self.ejercitar(0.001 * delta_x)
        return self.posicion_x, self.peso


diego = SerVivoPlus(especie="Humano", nombre="Diegus Maradonus", peso=100, altura=165)
koby = SerVivoPlus(especie="Humano", nombre="Kobe Brian", peso=100, altura=205)
porky = SerVivoPlus(especie="Cerdo", nombre="Cerdito Porky", peso=120, altura=80)

seres = [diego, koby, porky]

def imprimir_atributos2(objeto):
    print(objeto.especie)
    print(objeto.nombre)
    print(objeto.peso)
    print(objeto.altura)
    print(objeto.posicion_x)

import time
import random

def transcurrir_vida():
    while True:
        for ser in seres:
            cantidad_alimento=random.uniform(0.1, 1.8)
            ser.alimentarse(cantidad_alimento)
            tiempo_ejercicio=random.uniform(10, 30)
            ser.ejercitar(tiempo_ejercicio)
            cantidad_desecho=random.uniform(0.2, 0.5)
            ser.eliminar_desechos(cantidad_desecho)
            distancia_deplazamiento = random.uniform(-50, 50)
            ser.desplazarse(distancia_deplazamiento)
            #imprime estado del ser
            print("El estado del ser:", ser.nombre, "es: ")
            imprimir_atributos2(ser)
        time.sleep(0.1)

transcurrir_vida()


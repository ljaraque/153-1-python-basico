# STRINGS


'''
# definir strings y concatenar
texto_de_prueba = "Somos Terrícolas"
texto_de_prueba_2 = " Del Tercer Planeta"

resultado = texto_de_prueba + texto_de_prueba_2

print(resultado)

# números pueden ser strings

texto_con_numero = "500"
texto_com_numero_2 = "400"

resultado = texto_con_numero + texto_com_numero_2

print(resultado)

# sumar tipos distintos en Python genera error (TypeError)

#resultado = 500 + "400"

# Obtener datos desde el usuario y sumarlos.
# debemos convertir strings a entero o otro tipo numérico para obtener
# resultados de operaciones numéricas

datos = list()
for i in range(0,2):
    dato = int(input("Ingrese un número: "))
    datos.append(dato)
resultado = sum(datos)
print(resultado)
'''

# elementos de un string

texto = "Hola cómo estás?"

for elemento in texto:
    print(elemento)

import random

largo_texto = len(texto)
indice_random = random.randint(0, largo_texto)

print(texto)
print("Letra cualquiera")
letra_cualquiera = texto[random.randint(0, indice_random)]
print(letra_cualquiera)

# Strings son Mutables o Inmutables?

print(texto)
texto_lista = list(texto)
print(texto_lista)
texto_lista[5] = "a"
print(texto_lista)
print(str(texto_lista))
print(''.join(texto_lista))

def modificar_string(texto, posicion, caracter):
    texto_lista = list(texto)
    texto_lista[posicion] = caracter
    return ''.join(texto_lista)

texto_nuevo = "Estamos probando Python"
print(texto_nuevo)
print(id(texto_nuevo))
texto_nuevo =  modificar_string(texto_nuevo, 5, "e")
print(id(texto_nuevo))

print(texto_nuevo)

# Segmentación de Strings
# IDEM a listas

libro = '''Cervantes  comienza  fingiendo  ser  una 
especie  de  erudito  que  recopila  datos  de  otros 
autores  y  de  los  papeles  de  los  archivos  de  la 
Mancha para ordenar la historia de Don Quijote. En un 
momento determinado interrumpe el curso de la narración,   
mostrándose   apesadumbrado   por   no saber  más  de  su  
hidalgo.  Un  hallazgo  casual  le permite reanudar el hilo 
de su “verdadera historia”.'''

print("XXXX")
print(  libro[:38]    )
print("XXXX")
print(  libro[38:]    )
print("XXXX")
print(  libro[80:120]  )

# Algunos métodos disponibles en eobjetos de tipo String

nombre = "rolanda"
# capitalize: mayúscula la primera letra
print(nombre.capitalize())
# find: busca el substring y entrega indica de la primera aparición
print(nombre.find("an"))

# replace: reemplaza un substring por otro subtring en todas sus apariciones
texto_nuevo = "Estamos probando Python"
print(texto_nuevo, id(texto_nuevo))
texto_nuevo = texto_nuevo.replace("a", "XXXXXX")
print(texto_nuevo, id(texto_nuevo))
# buena pregunta de claudio vergara
print(id("Estamos probando Python")) #Aquí vemos que el id original sigue existiendo

# lower: pasar a minúsculas un string
texto_mayusculas = "HOLA COMO ESTAN TODOS?"
print(texto_mayusculas)
print(texto_mayusculas.lower())
print(texto_mayusculas.lower().upper())
# strip: 
extracto_libro = "     Aquí estamos          "
print(extracto_libro.strip())


# DICCIONARIOS

# estructura de datos en que accedo a ellos por un nombre/etiqueta
# que puede ser un string o un número 
diccionario_chico = {'comer': 'acción de alimentarse',
                    'dormir': 'acción de descansar en un estado mental especial',
                    'correr': 'caminar de forma tal que en un momento ambos pies están en el aire',
                    -101.5: "Soy otro elemento"
                    }

print( diccionario_chico['correr'] )
print( diccionario_chico[-101.5] )


# diccionario puede contener cualquier objeto de python
diccionario_variado =  {
    'nombres': ['Juana', 'Rosa', 'Mosqueta', 'Romiro', 'Raúl' ],
    'apellidos': ['Pérez', 'Díaz', 'Orrigorrieta', 'Rivadeneira', 'Lagos'],
    'telefonos': ['+5699999999999', '+5690000000000', '+569873245987345', ' +5687623874624', '+568726348764'],
    'direccion': [{'calle': 'calle1', 'numero':70, 'comuna': 'Maipú'},
                    {'calle': 'calle40', 'numero':80, 'comuna': 'Peñalolén'},
                    {'calle': 'calle145', 'numero':170, 'comuna': 'La Florida'},
                    {'calle': 'calle146', 'numero':720, 'comuna': 'Lo Barnechea'},
                    {'calle': 'calle17', 'numero':370, 'comuna': 'Estación Central'}]
}

print(diccionario_variado['direccion'])
print(diccionario_variado['direccion'][0])
print(diccionario_variado['direccion'][0]['comuna'])




# un diccionario más realista
diccionario_poderoso = {
  "version": "1.6.0",
  "autor": "mindicador.cl",
  "fecha": "2020-12-10T22:00:00.000Z",
  "uf": {
    "codigo": "uf",
    "nombre": "Unidad de fomento (UF)",
    "unidad_medida": "Pesos",
    "fecha": "2020-12-10T03:00:00.000Z",
    "valor": 29090.04
  },
  "ivp": {
    "codigo": "ivp",
    "nombre": "Indice de valor promedio (IVP)",
    "unidad_medida": "Pesos",
    "fecha": "2020-12-10T03:00:00.000Z",
    "valor": 30182.71
  },
  "dolar": {
    "codigo": "dolar",
    "nombre": "Dólar observado",
    "unidad_medida": "Pesos",
    "fecha": "2020-12-10T03:00:00.000Z",
    "valor": 739.45
  },
  "dolar_intercambio": {
    "codigo": "dolar_intercambio",
    "nombre": "Dólar acuerdo",
    "unidad_medida": "Pesos",
    "fecha": "2014-11-13T03:00:00.000Z",
    "valor": 758.87
  },
  "euro": {
    "codigo": "euro",
    "nombre": "Euro",
    "unidad_medida": "Pesos",
    "fecha": "2020-12-10T03:00:00.000Z",
    "valor": 891.87
  },
  "ipc": {
    "codigo": "ipc",
    "nombre": "Indice de Precios al Consumidor (IPC)",
    "unidad_medida": "Porcentaje",
    "fecha": "2020-11-01T03:00:00.000Z",
    "valor": -0.1
  },
  "utm": {
    "codigo": "utm",
    "nombre": "Unidad Tributaria Mensual (UTM)",
    "unidad_medida": "Pesos",
    "fecha": "2020-12-01T03:00:00.000Z",
    "valor": 51029
  },
  "imacec": {
    "codigo": "imacec",
    "nombre": "Imacec",
    "unidad_medida": "Porcentaje",
    "fecha": "2020-10-01T03:00:00.000Z",
    "valor": -1.2
  },
  "tpm": {
    "codigo": "tpm",
    "nombre": "Tasa Política Monetaria (TPM)",
    "unidad_medida": "Porcentaje",
    "fecha": "2020-12-10T03:00:00.000Z",
    "valor": 0.5
  },
  "libra_cobre": {
    "codigo": "libra_cobre",
    "nombre": "Libra de Cobre",
    "unidad_medida": "Dólar",
    "fecha": "2020-12-10T03:00:00.000Z",
    "valor": 3.48
  },
  "tasa_desempleo": {
    "codigo": "tasa_desempleo",
    "nombre": "Tasa de desempleo",
    "unidad_medida": "Porcentaje",
    "fecha": "2020-10-01T03:00:00.000Z",
    "valor": 11.58
  },
  "bitcoin": {
    "codigo": "bitcoin",
    "nombre": "Bitcoin",
    "unidad_medida": "Dólar",
    "fecha": "2020-12-06T03:00:00.000Z",
    "valor": 19377.66
  }
}

print("Valor del dolar: ", diccionario_poderoso['dolar']['valor'])

# iterar sobre diccionarios

diccionario = {'comer': 'acción de alimentarse',
                    'dormir': 'acción de descansar en un estado mental especial',
                    'correr': 'caminar de forma tal que en un momento ambos pies están en el aire',
                    -101.5: "Soy otro elemento"
                    }

# se recurre a la transformación dada por metodo items() que entrega un iterable
print(diccionario.items())

for clave, valor in diccionario.items():
  print(clave, ": ", valor)


# conteo de palabras y almacenaje en diccionarios
import time
cuentas = dict()

texto = input('Ingrese un texto:')
palabras = texto.split()
print('Palabras:', palabras)

print('Contando...')
time.sleep(3)
for palabra in palabras:
    cuentas[palabra] = cuentas.get(palabra,0) + 1
print('Cuentas', cuentas)



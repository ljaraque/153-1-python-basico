class Yagan:
    num_ruedas = 4
    num_velocidades = 4
    modelo = "Yagan"
    num_puertas = 5

    def __init__(self, color, nivel_estanque): 
        self.color = color
        self.nivel_estanque = nivel_estanque
        self.posicion_x = 0

    def avanzar(self, distancia):
        self.posicion_x += distancia
        self.nivel_estanque += -0.1 * distancia
        return self.posicion_x

    def estado(self):
        print("Color:", self.color)
        print("Nivel Estanque:", self.nivel_estanque)
        print("Posición X:", self.posicion_x)


auto_1 = Yagan("Rojo", 30)
auto_2 = Yagan("Azul", 30)

auto_1.estado()
print( dir(auto_1))
auto_2.estado()
print(dir(auto_2))

auto_1.avanzar(20)
auto_2.avanzar(50)
auto_1.estado()
auto_2.estado()

autos_rojos = []
for i in range(0,10):
    autos_rojos.append(Yagan("Rojo", 5))

for auto in autos_rojos:
    print(id(auto))
    auto.estado()
    print()

# cambiar nivel de estanque de todos los autos creados en serie
for auto in autos_rojos:
    auto.nivel_estanque += 5

for auto in autos_rojos:
    print(id(auto))
    auto.estado()
    print()

for auto in autos_rojos:
    print(auto.num_velocidades)

Yagan.num_velocidades = 5

for auto in autos_rojos:
    print(auto.num_velocidades)


# Ejemplo de la capericita roja
# Hay muchas caperucitas rojas en un reino

class Caperucita:
    color_capa = "Rojo"

caperucitas = []
for i in range(0,10):
    caperucitas.append(Caperucita())

for caperucita in caperucitas:
    print("El color de la capa de la caperucita "+str(id(caperucita))+" es: " + caperucita.color_capa)

# lo que hacemos a continuación es crear un atributo de instancia del mismo
# nombre que un atributo de clase
# y cuando posteriormente consulte su valor, lo que primero revisa Python es
# el atributo de instancia y si no encuentra busca el nombre en los atributos 
# de clase
caperucitas[2].color_capa = "Verde"
print(id(caperucitas[2]), type(caperucitas[2]))


for index, caperucita in enumerate(caperucitas):
    print(index, " El color de la capa de la caperucita "+str(id(caperucita))+" es: " + caperucita.color_capa)

print("El rey se enojó y mandó a hacer rojas todas las capas!!!")
Caperucita.color_capa = "Azul"

# la caperucita que se pudo capa Verde (Atributo de Instancia) tiene la capa Azul 
# guardada (Como atributo de Clase)
# y se accede con .__class__.color_capa
for index, caperucita in enumerate(caperucitas):
    print(index, " El color de la capa de la caperucita "+str(id(caperucita))+" es: " + caperucita.color_capa +" "+ caperucita.__class__.color_capa)


# Agregar Reino y Caperucitas de tal forma que Caperucitas dejen de existir si reino deja de existir
class Reino:

    def __init__(self, num_caperucitas):
        self.superficie = 100000
        self.caperucitas = self.crear_caperucitas(num_caperucitas)
        print("Reino creado de "+str(self.superficie)
                +" metros cuadrados y con caperucitas:\n"+str(self.caperucitas))
        for caperucita in self.caperucitas:
            print("Caperucita "+str(id(caperucita)))
    
    def crear_caperucitas(self, num_caperucitas):
        lista_caperucitas = []
        for n in range(0,num_caperucitas):
            lista_caperucitas.append(Caperucita())
        return lista_caperucitas

reino_1 = Reino(9)
for index, caperucita in enumerate(reino_1.caperucitas):
    print(index, " El color de la capa de la caperucita "+str(id(caperucita))+" es: " + caperucita.color_capa +" "+ caperucita.__class__.color_capa)

del reino_1
try:
    print(reino_1.caperucitas)
except Exception as e:
    print("Error, no puedo acceder a las caperucitas pues el reino_1 dejó de existir\n",e)


# Agregar Reino y Caperucitas de tal forma que Caperucitas sigan existiendo si reino deja de existir
class ReinoX:

    def __init__(self, *caperucitas):
        self.superficie = 100000
        self.caperucitas = list(caperucitas)
        print("Reino creado de "+str(self.superficie)
                +" metros cuadrados y con caperucitas:\n"+str(self.caperucitas))
        for caperucita in self.caperucitas:
            print("Caperucita "+str(id(caperucita)))
    
caperucita_1 = Caperucita()
caperucita_2 = Caperucita()
caperucita_3 = Caperucita()
caperucita_4 = Caperucita()
caperucita_5 = Caperucita()

reino_2 = ReinoX(caperucita_1, caperucita_2, caperucita_3, caperucita_4, caperucita_5)

print("Destruyendo reino_2")
del reino_2
try:
    print("Reino", id(reino_2))
except Exception as e:
    print(e)
print("Caperucita", id(caperucita_1))
print("Caperucita", id(caperucita_2))
print("Caperucita", id(caperucita_3))
print("Caperucita", id(caperucita_4))
print("Caperucita", id(caperucita_5))

print("El reino_2 ya no existe pero las caperucitas siguen existiendo")



# sobrecarga de métodos

class WebScraper:

    def __init__(self, nombre):
        self.nombre = nombre

    def obtener_paginas(self, *urls):
        for url in urls:
            print("Scrapeando dirección: ", url)

    def elemento_a_scrapear(self, **elementos):
        for key, value in elementos.items():
            print("Voy a scrapear: ", key, ":", value)

scraper_1 = WebScraper("ScraperX")

scraper_1.obtener_paginas("https://www.google.com", "https://www.emol.com")
scraper_1.obtener_paginas("https://www.google.com", "https://www.emol.com",
                            "www.cfg.com", "www.gekonus.com", "www.sandias.com",
                            "www.lider.cl", "www.tottus.cl", "www.jumbo.cl",
                            "www.oferta.cl")

scraper_1.elemento_a_scrapear(etiquetas = ['precio', 'descripcion'],
                                imagenes=['producto', 'logo', 'vendedor'])

scraper_1.elemento_a_scrapear(etiquetas = ['precio', 'descripcion'],
                                imagenes=['producto', 'logo', 'vendedor'],
                                documentos=['terminos y condiciones', 'garantía'])


# attributos privados

class Auto:

    def __init__(self, marca, posicion, nivel_estanque, color):
        self.posicion = posicion
        self.__nivel_estanque = nivel_estanque
        self.color = color
        self.orientacion = 0
        self.marca = marca
        self.documento = {'marca': self.marca, 'color': self.color}
    
    def girar(self, grados):
        self.orientacion += grados
        return self.orientacion
    
    def avanzar(self, cantidad):
        self.posicion += cantidad
        self.__reducir_nivel_estanque(-0.1*cantidad)
        return self.posicion
    
    def cargar_combustible(self, cantidad):
        self.__nivel_estanque += cantidad
        return self.__nivel_estanque
    
    def __reducir_nivel_estanque(self, cantidad):
        self.__nivel_estanque += -cantidad

    def estado(self):
        print("ESTADO")
        print("Posición: ", self.posicion)
        print("Nivel Estanque: ", self.__nivel_estanque)
        print("Color: ", self.color)
        print("Orientación: ", self.orientacion)
        print("Documentación:", self.documento)


auto_mio = Auto("Toyota", 0, 50, "Rojo")

auto_mio.estado()
auto_mio.cargar_combustible(30)
auto_mio.estado()

auto_mio._Auto__nivel_estanque = 10
auto_mio.estado()
print( dir(auto_mio))

# esto no funciona pues es un metodo "privado"
try:
    auto_mio.reducir_nivel_estanque(10)
except Exception as e:
    print("ERROR: Se ha intentado utilizar un método privado.!!!!\n", e)


# yo podría usar el método si violo el espiritu de python
# ESTO NO SE HACE!!!!!!
print("Antes del cambio")
auto_mio.estado()
auto_mio._Auto__reducir_nivel_estanque(10)
print("Después del cambio")
auto_mio.estado()

# getter y setters
# Haremos que podamos modificar el color de nuestro auto

auto_mio.color="Azul"
print(auto_mio.color)
auto_mio.estado()
#   Enhorabuena!!!!! hemos podido moficar el colo porque es atributo no "privado"
# Pero hemos destruido la consistencia de nuestros datos

# Hemos cambiado el color, pero eso nos lleva a tener que:
# Actualizar documentos de auto (CUEK!!!!!!) (EFE!!!!)
# Tendremos que ir a hacer el trámite.
# Se puso latero
auto_mio.documento['color']="Azul"
auto_mio.estado()

# Enhorabuena Tío!!! Se ha recuperado la consistencia. Pero ahora es un cacho modificar la
# variable pública color


# Definimos una clase AutoX similar a Auto
class AutoX:

    def __init__(self, marca, posicion, nivel_estanque, color):
        self.posicion = posicion
        self.__nivel_estanque = nivel_estanque
        self.__color = color
        self.orientacion = 0
        self.marca = marca
        self.__documento = {'marca': self.marca, 'color': self.__color}
    
    def girar(self, grados):
        self.orientacion += grados
        return self.orientacion
    
    def avanzar(self, cantidad):
        self.posicion += cantidad
        self.__reducir_nivel_estanque(-0.1*cantidad)
        return self.posicion
    
    def cargar_combustible(self, cantidad):
        self.__nivel_estanque += cantidad
        return self.__nivel_estanque
    
    def __reducir_nivel_estanque(self, cantidad):
        self.__nivel_estanque += -cantidad

    def set_color(self, color_nuevo):
        self.__color = color_nuevo
        self.__documento['color']=color_nuevo

    def estado(self):
        print("ESTADO")
        print("Posición: ", self.posicion)
        print("Nivel Estanque: ", self.__nivel_estanque)
        print("Color: ", self.__color)
        print("Orientación: ", self.orientacion)
        print("Documentación:", self.__documento)

print("\n\n\nCaso basado en AutoX:")
auto_tuyo = AutoX("Toyota", 0, 50, "Rojo")
auto_tuyo.estado()
auto_tuyo.set_color("Azul")
auto_tuyo.estado()


# Finalmente luego de muchas reuniones de Pythonistas preocupados
# de si su lenguaje tenía futuro.
# Todos los códigos históricos se habían quebrado porque habría que utilizar
# setters y getters como métdos de aquí en adelante y actualizar todos los
# códigos de estilo python
# Citaron a todos los medios para mostrar que habían salido de la depresión
# generada por los otros programadores 
# llegaron con la siguiente solución

# Queremos insistir en usar estilo python para setear variables, y de todas formas
# lograr que se actualice por ejemplo la documentación del auto

class AutoY:

    def __init__(self, marca, posicion, nivel_estanque, color):
        self.posicion = posicion
        self.__nivel_estanque = nivel_estanque
        self.__color = color
        self.orientacion = 0
        self.marca = marca
        self.__documento = {'marca': self.marca, 'color': self.__color}

    ''' tip de investigación. Esto es un decorador en Python
    def property(alguna_funcion):
        #modifico la funcion 
        return funcion_modificada
    '''

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color_nuevo):
        self.__color = color_nuevo
        self.__documento['color']=color_nuevo
    
    def girar(self, grados):
        self.orientacion += grados
        return self.orientacion
    
    def avanzar(self, cantidad):
        self.posicion += cantidad
        self.__reducir_nivel_estanque(-0.1*cantidad)
        return self.posicion
    
    def cargar_combustible(self, cantidad):
        self.__nivel_estanque += cantidad
        return self.__nivel_estanque
    
    def __reducir_nivel_estanque(self, cantidad):
        self.__nivel_estanque += -cantidad

    def estado(self):
        print("ESTADO")
        print("Posición: ", self.posicion)
        print("Nivel Estanque: ", self.__nivel_estanque)
        print("Color: ", self.__color)
        print("Orientación: ", self.orientacion)
        print("Documentación:", self.__documento)

print("\n\n\nCaso basado en AutoY:")
auto_python = AutoY("Toyota", 0, 50, "Rojo")
print(auto_python.color)
auto_python.estado()
auto_python.color = "Azul"
auto_python.estado()

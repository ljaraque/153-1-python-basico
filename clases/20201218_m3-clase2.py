
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

    def __init__(self, posicion, nivel_estanque, color):
        self.posicion = posicion
        self.__nivel_estanque = nivel_estanque
        self.color = color
        self.orientacion = 0
    
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


auto_mio = Auto(0, 50, "Rojo")

auto_mio.estado()
auto_mio.cargar_combustible(30)
auto_mio.estado()

auto_mio._Auto__nivel_estanque = 10
auto_mio.estado()
print( dir(auto_mio))

# estao no funciona pues es un metodo "privado"
#auto_mio.reducir_nivel_estanque(10)

# yo podría usar el método si violo el espiritu de python
#auto_mio._Auto__reducir_nivel_estanque(10)

# getter y setters
'''
auto_mio.posicion = 20
auto_mio.posicion

auto_mio.set_posicion(20)
'''
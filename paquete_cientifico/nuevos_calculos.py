#--------------
#-Area y perimetro de circulo, dado su radio.
#--------------
#El área del círculo es igual al valor de su radio elevado al cuadrado 
#multiplicado por pi = p x r2. Una rueda, al dar una vuelta completa, 
#describe una trayectoria cuya longitud es el perímetro de la 
#circunferencia de la rueda.
def calcular_radio():
    print("---------------------------------------")
    print ("CALCULAR RADIO DE UN CIRCULO")
    pi=3.14
    radio=int(input("Ingresa el RADIO de tu circulo: "))
    area=(radio ** 2) * pi
    print ("El area es de tu circulo es: ",  area)
    print("---------------------------------------")

#--------------
#-Area y perimetro de triangulo, dadas su base y su altura.
#--------------
#El **área** de un triángulo es igual a base por altura partido por 2.
#La altura es la recta perpendicular trazada desde un vértice al lado 
#opuesto (o su prolongación).
#El **perímetro** de un triángulo es igual a la suma de sus tres lados.
def a_p_triangulo():
    print("---------------------------------------")
    print ("CALCULAR AREA DE UN TRIANGULO")
    base = int(input("Ingrese la base: "))
    altura = int(input("ingresa la altura: "))
    area = ((base * altura) / 2)
    print ("El AREA de tu triangulo es: ",  area)
    print("---------------------------------------")
    print ("CALCULAR PERIMETRO DE UN TRIANGULO")
    lado1 = int(input("Ingresa la medida de lado 1: "))
    lado2 = int(input("Ingresa la medida de lado 2: "))
    lado3 = int(input("Ingresa la medida de lado 3: "))
    perimetro = (lado1 + lado2 + lado3)
    print ("El PERIMETRO de tu triangulo es: ", perimetro)
    print("---------------------------------------")
#--------------
#-Area y perimetro de rectangulo, dados sus lados.
#Area:** del rectángulo es igual a la base por la altura. 
#Es decir, lado mayor por lado menor.
# #Perímetro:** Suma de sus cuatro lados.
#--------------
def a_p_rectangulo():
    print("---------------------------------------")
    print ("CALCULAR AREA DE UN RECTANGULO")
    base = int(input("Ingrese la base: "))
    altura = int(input("ingresa la altura: "))
    area = (base * altura)
    print ("El AREA de tu RECTANGULO es: ",  area)
    print("---------------------------------------")
    print ("CALCULAR PERIMETRO DE UN RECTANGULO")
    lado1 = int(input("Ingresa la medida de lado 1: "))
    lado2 = int(input("Ingresa la medida de lado 2: "))
    perimetro = ((lado1 + lado2) * 2)
    print ("El PERIMETRO de tu RECTANGULO es: ", perimetro)
    print("---------------------------------------")
#--------------
#-Distancia recorrida, dados tiempo y velocidad.
#Comprende la ecuación básica: D=v*t, 
# donde D es la distancia, "v" la velocidad y "t" es el tiempo. 
# Si te dan una velocidad a la cual alguien viaja y el tiempo 
# que le lleva viajar, puedes usar la ecuación para calcular 
# la distancia total recorrida
#--------------
def d_calcular_distancia():
    print("---------------------------------------")
    print ("CALCULAR DISTANCIA RECORRIDA")
    tiempo = int(input("Ingrese tiempo: "))
    velocidad = int(input("ingresa la velocidad: "))
    distancia_recorrida = (tiempo * velocidad)
    print ("La distancia recorrida con es igual a :",  distancia_recorrida)
    print("---------------------------------------")

#---------------------------


if __name__ == "__main__":
    calcular_radio()
    a_p_triangulo()
    a_p_rectangulo()
    d_calcular_distancia()
    
    
    
 

    
    

### Tips Ejercicios
'''
# Individual 4.b

precio_lista = 24.95
envio_base = 3
envio_marginal = 0.75

print("\nSistema de Compra de Libros")
for i in range(0, 5):
    numero_copias = int(input("\nCuántas copias quiere comprar?: "))
    if numero_copias > 10:
        precio_libro = precio_lista * 0.6
    else:
        precio_libro = precio_lista
    precio_total_libros = numero_copias * precio_libro
    costo_envio = 3 + 0.75 * (numero_copias-1)
    costo_total = precio_total_libros + costo_envio
    print("\nEl costo total de tu compra de libros es:", costo_total)

'''

# Individual 4.c

import script_pruebas

print("Ingrese horario de inicio:")
hora_inicio = float(input("Hora:"))
minutos_inicio = float(input("Minutos:"))
velocidad_suave = float(input("Ingrese Velocidad Suave:"))
distancia_tramo_suave = float(input("Ingrese Distancia Tramo Suave:"))
velocidad_intermedia = float(input("Ingrese Velocidad Intermedia:"))
distancia_tramo_intermedio = float(input("Ingrese Distancia Tramo Intermedio:"))
velocidad_alto = float(input("Ingrese Velocidad Alta:"))
distancia_tramo_alto = float(input("Ingrese Distancia Tramo Alto:"))

# v=d/t ----> t=d/v
tiempo_tramo_suave = distancia_tramo_suave / velocidad_suave
tiempo_tramo_intermedio = distancia_tramo_intermedio / velocidad_intermedia
timepo_tramo_alto = distancia_tramo_alto / velocidad_alto

tiempo_total = tiempo_tramo_suave + tiempo_tramo_intermedio + timepo_tramo_alto

print("La distancia total de mi trayecto es: ", 
            distancia_tramo_suave
            + distancia_tramo_intermedio
            + distancia_tramo_alto)
print("El tiempo total de mi trayecto es: ", tiempo_total) # resultado en horas

# quiero obtener HORA : MINUTOS + N dias como horario de retorno  

horario_inicio = (hora_inicio, minutos_inicio)

horario_termino = script_pruebas.horario_termino(horario_inicio, tiempo_total)

print("El horario de regreso es", str(horario_termino[0])+":"
        + str(horario_termino[1])+ " + "
        + str(horario_termino[2])+ " días adicionales")






#--------------------------------------------------------------------------------------------
#2. Investigue para qué se utiliza la sentencia if __name__ == "__main__": 
# en módulos python. ¿Qué permite?
# referencia: https://es.stackoverflow.com/questions/32165/qu%C3%A9-es-if-name-main
#
#Es decir, si tienes un archivo llamado mi_modulo.py, si lo ejecutamos como programa principal el atributo __name__ será '__main__', 
# si lo usamos importándolo desde otro módulo (import mi_modulo) el atributo __name__ será igual a 'mi_modulo'.
#Básicamente, lo que haces usando if __name__ == “__main__”: es ver si el módulo ha sido ejecutado directamente o no (importado). 
# Si se ha ejecutado como programa principal se ejecuta el código dentro del condicional.
                                                                #LISTO
#--------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------
#3. Utilice if __name__ == "__main__": en nuevos_calculos.py para
#probar las funciones que ha creado.                            #LISTO 
#--------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------
#4. Habilite las nuevas funciones creadas en el nuevo archivo como
#parte del paquete_cientifico.                                  #LISTO
#--------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------
#5. Cree 3 archivos adicionales similares a nuevos_calculos.py, que
#también contengan una zona de pruebas basada en if __name__== "__main__": 
# Cada uno de estos archivos debe contener 4 funciones básicas para algún 
# tipo de calculo matemático o físico de interés. 
# Los archivos deben estar definidos por temáticas. Por
#ejemplo uno para cálculos físicos, otro para cálculos matemáticos,
#otro para cálculos químicos, etc. Se sugiere definir en reunión
#conjunta los alcances y contenidos de cada archivo de manera
#general y distribuirlos en los distintos miembros del grupo.
#--------------------------------------------------------------------------------------------
#Funciones Calculos matematicos:
#funciones calculos fisicos:
#funciones calculos quimicos:
    
#--------------------------------------------------------------------------------------------
#6. Cada integrante a cargo de uno de los archivos, deberá habilitar su
#creación como parte del paquete_cientifico (En __init__.py).
#--------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------
#7. Cada integrante deberá trabajar en una rama Git correspondiente a
#la funcionalidad que está desarrollando y hacer push a un
#repositorio del grupo de trabajo para este proyecto.
#--------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------
#8. Crear un script fuera del paquete, que importe éste mismo y utilice
#todas las funciones del módulo.
#--------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------
#9. El grupo deberá acordar quién y cómo se realizará la convergencia
#de los trabajos individuales. ¿Qué ramas utilizarán? ¿Quién realizará
#las acciones de merge?
#--------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------
#10. El repositorio deberá quedar disponible en un repositorio GitHub
#público.
#-----------------------------------------------------------
def vol_cilindro(altura, area_base):
    volumen = altura*area_base
    return volumen

import paquete_cientifico.nuevos_calculos

def horario_termino(horario_inicio, tiempo_total):
    ''' calcula horario de termino en base a:
            horario_inicio --> (horas, minutos)
            tiempo_total --> horas
        retorna horario_termino
    '''
    hora_inicio = horario_inicio[0]
    minutos_inicio = horario_inicio[1]
    #print("Tiempo en horas:", tiempo_total)
    # HORA : MINUTOS + N dias  
    tiempo_total_minutos = 60 * tiempo_total
    #print("Tiempo en minutos:", tiempo_total_minutos)
    dias = tiempo_total_minutos/(1440)
    dias_entero = int(dias)
    #print("Cantidad de Días:", dias_entero)
    minutos_restantes = tiempo_total_minutos - dias_entero *1440
    #print("Minutos Restantes: ", minutos_restantes)
    horas = minutos_restantes/60
    horas_entero = int(horas)
    #print("Cantidad de Horas:", horas_entero)
    minutos_restantes = int(minutos_restantes - horas_entero * 60)
    #print("Minutos Restantes: ", minutos_restantes)
    hora_termino = hora_inicio + horas_entero
    minutos_termino = minutos_inicio + minutos_restantes
    dias_adicionales = dias_entero
    print("\nEl horario de inicio es ", str(int(hora_inicio))+":"
                                        +str(int(minutos_inicio)))
    print("El tiempo total es ", str(horas_entero) 
            + ":" + str(minutos_restantes)
            + " +" + str(dias_entero)+ " días" )
    if minutos_termino > 59:
        hora_termino = hora_termino + 1
        minutos_termino = minutos_termino - 60
    if hora_termino > 23:
        dias_adicionales = dias_adicionales + 1
        hora_termino = hora_termino - 24
    return (int(hora_termino), int(minutos_termino), dias_adicionales)

if __name__ == "__main__":
    horario_inicio = (6, 52)
    tiempo_total = 68.66
    print( horario_termino(horario_inicio, tiempo_total) )

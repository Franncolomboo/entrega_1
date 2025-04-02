import time
def calcularPuntos(kills,asistencias,muertes):
    puntos = (kills*3)- muertes + asistencias
    return puntos

def maxMVP(puntuacion):
    max = 0
    for jugador,puntos in puntuacion.items():
        if puntos > max:
            max = puntos
            maxJugador = jugador
    return maxJugador

def tablas_puntuacion(rounds):
    stats = {}
    puntuacion = {}
    mvp_jugador = {}
    i = 1
    for jugador in rounds[0].keys(): #Tomo los jugadores para inicializar el diccionario de cada jugador
        stats[jugador] = {"kills" : 0, "assists": 0, "deaths": 0, "puntos": 0} #Cada vez que lee un jugador lo agrego al diccionario y le inicializo las estadisticas
        puntuacion[jugador] = 0
        mvp_jugador[jugador] = 0
    for ronda in rounds:
        print(f"Ronda {i} :")
        i+=1
        puntaje_ronda = {}
        for jugador,estadisticas in ronda.items(): #Accedo a cada jugador y sus estadisticas
            # Guardo las estadisticas de cada jugador en variables para sumarlas al total
            kills = estadisticas["kills"]  
            asistencias = estadisticas["assists"]
            muertes = 1 if estadisticas["deaths"] else 0 #Si muertes es True, muertes = 1, sino muertes = 0
            puntos = calcularPuntos(kills,asistencias,muertes) #Calculo el puntaje de la ronda
            stats[jugador]["kills"] += kills
            stats[jugador]["assists"] += asistencias
            stats[jugador]["deaths"] += muertes
            puntaje_ronda[jugador] = puntos # Asigno el puntaje a cada jugador de la ronda
            puntuacion[jugador] += puntos # Sumo el puntaje a cada jugador al total de puntuacion
        jugador_mvp_ronda = maxMVP(puntaje_ronda) #Calculo el jugador MVP de la ronda
        mvp_jugador[jugador_mvp_ronda] += 1 #Sumo 1 al MVP de la ronda en su contador de MVP
        tabla_ordenada= sorted(puntuacion.items(), key=lambda item: item[1], reverse=True) #Ordeno la puntuacion de mayor a menor
        print(f' Jugador   |  Kills  |  Asistencias  |  Muertes  |  Puntos  |')#Imprimo la tabla
        for jugador,puntos_ronda in tabla_ordenada:
            print(f'{jugador}     |      {stats[jugador]["kills"]}    |       {stats[jugador]["assists"]}   |      {stats[jugador]["deaths"]}   |       {puntos_ronda} ')
            print("\n")
        print(f'Jugador MVP de la ronda: {jugador_mvp_ronda}')
        print("\n")
        time.sleep(1.5) #Pausa de 1.5 segundos antes de la siguiente ronda
    print(f'Ranking final: ') #Imprimo el ranking final
    print(f' Jugador   |  Kills  |  Asistencias  |  Muertes  |  MVPs  |  Puntos  |')
    for jugador,puntos_totales in tabla_ordenada:
        print(f'{jugador}     |       {stats[jugador]["kills"]}    |      {stats[jugador]["assists"]}     |      {stats[jugador]["deaths"]}   |   {mvp_jugador[jugador]}   |   {puntos_totales} ')
        print("\n")
        
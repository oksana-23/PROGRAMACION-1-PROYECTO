# Lista de preguntas con opciones
preguntas_formula = [
        "En que circuito se establecio el record de la vuelta mas rapida? a)Nurburgring b)Monza c)Monaco d)Silverstone",
        "Cuanto duró la carrera mas larga de la historia de Formula 1? a)3 dias b)3h 30m 25s c)4h 4m 39s d)4h 19m 22s",
        "Cuantos puntos vale el primer puesto cuando terminas la carrera? a)18 pts b)25 pts c)22 pts d)30 pts",
        "Que motor utiliza Red Bull en sus autos Formula 1 2024? a)PU106C Hybrid b)Mercedes-AMG F1 M15 c)TAG Heuer R.E.18 V6 Turbo d)Honda RBPTH002 ",
        "Cuantos mecanicos hay en una parada de pits? a)12 b)20 c)15 d)8",
        "En que pais se disputo el primer gran premio de la temporada 2020? a)Australia b)Alemania c)España d)Mexico",
        "Quien fue el campeon mundial de la formula 1 en 2019? a)Lewis Hamilton b)Fernando Alonso c)Niki Lauda d)Max Verstappen",
        "Cuantas veces fue campeon munial Juan Manuel Fangio? a)más de 5 b)3 c)ninguno d)5",
        "Cuantos muniales en Formula 1 tiene Max Verstappen? a)1 b)3 c)más de 3 d)2",
        "Cuantos pilotos corren en cada carrera?  a)20 b)15 c)10 d)22",
        "Cual es la marca con mas campeonatos de constructores? a)McLaren b)Mercedes c)Ferrari d)Red Bull",
        "En que año se fundo la Formula 1? a)1890 b)1954 c)1950 d)1960",
        "En que categoria compiten los de la Formula 1? a)Gt b)Turismo c)Nascar d)Monoplazas",
        "Cual fue el ultimo piloto en perder la vida? a)Jules Bianchi b)Niki Lauda c)Ayrton Senna d)David Ferrer",
        "Cual es el circuito con mas vueltas hechas? a)Hungaroring b)Red Bull Ring c)Spa-Francorchamps d)Silverstone",
        "De que color son los neumaticos de categoria Hard? a)Azul b)Rojo c)Amarillod)Rosa",
        "De que color son los neumaticos de categoria Soft?  a)Morado b)Blanco c)Naranja d)Amarillo",
        "De que color son los neumaticos de categoria Medium? a)Blanco b)Morado c)Rojo d)Azul",
        "Cual es el circuito mas famoso del mundo? a)Nurburgring b)Spa-Francorchamps c)Silverstone d)Monaco",
        "Quien tiene la vuelta mas rapida de Formula 1 en la hitoria? a)Max Verstappen b)Fernando Alonso c)Lewis Hamilton d)Niki Lauda",
        "Que piloto dijo la iconica frace 'El muro se movio'? a)Niki Lauda b)Fernando Alonso c)Aryton Senna d)David Ferrare",
        "Cuantas banderas hay en Formula 1? a)6 b)9 c)3 d)5",
        "Quienes son los pilotos con mas poseedores de titulos mundiales? a)Lewis Hamilton y Niki Lauda b) Max Verstappen y Juan Manuel Fangio c) Lewis Hamilton y Michael Schaumer d)Niki Lauda y Max Verstappen",
        "En que año entro McLaren en la competencia de Formula 1? a) 1996 b) 1955 c) 1976 d) 1992",
]

# Lista de respuestas correctas (solo la opción correcta)
respuestas_correctas = [
    "b",  # Monza 
    "c",  # 4h 4m 39s
    "b",  # 25 pts
    "d",  # Honda RBPTH002
    "b",  # 20
    "a",  # Australia
    "a",  # Lewis Hamilton
    "d",  # 5
    "b",  # 3
    "a",  # 20
    "c",  # Ferrari
    "c",  # 1950
    "d",  # Monoplaza
    "d",  # David Ferrer
    "b",  # Red Bull Ring
    "a",  # Azul
    "d",  # Amarillo
    "a",  # Blanco
    "d",  # Monaco
    "d"   # Niki Lauda
    "c",  # Aryton Senna
    "b",  # 9
    "c",  # Lewis Hamilton y Michael Schumacher
    "a",  # 1996
]

# Lista con las preguntas y respuestas correctas
preguntas_respuestas = [
    {"pregunta": preguntas_formula[i], "respuesta_correcta": respuestas_correctas[i]} 
    for i in range(len(preguntas_formula))
]

# Función para jugar al juego de trivia
def jugar_trivia():
    puntaje = 0
    print("¡Bienvenido al juego de trivia de Formula 1!\n")

    for i, item in enumerate(preguntas_respuestas):
        print(f"Pregunta {i + 1}: {item['pregunta']}")
        respuesta_usuario = input("Tu respuesta (a, b, c, d): ").lower()

        if respuesta_usuario == item['respuesta_correcta']:
            print("¡Correcto!\n")
            puntaje += 1
        else:
            print(f"Incorrecto. La respuesta correcta era '{item['respuesta_correcta']}'.\n")

    print(f"Tu puntaje final es: {puntaje}/{len(preguntas_respuestas)}")
    if puntaje == len(preguntas_respuestas):
        print("¡Felicidades! ¡Has acertado todas las preguntas!")
    elif puntaje > len(preguntas_respuestas) / 2:
        print("¡Buen trabajo! Has acertado la mayoría de las preguntas.")
    else:
        print("¡Sigue practicando! Puedes hacerlo mejor la próxima vez.")

# Llamada a la función para comenzar el juego
jugar_trivia()
# Lista de preguntas con opciones
preguntas_futbol = [
    "¿Qué selección ha ganado más Copas del Mundo? a) Brasil b) Alemania c) Italia d)",
    "¿En qué año Argentina ganó su primer Mundial de fútbol? a) 1974 b) 1978 c) 1986 d) 1990",
    "¿Cuál es el club con más títulos de la UEFA Champions League? a) AC Milan b) FC Barcelona c) Real Madrid d) Bayern Múnich",
    "¿Qué jugador fue transferido por una cifra récord de 222 millones de euros en 2017? a) Cristiano Ronaldo b) Neymar Jr. c) Lionel Messi d) Kylian Mbappé",
    "¿Qué equipo ganó la Premier League en la temporada 2015-2016? a) Manchester City b) Leicester City c) Chelsea d) Liverpool",
    "¿Cuál es el máximo goleador en la historia de la selección de Portugal? a) Eusébio b) Pauleta c) Cristiano Ronaldo d) Luís Figo",
    "¿Qué equipo es conocido como 'Los Diablos Rojos'? a) Manchester United b) AC Milan c) Independiente d) Bayern Múnich",
    "¿Quién ganó el Balón de Oro en 2021? a) Lionel Messi b) Robert Lewandowski c) Karim Benzema d) Cristiano Ronaldo",
    "¿Qué selección ganó la Eurocopa en 2004? a) Portugal b) Francia c) Italia d) Grecia",
    "¿Qué club argentino tiene más títulos de la Copa Libertadores? a) River Plate b) Boca Juniors c) Independiente d) Racing Club",
    "¿En qué estadio juega el FC Barcelona? a) Santiago Bernabéu b) Camp Nou c) Anfield d) Allianz Arena",
    "¿Qué entrenador ha ganado más Champions League como entrenador? a) Carlo Ancelotti b) Pep Guardiola c) Sir Alex Ferguson d) Zinedine Zidane",
    "¿Qué país ganó la Copa América 2021? a) Argentina b) Brasil c) Chile d) Uruguay",
    "¿Qué equipo español ha ganado más títulos de La Liga? a) Atlético Madrid b) Real Madrid c) Valencia d) FC Barcelona",
    "¿En qué equipo jugó Diego Maradona entre 1984 y 1991? a) FC Barcelona b) Sevilla FC c) SSC Napoli d) Boca Juniors",
    "¿Qué país fue anfitrión del Mundial de fútbol en 2014? a) Sudáfrica b) Brasil c) Alemania d) Rusia",
    "¿Qué selección tiene el récord de más victorias consecutivas en los Mundiales? a) Alemania b) Italia c) Brasil d) Francia",
    "¿Qué equipo de la Serie A ha ganado más títulos de liga? a) Juventus b) AC Milan c) Inter de Milán d) AS Roma",
    "¿Cuál es el club más antiguo del mundo aún en existencia? a) Sheffield FC b) Notts County c) Preston North End d) Aston Villa",
    "¿Qué selección ganó la primera Copa del Mundo en 1930? a) Argentina b) Brasil c) Italia d) Uruguay"
]

# Lista de respuestas correctas (solo la opción correcta)
respuestas_correctas = [
    "a",  # Brasil
    "b",  # 1978
    "c",  # Real Madrid
    "b",  # Neymar Jr.
    "b",  # Leicester City
    "c",  # Cristiano Ronaldo
    "a",  # Manchester United
    "a",  # Lionel Messi
    "d",  # Grecia
    "c",  # Independiente
    "b",  # Camp Nou
    "a",  # Carlo Ancelotti
    "a",  # Argentina
    "b",  # Real Madrid
    "c",  # SSC Napoli
    "b",  # Brasil
    "c",  # Brasil
    "a",  # Juventus
    "a",  # Sheffield FC
    "d"   # Uruguay
]

# Lista con las preguntas y respuestas correctas
preguntas_respuestas = [
    {"pregunta": preguntas_futbol[i], "respuesta_correcta": respuestas_correctas[i]} 
    for i in range(len(preguntas_futbol))
]

# Función para jugar al juego de trivia
def jugar_trivia():
    puntaje = 0
    print("¡Bienvenido al juego de trivia de fútbol!\n")

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

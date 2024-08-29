# Lista de preguntas con opciones
preguntas_autos=[
"¿Cuál es la marca de autos más antigua aún en funcionamiento? a) Ford, b) Mercedes-Benz, c) Fiat, d) Peugeot", 
"¿Qué marca produce el modelo Mustang? a) Chevrolet, b) Dodge, c) Ford, d) Nissan",
"¿En qué país se fundó Ferrari? a) Alemania, b) Italia, c) Francia, d) Estados Unidos",
"¿Cuál fue el primer auto producido en masa? a) Ford Model T, b) Mercedes-Benz 300SL, c) Chevrolet Corvette, d) Volkswagen Beetle",   
"¿Qué marca es conocida por su modelo 911? a) Ferrari, b) Porsche, c) Lamborghini, d) Aston Martin", 
"¿Cuál de estos autos es conocido como el auto del pueblo? a) Fiat 500, b) Citroën 2CV, c) Volkswagen Beetle, d) Mini Cooper"
"¿Qué marca produce el superdeportivo Veyron? a) Lamborghini, b) Ferrari, c) Bugatti, d) McLaren",  
"¿Qué auto eléctrico es producido por Tesla? a) Model X, b) Leaf, c) Bolt, d) i8" ,
"¿Qué marca fue fundada por Enzo Ferrari? a) Maserati, b) Ferrari, c) Alfa Romeo, d) Lamborghini",  
"¿Cuál es la marca de lujo de Toyota?  a) Acura, b) Infiniti, c) Lexus, d) Genesis",  
"¿Qué auto es conocido por sus puertas de ala de gaviota? a) DeLorean DMC-12, b) Lamborghini Aventador, c) Ferrari LaFerrari, d) Porsche 918 ", 
"¿En qué país se encuentra la sede de Volvo? a) Suecia, b) Alemania, c) Noruega, d) Estados Unidos ",
"¿Qué auto fue popularmente conocido como Escarabajo? a) Citroën DS, b) Fiat 500, c) Volkswagen Beetle, d) Mini Cooper",
"¿Qué marca produce el modelo Civic? a) Toyota, b) Nissan, c) Honda, d) Mazda ",
"¿Cuál fue el primer auto deportivo producido por Lamborghini? a) Miura, b) Countach, c) Diablo, d) 350 GT",
"¿Qué marca es conocida por sus autos híbridos Prius? a) Honda, b) Toyota, c) Nissan, d) Mitsubishi",
"¿En qué año se lanzó el primer Ford Mustang?  a) 1955, b) 1964, c) 1970, d) 1980 ",
"¿Qué marca de autos de lujo tiene un logo con un espíritu alado conocido como Espíritu del Éxtasis? a) Bentley, b) Rolls-Royce, c) Aston Martin, d) Jaguar ",
"¿Cuál es el auto deportivo más famoso de Chevrolet?  a) Camaro, b) Corvette, c) Impala, d) Malibu",  
"¿Qué marca alemana es conocida por el eslogan  Das Auto?  a) BMW, b) Audi, c) Volkswagen, d) Mercedes-Benz"  
]

# Lista de respuestas correctas
respuestas_correctas = [
    "d",  # Peugeot
    "c",  # Ford
    "b",  # Italia
    "a",  # Ford Model
    "b",  # Lamborghini
    "c",  # Volkswagen Beetle
    "c",  # Bugatti
    "a",  # Model X
    "b",  # Ferrari
    "c",  # Lexus 
    "a",  # DeLorean DMC-12
    "a",  # Suecia
    "c",  # Volkswagen Beetle
    "c",  # Honda
    "d",  # 350 GT
    "b",  # Toyota
    "b",  # 1964
    "b",  # Rolls-Royce
    "b",  # Corvette
    "c"   # Volkswagen
]

# Lista con las preguntas y respuestas correctas
preguntas_respuestas = [
    {"pregunta": preguntas_autos[i], "respuesta_correcta": respuestas_correctas[i]} 
    for i in range(len(preguntas_autos))
]

# Función para jugar al juego de trivia
def jugar_trivia():
    puntaje = 0
    print("¡Bienvenido al juego de trivia de autos!\n")

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
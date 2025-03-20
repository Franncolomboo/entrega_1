import random
import string
import sys
#CARACTERES INVALIDOS
numeros = string.digits
# Preguntas para el juego
questions = [
    "¿Qué función se usa para obtener la longitud de una cadena en Python?",
    "¿Cuál de las siguientes opciones es un número entero en Python?",
    "¿Cómo se solicita entrada del usuario en Python?",
    "¿Cuál de las siguientes expresiones es un comentario válido en Python?",
    "¿Cuál es el operador de comparación para verificar si dos valores son iguales?",
]

# Respuestas posibles para cada pregunta, en el mismo orden que las preguntas
answers = [
    ("size()", "len()", "length()", "count()"),
    ("3.14", "'42'", "10", "True"),
    ("input()", "scan()", "read()", "ask()"),
    (
        "// Esto es un comentario",
        "/* Esto es un comentario */",
        "-- Esto es un comentario",
        "# Esto es un comentario",
    ),
    ("=", "==", "!=", "==="),
]

# Índice de la respuesta correcta para cada pregunta, en el mismo orden que las preguntas
correct_answers_index = [1, 2, 0, 3, 1]

#Inicializamos sus puntos
puntos = 0

#Divido en tuplas y generar listas que no se repiten por el uso del random.sample()
questions_to_ask = random.sample(list(zip(questions,answers,correct_answers_index)),k=3)

# El usuario deberá contestar 3 preguntas 
for pregunta,respuestas,index_correcto in questions_to_ask:
    # Se selecciona una pregunta aleatoria
    print(pregunta)
    # Se muestra la pregunta y las respuestas posibles
    for i, answer in enumerate(respuestas):
        print(f"{i + 1}. {answer}")
    
    # El usuario tiene 2 intentos para responder correctamente
    for intento in range(2):
        user_answer = input("Respuesta: ")
        #Verifico que tipo de respuesta se ingreso (numero o caracter)
        if user_answer not in numeros :
            print("Respuesta Invalida")
            sys.exit(1)
        else:
            user_answer = int(user_answer)-1
        # Se verifica si la respuesta es correcta
        if user_answer == index_correcto:
            print("¡Correcto!")
            puntos += 1
            break
        else:
            print("Respuesta incorrecta")
            puntos -= 0.5
    else:
        # Si el usuario no responde correctamente después de 2 intentos,
        # se muestra la respuesta correcta
        print("Incorrecto. La respuesta correcta es:")
        print(respuestas[index_correcto])
print(f'Su puntuacion final es de {float(puntos)}/3.0')
def anagrama(palabra1,palabra2):
    """Verifica si dos palabras son anagramas"""
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    diccionario = {} # Creo un diccionario para almacenar las letras y sus repeticiones
    #Analizo la primera palabra
    for letra in palabra1:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    #Analizo la segunda palabra
    for letra in palabra2:
        if letra in diccionario:
            diccionario[letra] -= 1
        else:
            diccionario[letra] = -1
    #Verifico si las palabras son anagramas
    cant = 0 #Contador para verificar si coinciden las repeticiones entre las palabras
    for value in diccionario.values(): #Recorro el diccionario
        if value == 0: #Si las repeticiones son iguales por que la voy decrementando con la segunda palabra es igual a 0
            cant+=1 #Sumamos 1 al contador
    if cant == len(diccionario): #Si el contador es igual a la longitud del diccionario 
        print("Las palabras son anagramas") 
    else:
        print("Las palabras no son anagramas")  

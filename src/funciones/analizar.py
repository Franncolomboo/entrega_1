def analisis(texto):
    """Analiza el texto y cuenta las menciones de las palabras dadas en una lista """
    cantMusica = 0
    cantCharla = 0
    cantEntretenimiento = 0
    for renglon in texto:
        listaPalabras = renglon.split()
        for palabra in listaPalabras:
            palabra = palabra.lower()
            if palabra == "música":
                cantMusica = cantMusica + 1
            elif palabra == "charla":
                cantCharla = cantCharla + 1
            elif palabra == "entretenimiento":
                cantEntretenimiento = cantEntretenimiento + 1
    return print(f'Menciones de Musica: {cantMusica}\nMenciones de Charla: {cantCharla}\nMenciones de Entretenimiento: {cantEntretenimiento}')
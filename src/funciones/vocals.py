def vocales(texto):
    """"Imprime las oraciones que empiezan con una vocal""" 
    #Recibo el texto dividido en renglones 
    listaVocales=["a","e","i","o","u"]
    lista_zen = texto.splitlines("\n") # Vuelvo a dividir los renglones por palabras
    for i in lista_zen:    #Recorro la lista de renglones con la letra i 
        if len(i) >1:   #Si tiene mas de una palabra el renglon ,puedo verificar si la segunda palabra empieza con una vocal
            palabra = i.split()[1]; #me quedo con la segunda palabra del renglon
            if palabra.startswith(tuple(listaVocales)): #verifico si la segunda palabra empieza con una vocal
                print(i) #imprime el renglon 
    return
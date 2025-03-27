def renglonMasLargo(texto):
    max= -1
    for renglon in texto:
        if len(renglon)>max:
            max=len(renglon)
            maxTitle=renglon
    return maxTitle
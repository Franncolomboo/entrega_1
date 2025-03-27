def encontrarClave(texto, clave):
    textoDividio= texto.split(".")
    for oracion in textoDividio:
        if  clave in oracion:
            print(oracion)
    return
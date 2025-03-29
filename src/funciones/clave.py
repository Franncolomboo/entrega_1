def encontrarClave(texto, clave):
    """Devuelve las oraciones que contienen la clave"""
    textoDividio= texto.split(".")
    for oracion in textoDividio:
        if  clave in oracion:
            print(oracion)
    return
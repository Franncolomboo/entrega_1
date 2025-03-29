import string
def validar_caracteres(usuario):
    """"Valida que el usuario tenga al menos 5 caracteres"""
    if(len(usuario) >= 5):
        return True
    return False

def validar_numero(usuario):
    """Valida que el usuario tenga por lo menos un numero"""
    cantNum= 0
    for caracter in usuario:
        if caracter.isdigit():
            cantNum+=1
    if cantNum>0:
        return True
    return False

def validar_Mayus(usuario):
    """Valida que el usuario tenga por lo menos una letra mayuscula"""  
    cantMayus=0
    for caracter in usuario:
        if caracter.isupper():
            cantMayus+=1
    if cantMayus>0:
        return  True
    return False

def validar_letrasNum(usuario):
    """Valida que el usuario no tenga caracteres especiales"""
    for caracter in usuario:
        if caracter in string.punctuation:
            return False
    return True
        
def validar(usuario):
    """Invoca todas las funciones de validacion y si todas son True imprime que el usuario es valido"""
    if validar_caracteres(usuario) and validar_numero(usuario) and validar_Mayus(usuario) and validar_letrasNum(usuario):
        return print("Usuario valido!")
    return print("Usuario no valido!")
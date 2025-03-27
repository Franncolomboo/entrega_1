import string
def validar_caracteres(usuario):
    #Validar que la contraseña tenga al menos 5 caracteres
    if(len(usuario) >= 5):
        return True
    return False

def validar_numero(usuario):
    cantNum= 0
    for caracter in usuario:
        if caracter.isdigit():
            cantNum+=1
    if cantNum>0:
        return True
    return False

def validar_Mayus(usuario):
    cantMayus=0
    for caracter in usuario:
        if caracter.isupper():
            cantMayus+=1
    if cantMayus>0:
        return  True
    return False

def validar_letrasNum(usuario):
    for caracter in usuario:
        if caracter in string.punctuation:
            return False
    return True
        
def validar(usuario):
    if validar_caracteres(usuario) and validar_numero(usuario) and validar_Mayus(usuario) and validar_letrasNum(usuario):
        return print("Usuario valido!")
    return print("Usuario no valido!")
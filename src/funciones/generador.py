import random

def validarUsuario(usuario):
    """Valida que el usuario tenga menos de 15 caracteres"""
    if len(usuario)>15:
        return False
    return True

def generarStrRandom(longitud):
    """Genera una cadena aleatoria de longitud especificada que contiene letras y numeros"""
    import string
    caracteres = string.ascii_letters + string.digits
    clave = random.choices(caracteres, k=longitud)
    clave = ''.join(clave).upper()
    return clave

def codigoDescuento(usuario,fecha):
    """Genera un codigo de descuento aleatorio"""
    if (validarUsuario(usuario)):
        user = usuario.upper()
        date = fecha.replace("-","")
        cupon = user + "-" + date + "-" 
        logitudTotal= 28 #Descuento los - entre cada parte
        logitudTotal = logitudTotal - len(user) - len(date)
        cupon = cupon + generarStrRandom(logitudTotal)
        return print(f'Cupon generado! {cupon}') 
    else:
        return "USUARIO NO VALIDO"
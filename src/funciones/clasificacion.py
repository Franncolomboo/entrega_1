def clasificar(tiempo):
    """Clasifica la velocidad segun el tiempo en ms"""
    if tiempo < 200:
        return "Velocidad rapida"
    elif 200 < tiempo < 500:
        return "Velocidad media"
    else:
        return "Velocidad lenta"
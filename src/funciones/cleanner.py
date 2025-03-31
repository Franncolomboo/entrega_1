def eliminarNulos(texto):
    texto[:] = [c for c in texto if c is not None]
    texto[:] = [c for c in texto if c != "" and c != " "]
    return texto 
def limpiarEspacios(texto):
    """Elimina espacios de un texto"""
    texto = [elemento.strip() for elemento in texto] 
    return texto   

def capitalizar(cliente):
    """Capitaliza el nombre del cliente"""
    return cliente.lower().capitalize()
def limpieza(texto):
    """Limpia y estandardiza el texto para usarlos en un sistema de facturacion"""
    eliminarNulos(texto)
    texto =limpiarEspacios(texto)
    texto = [capitalizar(elemento) for elemento in texto]
    texto_sin_repetidos = list(set(texto))
    texto_sin_repetidos = sorted(texto_sin_repetidos)
    return texto_sin_repetidos
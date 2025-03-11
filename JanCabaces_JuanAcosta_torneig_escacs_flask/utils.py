import re

def validar_nom(nom):
    """Valida que el nom només contingui lletres i espais."""
    return bool(re.match(r'^[A-Za-zÀ-ÿ ]+$', nom))

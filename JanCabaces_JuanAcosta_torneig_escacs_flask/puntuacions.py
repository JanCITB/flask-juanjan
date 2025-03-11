# Modul per gestionar puntuacions
import json

PUNTUACIONS_FILE = "puntuacions.json"

def actualitzar_puntuacions(puntuacions, guanyador):
    """Actualitza les puntuacions del torneig."""
    if guanyador in puntuacions:
        puntuacions[guanyador] += 1
    else:
        puntuacions[guanyador] = 1
    desar_puntuacions_a_fitxer(puntuacions, PUNTUACIONS_FILE)

def calcular_ranquing(puntuacions):
    """Calcula el rànquing ordenat per puntuació."""
    return sorted(puntuacions.items(), key=lambda x: x[1], reverse=True)

def desar_puntuacions_a_fitxer(puntuacions, fitxer):
    """Desa les puntuacions en un fitxer JSON."""
    with open(fitxer, "w") as f:
        json.dump(puntuacions, f, indent=4)

def carregar_puntuacions_de_fitxer(fitxer):
    """Carrega les puntuacions des d'un fitxer JSON."""
    try:
        with open(fitxer, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
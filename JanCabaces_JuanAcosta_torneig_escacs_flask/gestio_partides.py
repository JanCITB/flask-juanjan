# Modul per gestionar partides
import json
import random

PARTIDES_FILE = "partides.json"

def generar_partides(participants, fitxer=PARTIDES_FILE):
    """Genera partides automàtiques entre participants."""
    random.shuffle(participants)
    partides = []
    
    # Si el nombre de participants és imparell, donem una ronda de descans
    if len(participants) % 2 == 1:
        partides.append((participants[-1], "bye"))  # L'últim participant descansa
    
    for i in range(0, len(participants) - 1, 2):
        partides.append((participants[i], participants[i+1]))
    
    desar_partides_a_fitxer(partides, fitxer)
    return partides

def desar_partides_a_fitxer(partides, fitxer):
    """Desa la llista de partides en un fitxer JSON."""
    with open(fitxer, "w") as f:
        json.dump(partides, f, indent=4)

def carregar_partides_de_fitxer(fitxer):
    """Carrega la llista de partides des d'un fitxer JSON."""
    try:
        with open(fitxer, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

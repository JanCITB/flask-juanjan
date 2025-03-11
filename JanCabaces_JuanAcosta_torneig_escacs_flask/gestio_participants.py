# Modul per gestionar participants
import json
import re

PARTICIPANTS_FILE = "participants.json"

def afegir_participant(nom):
    """Validar i afegir un participant a la llista."""
    if not re.match(r'^[A-Za-zÀ-ÿ ]+$', nom):
        return False  # Nom invàlid
    participants = carregar_participants_de_fitxer(PARTICIPANTS_FILE)
    if nom not in participants:
        participants.append(nom)
        desar_participants_a_fitxer(participants, PARTICIPANTS_FILE)
    return True

def desar_participants_a_fitxer(participants, fitxer):
    """Desa la llista de participants en un fitxer JSON."""
    with open(fitxer, "w") as f:
        json.dump(participants, f, indent=4)

def carregar_participants_de_fitxer(fitxer):
    """Carrega la llista de participants des d'un fitxer JSON."""
    try:
        with open(fitxer, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

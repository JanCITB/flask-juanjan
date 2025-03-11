from flask import Flask, render_template, request, redirect, url_for
from gestio_participants import afegir_participant, carregar_participants_de_fitxer
from gestio_partides import generar_partides, carregar_partides_de_fitxer
from puntuacions import carregar_puntuacions_de_fitxer, calcular_ranquing
from utils import validar_nom

PARTICIPANTS_FILE = "participants.json"
PARTIDES_FILE = "partides.json"
PUNTUACIONS_FILE = "puntuacions.json"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/participants', methods=['GET', 'POST'])
def participants():
    if request.method == 'POST':
        nom = request.form['nom']
        if validar_nom(nom):
            afegir_participant(nom)
    participants = carregar_participants_de_fitxer(PARTICIPANTS_FILE)
    return render_template('participants.html', participants=participants)

@app.route('/partides')
def partides():
    participants = carregar_participants_de_fitxer(PARTICIPANTS_FILE)
    partides = generar_partides(participants) if participants else []
    return render_template('partides.html', partides=partides)

@app.route('/puntuacions')
def puntuacions():
    puntuacions = carregar_puntuacions_de_fitxer(PUNTUACIONS_FILE)
    ranquing = calcular_ranquing(puntuacions)
    return render_template('puntuacions.html', ranquing=ranquing)

if __name__ == '__main__':
    app.run(debug=True)

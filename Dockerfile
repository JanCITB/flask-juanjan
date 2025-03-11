# Utilitzar una imatge base lleugera de Python 3.11
FROM python:3.11-slim

# Instal·lar les dependències del sistema necessàries, incloent el servidor SSH
RUN apt-get update && apt-get install -y \
    openssh-server \
    && rm -rf /var/lib/apt/lists/*  # Netejar la memòria cau per reduir la mida de la imatge

# Definir el directori de treball dins del contenidor
WORKDIR /app

# Copiar el fitxer de dependències de Python i instal·lar-les
COPY requisitos.txt .
RUN pip install --no-cache-dir -r requisitos.txt

# Copiar tots els fitxers del projecte al directori de treball del contenidor
COPY . .

# Configurar Gunicorn per executar l'aplicació Flask amb 4 processos de treballadors
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "JanCabaces_JuanAcosta_torneig_escacs_flask.app:app"]

# Exposar els ports necessaris: 
# 5000 per a l'aplicació Flask i 22 per a connexions SSH
EXPOSE 5000 22

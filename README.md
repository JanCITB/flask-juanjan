# Flask Docker Image

Aquest repositori conté un Dockerfile per construir una imatge Docker d'una aplicació Flask.

## 🚀 Passos per executar la imatge

### 1️⃣ Clonar el repositori:
```sh
git clone https://github.com/el_teu_usuari/flask-docker-image.git
cd flask-docker-image
```

### 2️⃣ Construir la imatge Docker:
```sh
docker build -t flask .
```

### 3️⃣ Executar el contenidor:
```sh
docker run -p 5000:5000 -p 22:22 flask
```

### 4️⃣ Accedir a l'aplicació Flask:
Obre el teu navegador i ves a:

🔗 [http://localhost:5000](http://localhost:5000)

---



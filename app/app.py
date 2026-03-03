from flask import Flask, jsonify
import psutil
import time

app = Flask(__name__)

# Heure de demarrage de l'application
START_TIME = time.time()

@app.route("/")
def home():
    return jsonify({"message": "CloudPulse fonctionne !", "status": "ok"})

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/metrics/system")
def metrics():
    # CPU
    cpu = psutil.cpu_percent(interval=0.1)

    # Mémoire
    memoire = psutil.virtual_memory()

    # Disque
    disque = psutil.disk_usage("/")

    # Temps depuis le démarrage
    uptime = round(time.time() - START_TIME, 2)

    return jsonify({
        "uptime_secondes": uptime,
        "cpu": {
            "pourcentage": cpu
        },
        "memoire": {
            "total_mb": round(memoire.total / 1024 / 1024, 2),
            "utilise_mb": round(memoire.used / 1024 / 1024, 2),
            "pourcentage": memoire.percent
        },
        "disque": {
            "total_gb": round(disque.total / 1024 / 1024 / 1024, 2),
            "utilise_gb": round(disque.used / 1024 / 1024 / 1024, 2),
            "pourcentage": disque.percent
        }
    })

if __name__ == "__main__":    
    app.run(host="0.0.0.0", port=5000)
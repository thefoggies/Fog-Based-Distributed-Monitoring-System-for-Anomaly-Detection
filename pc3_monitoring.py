from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL d’InfluxDB 1.8 : pas de token !!
INFLUX_URL = "http://localhost:8086/write?db=fog_data"

@app.route("/alert", methods=["POST"])
def alert():
    data = request.json
    print("PC1 → Alerte reçue :", data)

    # Conversion JSON → Line Protocol
    line = (
        "alerts,"
        f"device_id={data['device_id']} "
        f"temperature={float(data['temperature'])},"
        f"humidity={float(data['humidity'])},"
        f"status=\"{data['status']}\","
        f"timestamp={int(data['timestamp'])}"
    )

    # Envoi vers InfluxDB
    try:
        r = requests.post(INFLUX_URL, data=line)
        if r.status_code == 204:
            print("✔ Donnée enregistrée dans InfluxDB")
        else:
            print("❌ Erreur Influx :", r.text)
    except Exception as e:
        print("❌ Erreur réseau :", e)

    return jsonify({"saved": True})

if __name__ == "__main__":
    app.run(host="192.168.137.53", port=5002)
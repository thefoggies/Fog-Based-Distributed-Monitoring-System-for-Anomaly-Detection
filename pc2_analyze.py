from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# PC1 = 192.168.137.82
PC1_ALERT_URL = "http://192.168.137.53:5002/alert"

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    print("\nPC2 → reçu (cleaned) :", data)

    t = data.get("temperature")
    h = data.get("humidity")

    # Analyse
    if t is None or h is None:
        data["status"] = "invalid"
    elif t < -50 or t > 30 or h < 0 or h > 30:
        data["status"] = "anomaly"
    else:
        data["status"] = "normal"

    print("PC2 → analysé :", data)

    # Envoi au PC1
    try:
        response = requests.post(PC1_ALERT_URL, json=data)
        print("PC2 → envoyé à PC1 :", response.json())
    except Exception as e:
        print("❌ Erreur envoi PC1 :", e)

    return jsonify({"status": "analysis_done", "data": data})

if __name__ == "__main__":
    app.run(host="192.168.137.1", port=5001)

from flask import Flask, request, jsonify
import requests

PC2_URL = "http://192.168.137.1:5001/analyze"   # PC2 API REST

app = Flask(__name__)  

@app.route("/raw", methods=["POST"])
def receive_raw():
    data = request.json
    print("PC1 → reçu brut :", data)

    # Nettoyage
    if data["temperature"] < 0:
        data["temperature"] = 0
    if data["humidity"] < 0:
        data["humidity"] = 0

    print("PC1 → cleaned :", data)

    # Envoi à PC2
    response = requests.post(PC2_URL, json=data)
    print("PC1 → PC2 response :", response.json())

    return jsonify({"status": "cleaned_and_sent"})
    
app.run(host="192.168.137.203", port=5000)
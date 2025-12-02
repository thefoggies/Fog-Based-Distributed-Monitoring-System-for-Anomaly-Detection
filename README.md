# 🌩️ Fog-Based Distributed Monitoring System for Anomaly Detection

Ce projet implémente une architecture Fog Computing composée de **3 nœuds IoT distribués** permettant le nettoyage, l’analyse, la détection d’anomalies et la visualisation de données environnementales générées par Node-RED.

L’objectif : créer un pipeline intelligent, réactif et distribué pour simuler un système IoT industriel.


## 🚀 Architecture Globale


### 🔵 **PC1 — Cleaning Node**
- Reçoit les données brutes depuis Node-RED  
- Nettoie les données (filtrage, arrondi, ajout timestamp)  
- Envoie les données nettoyées à PC2  

📄 *Code : `pc1_cleaner.py` 


### 🟣 **PC2 — Anomaly Detection Node**
- Reçoit les données nettoyées depuis PC1  
- Analyse :
  - température hors limites  
  - humidité hors limites  
- Génère un statut :
  - `"normal"`
  - `"anomaly"`
- Envoie les alertes vers PC3 (via API Flask)

📄 *Code : `pc2_analyze.py`*

---

## 📊 PC3 - Visualisation — Grafana + InfluxDB
- Reçoit les alertes depuis PC2  
- Stocke les alertes dans **InfluxDB 1.8** 
- Affiche les graphiques dans **Grafana**  
- Sauvegarde les dashboards dans **Firebase Firestore**
- Base : `fog_data`
- Mesure : `alerts`
- Champs stockés :  
  - `temperature`  
  - `humidity`  
  - `status`  
  - `timestamp`  
- Dashboard : courbes temps réel des alertes IoT  


---

## ☁️ Sauvegarde Cloud — Firebase Firestore

Chaque dashboard Grafana exporté en JSON est :

✔ enregistré dans une collection Firestore :  
**`dashboards/exports`**

Cela permet :
- 🔒 un backup sécurisé  
- 🌍 un accès multi-machines  
- 🧪 une traçabilité historique des dashboards  

---

## 🛠️ Technologies Utilisées

- **Python Flask**
- **Node-RED** (simulateur IoT)
- **InfluxDB 1.8** (Docker)
- **Grafana**
- **Firebase Firestore**
- **HTTP REST APIs**
- **Fog Computing Architecture**




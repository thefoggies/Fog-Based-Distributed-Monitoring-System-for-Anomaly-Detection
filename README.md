# Fog-Based Distributed Monitoring System for Anomaly Detection

Ce projet met en place une architecture Fog Computing composée de trois nœuds permettant le nettoyage, l’analyse, la détection d’anomalies et la visualisation de données environnementales générées par Node-RED.  
L’objectif est de construire un pipeline IoT distribué, simple et efficace.

---

## 1. Architecture Générale

### 1.1 PC1 – Cleaning Node
- Reçoit les données brutes depuis Node-RED  
- Nettoie les données (filtrage, arrondi, timestamp)  
- Envoie les données nettoyées à PC2  

**Fichier :** `pc1_cleaner.py`

---

### 1.2 PC2 – Anomaly Detection Node
- Reçoit les données nettoyées depuis PC1  
- Détecte les anomalies sur la température et l’humidité  
- Produit un statut : `normal` ou `anomaly`  
- Transmet les alertes vers PC3 via API Flask  

**Fichier :** `pc2_analyze.py`

---

## 2. PC3 – Visualisation (Grafana + InfluxDB)

- Reçoit les alertes envoyées par PC2  
- Stocke les données dans InfluxDB (base : `fog_data`, mesure : `alerts`)  
- Affiche les graphiques dans Grafana  
- Exporte les dashboards en JSON  
- Sauvegarde des dashboards dans Firebase Firestore

**Champs stockés :**
- temperature  
- humidity  
- status  
- timestamp  

---

## 3. Sauvegarde Cloud (Firebase Firestore)

Les dashboards Grafana exportés sont enregistrés dans :

**Collection :** `dashboards/exports`

Cette sauvegarde permet un stockage sécurisé et une récupération facile du travail.

---

## 4. Technologies Utilisées

- Python (Flask)
- Node-RED
- InfluxDB 1.8  
- Grafana  
- Firebase Firestore  
- APIs REST  
- Architecture Fog Computing

---

Travail réalisé dans le cadre d’un projet étudiant d’architecture Fog Computing.

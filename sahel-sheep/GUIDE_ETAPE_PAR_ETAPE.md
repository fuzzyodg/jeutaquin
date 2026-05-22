# Guide de Mise en Œuvre : SahelSheep Connect 🐑

Ce guide vous accompagne étape par étape pour transformer cette idée en un prototype fonctionnel pour votre ferme.

## 1. Liste du Matériel (BOM) - Pour 1 prototype
*Budget estimé pour 1 collier + 1 base : ~50 000 CFA*

- **ESP32-S3 DevKit** (x2) : Le cerveau du système.
- **Module LoRa SX1278 (433MHz)** (x2) : Pour la communication longue portée.
- **Capteur de température DS18B20** (x1) : Étanche, pour la santé.
- **Accéléromètre ADXL345** (x1) : Pour l'activité.
- **Module GSM SIM800L** (x1) : Pour les SMS d'alerte (uniquement sur la base).
- **Lecteur RFID RC522** (x1) : Pour le comptage à l'entrée.
- **Batterie Li-ion 18650** + **TP4056** (Module de charge).
- **Petit panneau solaire (5V/100mA)**.

## 2. Étape par Étape

### Étape 1 : Le Collier (Suivi Santé)
1. **Montage** : Connectez le DS18B20 et l'ADXL345 à l'ESP32.
2. **Code** : Programmez l'ESP32 pour lire les données toutes les 30 min et les envoyer par LoRa.
3. **Optimisation** : Utilisez le mode "Deep Sleep" de l'ESP32 pour économiser la batterie. L'appareil ne doit s'allumer que quelques secondes pour mesurer et envoyer.

### Étape 2 : La Recherche d'Eau (Sonde de Résistivité)
1. **Principe** : Plantez deux tiges métalliques à 1m l'une de l'autre.
2. **Circuit** : Utilisez un pont diviseur de tension simple relié à une broche analogique de l'ESP32.
3. **Interprétation** :
    - Résistance très haute = Sol très sec.
    - Résistance baisse brusquement = Présence d'eau ou forte humidité.
    - *Astuce* : Comparez les mesures à différents endroits de la ferme pour trouver le point le plus humide.

### Étape 3 : La Passerelle (Gateway)
1. Placez l'antenne LoRa le plus haut possible (sur un poteau ou le toit de l'enclos).
2. Configurez le module GSM pour envoyer un SMS si :
    - `Température > 40°C`
    - `Mouvement == 0` pendant plus de 2 heures en journée.

### Étape 4 : L'Identification Économique
1. Fixez un **Tag RFID passif** (sous forme de boucle d'oreille) à chaque mouton.
2. Installez le lecteur à l'entrée de l'abreuvoir ou de l'enclos.
3. Dès qu'un mouton passe, son ID est enregistré. Si à 18h un ID manque à l'appel, la base envoie une alerte "Mouton manquant".

---

## 3. Évolutions Futures (Améliorations)

1. **Analyse de la Nutrition (IA légère)** :
   En analysant les mouvements de l'accéléromètre, on peut distinguer si le mouton "mange" ou s'il "marche". On peut ainsi calculer son temps de pâturage quotidien et savoir s'il est bien nourri.

2. **Détection de Chaleur** :
   Une augmentation légère de la température et une agitation accrue peuvent indiquer la période de reproduction pour optimiser l'élevage.

3. **Cartographie de l'Eau** :
   En déplaçant votre sonde et en enregistrant les points GPS sur votre téléphone, vous pouvez créer une carte thermique des zones humides de votre terrain pour choisir où creuser un forage.

4. **Boîtier Robuste** :
   Utilisez l'impression 3D ou des boîtes de dérivation électrique étanches pour protéger l'électronique des coups de cornes et de la poussière sahélienne.

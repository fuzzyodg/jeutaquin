# SahelSheep Connect 🐑🛰️

## Architecture Technique du Projet

Le projet est conçu pour une ferme en voie de développement (20-50 moutons) sans infrastructure réseau préexistante.

### 1. Les Équipements (Hardware)

#### A. Le Collier Connecté (Le "Node")
*Chaque mouton porte un collier léger contenant :*
- **Microcontrôleur** : ESP32-S3 (puissant et économe en énergie).
- **Communication** : Module LoRa (E32 ou RFM95) - Portée de 2 à 5 km sans Wi-Fi.
- **Capteurs** :
    - Accéléromètre (ADXL345) pour détecter l'activité (pâturage, repos, agitation anormale).
    - Capteur de température (DS18B20) placé contre la peau pour détecter la fièvre.
- **Énergie** : Batterie Li-ion 18650 rechargée par un petit panneau solaire flexible sur le collier.
- **Identification** : Tag RFID passif (type boucle d'oreille ou intégré au collier).

#### B. La Station de Base (La "Gateway")
*Placée à la ferme, elle centralise les données :*
- **Microcontrôleur** : ESP32.
- **Réception** : Antenne LoRa.
- **Transmission** : Module GSM (SIM800L) pour envoyer les alertes par SMS ou vers le web via la 2G.
- **Portique RFID** : Lecteur RFID longue portée (RC522 ou RDM6300) à l'entrée de l'enclos pour compter les têtes automatiquement.

#### C. Le Détecteur d'Eau (Sonde de Résistivité)
- Utilisation de deux barres de fer (électrodes) plantées à 1-2 mètres de distance.
- Mesure de la résistance du sol : un sol humide ou une nappe proche conduit mieux l'électricité qu'un sol sec.

### 2. Flux de Données

1. **Collecte** : Les colliers mesurent la santé toutes les 30 minutes.
2. **Transmission** : Les données sont envoyées par LoRa vers la Gateway (gratuit, pas besoin d'abonnement).
3. **Analyse** : La Gateway vérifie si la température dépasse 40°C ou si un mouton ne bouge plus.
4. **Alerte** : En cas de problème, un SMS est envoyé au berger via le module GSM.
5. **Visualisation** : Les données sont consultables sur l'application smartphone (maquette ci-jointe).

---

## Étude de Faisabilité

### Points Forts
- **Indépendance énergétique** : Le solaire permet une autonomie totale.
- **Coût réduit** : Le LoRa évite les frais de communication entre les animaux et la base.
- **Scalabilité** : On peut facilement ajouter des moutons (jusqu'à 100+).

### Défis à Relever
- **Robustesse** : Les colliers doivent résister à la poussière, aux chocs et aux frottements.
- **Précision thermique** : La laine du mouton isole beaucoup, le capteur doit être bien positionné.
- **Recherche d'eau** : La résistivité donne une indication d'humidité, pas une certitude de nappe profonde (nécessite des tests de calibration).

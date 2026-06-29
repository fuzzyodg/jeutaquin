# 🚀 Programme de Maîtrise : Anglais Technique pour l'Ingénieur Systèmes Avioniques

## 1. La Fiche de Route (Roadmap)
*Objectif : Passer de la compréhension générale à la conception de systèmes complexes.*

*   **Niveau 1 : Technical Literacy (L'Alphabétisation)**
    *   *Focus :* Vocabulaire des composants (Hardware/Software) et mesures de base.
*   **Niveau 2 : Functional Understanding (La Logique Système)**
    *   *Focus :* Lecture de schémas-blocs (**Block Diagrams**) et flux de données (**Data Flow**).
*   **Niveau 3 : Operational Proficiency (L'Exploitation)**
    *   *Focus :* Diagnostic de pannes (**Troubleshooting**) et rapports techniques.
*   **Niveau 4 : Advanced Engineering (La Maîtrise)**
    *   *Focus :* Spécifications (**Requirements**), Certification (**DO-178C**) et Revues de Design.

---

## 2. Les Fondamentaux : L'Avionique expliquée simplement
*Pour bien comprendre l'anglais technique, utilisons l'analogie du corps humain.*

1.  **The Nervous System (Le Bus de Données) :** Les nerfs transmettent l'information. Dans un avion, c'est le **Data Bus**. Au lieu de messages nerveux, on parle de **Signals**.
2.  **The Brain (Le Processeur/LRU) :** Le cerveau traite les données. Nous utilisons des **LRU (Line Replaceable Units)**, des calculateurs modulaires que l'on peut remplacer rapidement.
3.  **The Senses (Sensors) :** Vos yeux sont des capteurs. L'avion utilise des **Sensors** (ex: **Pitot Tubes** pour la vitesse, **Gyroscopes** pour l'orientation).
4.  **The Muscles (Actuators) :** Pour bouger une aile, le cerveau envoie un ordre aux muscles. L'avion envoie un signal à un **Actuator** (moteur électrique ou vérin hydraulique).

---

## 3. Programme Intensif sur 6 Semaines (Expertise Systèmes)

| Semaine | Thème | Concept Clé | Exercice |
| :--- | :--- | :--- | :--- |
| **1** | **System Architecture** | Inputs / Outputs / Feedback | Schématiser un système simple (ex: pilote automatique). |
| **2** | **Electronics & Power** | Voltage, Current, Circuit Protection | Analyser une **Datasheet** de composant. |
| **3** | **Data Communication** | Protocols (ARINC 429, Ethernet, AFDX) | Expliquer comment une donnée voyage du capteur à l'écran. |
| **4** | **Navigation Systems** | GNSS, ILS, Inertial Navigation | Simuler un rapport de test sur un récepteur GPS. |
| **5** | **Troubleshooting** | Fault isolation, Error codes, BITE | Rédiger un guide de diagnostic pour une panne radio. |
| **6** | **Certification & Quality** | Standards (DO-178C), Compliance | Écrire 5 exigences techniques avec "**The system shall...**". |

---

## 4. Focus Expert : L'Architecture IMA (Integrated Modular Avionics)
*C'est le cœur de l'aviation moderne (A380, A350, Boeing 787).*

*   **Définition :** Au lieu d'avoir un ordinateur par fonction, on utilise une plateforme partagée. C'est l'informatique "cloud" appliquée à l'avion.
*   **Redundancy (Redondance) :** On multiplie les systèmes pour éviter le "Single Point of Failure" (point de défaillance unique).
*   **Segregation (Ségrégation) :** On s'isole les logiciels pour qu'un bug mineur ne perturbe pas le pilotage (**Partitioning**).

---

## 5. Projets Pratiques suggérés
1.  **Manual Analysis :** Prenez un manuel de maintenance (AMM) et listez les verbes d'action (Check, Inspect, Tighten, Disconnect).
2.  **Requirement Writing :** Prenez un système simple (une cafetière) et rédigez ses spécifications en anglais comme s'il s'agissait d'un système critique.
3.  **Fault Reporting :** Simulez un appel radio ou un email décrivant une panne complexe survenue en plein vol.

---

## 6. Guide de Révision Rapide (Vocabulaire Essentiel)
*   **Power Supply :** Alimentation.
*   **Wiring Harness :** Faisceau de câbles.
*   **Shielding :** Blindage (contre les interférences).
*   **Reliability :** Fiabilité.
*   **Real-time :** Temps réel.
*   **Embedded :** Embarqué.
*   **Failure :** Défaillance.
*   **Warning / Caution / Advisory :** Niveaux d'alerte (Rouge / Ambre / Cyan).

# AGENTS.md — A'kadi Restaurant

> Ce fichier guide Jules dans le développement du site web du restaurant
> **A'kadi**, un restaurant tradi-moderne burkinabè à Ouagadougou.
> Lis-le entièrement avant de commencer toute tâche.

---

## 🍲 Project Context

Site web vitrine + fonctionnel pour **A'kadi**, restaurant burkinabè
alliant cuisine traditionnelle et esthétique contemporaine.

- **Type** : Site web multi-pages, HTML/CSS/JS vanilla (pas de framework)
- **Public** : Clients à Ouagadougou et visiteurs internationaux
- **Langue** : Français (langue principale du site)
- **Devise** : Francs CFA (XOF) — toujours afficher les prix en CFA
- **Ton visuel** : Tradi-moderne — chaleureux, élégant, inspiré du Bogolan
  et des couleurs du Sahel (or, terre de latérite, nuit de brousse)

---

## 📁 Architecture des fichiers

```
/
├── index.html              → Page d'accueil (hero, highlights, CTA) et petite galerie photo des plats et du cadre du resto
├── menu.html               → Menu complet avec catégories et prix et filtres des plats
|---apropos.html            histoire du resto comment il est ne et presentation de notre equipe et de nos valeurs
├── evenement.html           → tous les evenements que nous organisons au sein de notre cadre : soiree karaoke et brunchs
├── contact.html       → Page de formulaire de reservation et de confirmation commande/réservation/livraison
│
├── css/
│   └── pages/
        |--common.css
│       ├── index.css
│       ├── menu.css
│       ├── apropos.css
│       ├── evenement.css
│       └── contact.css
│
├── js/
│   ├─script.js
```

---

## 🎨 Design System

### Palette de couleurs (CSS variables dans main.css)
```css
--oro: #C8922A;          /* Or sahélien — couleur principale */
--terre: #8B4513;        /* Terre de latérite */
--rouge: #C0392B;        /* Rouge feu */
--sable: #F5E6C8;        /* Sable du Sahel — texte principal */
--nuit: #1A0F05;         /* Nuit de brousse — fond principal */
--cendre: #2C1A0E;       /* Cendre — fond cartes */
--fauve: #D4832A;        /* Fauve — accent chaud */
--vert-kola: #4A6741;    /* Vert kola — accent nature */
--blanc-creme: #FAF3E0;  /* Blanc crème — titres */
```

### Typographies
- **Cinzel** (Google Fonts) → Titres principaux, logo, prix
- **Cormorant Garamond** (Google Fonts) → Sous-titres, citations, italiques
- **Raleway** (Google Fonts) → Corps de texte, labels, boutons

### Motifs décoratifs
- Motif Bogolan en SVG (pattern géométrique noir et or)
- Flammes CSS animées (animation `flicker`)
- Braises flottantes (particules CSS animées, animation `float-ember`)
- Losanges dorés pulsants comme séparateurs

---

## ⚙️ Standards de code

### HTML
- Sémantique stricte : `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>`
- Un seul `<h1>` par page
- Attributs `alt` obligatoires sur toutes les images
- Attributs `aria-label` sur tous les boutons sans texte visible
- Charset UTF-8, viewport meta tag sur chaque page
- Inclure les Google Fonts via `<link>` dans le `<head>`

### CSS
- Toutes les couleurs via les variables CSS de `main.css`, jamais en dur
- Mobile-first : commencer par les styles mobile, puis `@media (min-width:…)`
- Pas de `!important` sauf exception justifiée en commentaire
- Nommage BEM pour les classes : `.plat-card`, `.plat-card__titre`, `.plat-card--featured`
- Les animations complexes dans `animations.css` uniquement

### JavaScript
- Vanilla JS pur — pas de jQuery, pas de frameworks
- `'use strict'` en tête de chaque fichier JS
- Sélecteurs via `document.querySelector` / `querySelectorAll`
- Événements via `addEventListener`, jamais d'attributs `onclick` dans le HTML
- Données du menu chargées depuis `data/menu.json` via `fetch()`
- Pas de `var` — utiliser `const` et `let` uniquement
- Commenter les fonctions complexes en français

---

## 🛒 Fonctionnalités clés

### Menu en ligne (`menu.html` + `menu.js`)
- Chargement des plats depuis `data/menu.json`
- Filtres par catégorie : Entrées, Plats traditionnels, Grillades, Boissons, Desserts
- Affichage : nom, description, prix en CFA, badge (Signature / Chef / Populaire)
- Bouton "Ajouter au panier" sur chaque plat
- Compteur panier visible dans la navigation

### Réservation de table (`reservation.html` + `reservation.js`)
- Champs : Nom complet, Téléphone (+226), Date, Heure, Nombre de personnes, Message
- Validation côté client avant envoi (champs requis, format téléphone burkinabè)
- Confirmation visuelle après soumission (pas de backend requis pour l'instant — simuler)
- Créneaux horaires disponibles : 12h00–14h30 (déjeuner), 19h00–22h00 (dîner)

### Commande / Livraison (`commande.html` + `commande.js`)
- Panier persistant via `localStorage`
- Calcul automatique du total en CFA
- Frais de livraison fixes : 500 CFA (Ouagadougou intramuros)
- Champ adresse de livraison obligatoire
- Bouton "Passer la commande" → redirige vers `contact.html`

### Paiement en ligne (`paiement.html` + `paiement.js`)
- Intégration **CinetPay** (provider de paiement mobile money Afrique de l'Ouest)
- Modes acceptés : Orange Money BF, Moov Money BF, Carte bancaire
- Afficher le récapitulatif de commande avant paiement
- Page `contact.html` après paiement réussi
- Ne jamais logger les données de carte ou de paiement en console

### Galerie photos (`galerie.html` + `galerie.js`)
- Filtres : Plats, Ambiance, Équipe, Événements
- Lightbox au clic sur chaque photo (vanilla JS, pas de librairie externe)
- Lazy loading des images via `loading="lazy"`

---

## 📱 Responsive

- **Mobile** : 320px–767px → navigation burger, cartes en colonne unique
- **Tablette** : 768px–1023px → grille 2 colonnes
- **Desktop** : 1024px+ → grille 3–4 colonnes, layout complet

Le site doit être parfaitement utilisable sur mobile (majorité des utilisateurs
à Ouagadougou naviguent sur smartphone).

---

## 🚫 Do NOT

- Ne jamais utiliser de framework JS (React, Vue, Angular…)
- Ne jamais modifier `data/menu.json` sans le signaler explicitement
- Ne jamais utiliser `console.log` dans le code de production
- Ne jamais changer la palette de couleurs définie dans `main.css`
- Ne jamais utiliser de CDN autre que Google Fonts et éventuellement
  la librairie officielle CinetPay
- Ne jamais stocker de données de paiement sensibles en `localStorage`
- Ne pas créer de nouveaux fichiers CSS en dehors de la structure définie

---

## ✅ Definition of Done

Une tâche est considérée terminée quand :
- Le code fonctionne sur Chrome, Firefox et Safari mobile
- La page est responsive (mobile + desktop)
- Aucune erreur dans la console du navigateur
- Les variables CSS sont utilisées (pas de couleurs hardcodées)
- Le code est commenté en français pour les fonctions complexes

---

## ❓ If Stuck

Si tu rencontres une ambiguïté sur :
- **Les prix** → ne pas inventer, mettre un placeholder `XXXX CFA`
- **Les images** → utiliser des placeholders `assets/images/placeholder.jpg`
- **L'intégration CinetPay** → pause et pose une question, ne pas improviser
- **La structure des données** → respecter scrupuleusement le format de `sript.json`

---

*Dernière mise à jour : Mai 2025 — Projet Wend Yam*

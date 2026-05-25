import json

slides_data = [
    {
        "title": "Accueil - Hero & Identité",
        "image": "screenshots/accueil_hero.png",
        "code_html": '<section class="hero">\n  <div class="hero__slides">\n    <div class="hero__slide active">...</div>\n  </div>\n  <div class="hero__content">\n    <h1>L\'authenticité...</h1>\n  </div>\n</section>',
        "code_css": '.hero__slide {\n  opacity: 0;\n  transition: opacity 1s;\n}\n.hero__slide.active {\n  opacity: 1;\n}',
        "code_js": 'function goTo(idx) {\n  slides[current].classList.remove(\'active\');\n  current = idx % slides.length;\n  slides[current].classList.add(\'active\');\n}',
        "explanation": "La bannière d'accueil utilise un système de diapositives (slides) géré en JavaScript. Le CSS assure une transition fluide par opacité (fade-in) entre les images pour un rendu luxueux et moderne."
    },
    {
        "title": "Accueil - Spécialités Animées",
        "image": "screenshots/accueil_specialties.png",
        "code_html": '<article class="specialty-card specialty-card--slider active">\n  <img src="zamnin.jpeg" />\n  <div class="specialty-card__content">\n    <h3>Zamne</h3>\n  </div>\n</article>',
        "code_css": '.specialty-card {\n  transition: transform 0.8s, opacity 0.8s;\n}\n.specialty-card.exit {\n  transform: translateX(-100%);\n}',
        "code_js": 'slides[current].classList.add(\'exit\');\nsetTimeout(() => {\n  slides[prev].classList.remove(\'exit\');\n}, 800);',
        "explanation": "Le curseur des spécialités combine des classes d'état (active, exit) pour créer un mouvement de glissement élégant. L'utilisation de setTimeout permet de synchroniser le retrait des anciennes cartes."
    },
    {
        "title": "Accueil - Avis Clients",
        "image": "screenshots/accueil_reviews.png",
        "code_html": '<div class="review-card">\n  <div class="review-card__stars">★★★★★</div>\n  <p>...</p>\n</div>',
        "code_css": '.review-card {\n  background: var(--color-white);\n  border-radius: var(--radius-lg);\n  box-shadow: var(--shadow-sm);\n}',
        "explanation": "La section des avis clients utilise une grille responsive pour présenter les témoignages. Les étoiles sont gérées par des caractères Unicode et stylisées en doré pour rester cohérent avec le thème."
    },
    {
        "title": "Accueil - Producteurs Locaux",
        "image": "screenshots/accueil_map.png",
        "code_html": '<div class="producer-markers">\n  <div class="producer-marker" style="top: 20%; left: 30%;">\n    <div class="producer-marker__dot"></div>\n  </div>\n</div>',
        "code_css": '.producer-marker__dot {\n  width: 12px; height: 12px;\n  background: var(--color-primary);\n  border-radius: 50%;\n  animation: pulse 2s infinite;\n}',
        "explanation": "Une carte interactive (visuelle) localise les producteurs. Des marqueurs positionnés de manière absolue en CSS avec des animations de pulsation soulignent l'engagement local du restaurant."
    },
    {
        "title": "Menu - Bandeau Défilant Infini",
        "image": "screenshots/menu_infinite.png",
        "code_html": '<div class="infinite-scroll__track">\n  <!-- Groupe 1 -->\n  <div class="food-card">...</div>\n  <!-- Groupe 2 (Copie) -->\n  <div class="food-card">...</div>\n</div>',
        "code_css": '@keyframes scroll {\n  0% { transform: translateX(0); }\n  100% { transform: translateX(-50%); }\n}\n.infinite-scroll__track {\n  animation: scroll 40s linear infinite;\n}',
        "explanation": "Le défilement infini est réalisé en CSS pur. En doublant les éléments dans le HTML et en déplaçant le conteneur de 50%, on crée une boucle parfaite sans interruption visuelle."
    },
    {
        "title": "Menu - Filtrage Dynamique",
        "image": "screenshots/menu_list.png",
        "code_html": '<button class="filter__btn" data-category="grillades">Grillades</button>\n<div class="menu-item" data-category="grillades">...</div>',
        "code_js": 'items.forEach(item => {\n  const catOk = cat === \'all\' || itemCat === cat;\n  item.classList.toggle(\'hidden\', !catOk);\n});',
        "code_css": '.hidden {\n  display: none;\n  opacity: 0;\n}',
        "explanation": "Le filtrage utilise des attributs de données (data-attributes). Le JavaScript masque ou affiche les plats instantanément sans recharger la page, offrant une navigation fluide aux clients."
    },
    {
        "title": "À propos - Histoire Familiale",
        "image": "screenshots/apropos_history.png",
        "code_html": '<div class="about-hero__content">\n  <h2>Une Passion Culinaire</h2>\n  <p>Fondé avec la conviction...</p>\n</div>',
        "code_css": '.about-hero {\n  display: grid;\n  grid-template-columns: 1fr 1fr;\n  gap: var(--spacing-xl);\n}',
        "explanation": "La page À Propos utilise une grille à deux colonnes sur desktop pour équilibrer le texte narratif et les images de l'équipe, assurant une lecture agréable de l'histoire du restaurant."
    },
    {
        "title": "À propos - Valeurs & Engagement",
        "image": "screenshots/apropos_values.png",
        "code_html": '<div class="value-card">\n  <div class="value-card__icon">🌱</div>\n  <h3>Nutrition Saine</h3>\n</div>',
        "code_css": '.value-card:hover {\n  transform: translateY(-5px);\n  box-shadow: var(--shadow-md);\n}',
        "explanation": "Les valeurs sont présentées dans des cartes auto-descriptives. Des micro-interactions (hover) renforcent l'engagement de l'utilisateur tout en soulignant les piliers éthiques d'A'kadi."
    },
    {
        "title": "À propos - L'Histoire de Maman A'kadi",
        "image": "screenshots/apropos_story.png",
        "code_html": '<section class="story">\n  <h2>L\'Histoire de Maman A\'kadi</h2>\n  <p>Tout a commencé par...</p>\n</section>',
        "code_css": '.story {\n  background: linear-gradient(135deg, #e7e1d1, #b77212);\n  padding: 4rem 0;\n}',
        "explanation": "Le design narratif utilise des dégradés de couleurs inspirés du Sahel. La mise en page sémantique (section, article) assure une bonne accessibilité et un récit immersif."
    },
    {
        "title": "Événements - Calendrier & Grille",
        "image": "screenshots/evenement_list.png",
        "code_html": '<div class="event-card">\n  <img src="ldc.jpg" />\n  <span class="event-card__date">Mai 2026</span>\n</div>',
        "code_css": '.event-card__image {\n  position: relative;\n  overflow: hidden;\n}',
        "explanation": "Les événements sont organisés dans une grille flexible. Chaque carte possède un badge de date positionné de manière absolue, garantissant une lisibilité immédiate des échéances."
    },
    {
        "title": "Événements - Modales d'Inscription",
        "image": "screenshots/evenement_hero.png",
        "code_html": '<div id="event-modal" class="modal">\n  <div class="modal__content">...</div>\n</div>',
        "code_js": 'function openModal(eventName) {\n  modal.classList.add(\'active\');\n  document.body.style.overflow = \'hidden\';\n}',
        "code_css": '.modal.active {\n  opacity: 1;\n  visibility: visible;\n}',
        "explanation": "La gestion des événements utilise des fenêtres modales. Le JavaScript contrôle l'état d'affichage et verrouille le défilement du corps de la page pour une meilleure UX lors de la saisie."
    },
    {
        "title": "Contact - Logique de Réservation",
        "image": "screenshots/contact_form.png",
        "code_html": '<input type="radio" name="mode" value="livraison" />\n<div id="address-block" style="display:none">...</div>',
        "code_js": 'radio.addEventListener(\'change\', () => {\n  const isDelivery = radio.value === \'livraison\';\n  addrBlock.style.display = isDelivery ? \'block\' : \'none\';\n});',
        "explanation": "Le formulaire est intelligent : il affiche dynamiquement les champs selon le mode choisi (livraison ou sur place). Le JavaScript gère l'affichage conditionnel pour simplifier le parcours client."
    },
    {
        "title": "Gestion du Panier - LocalStorage",
        "image": "screenshots/accueil_hero.png",
        "code_js": 'let items = JSON.parse(localStorage.getItem(\'akadi_cart\') || \'[]\');\nfunction save() {\n  localStorage.setItem(\'akadi_cart\', JSON.stringify(items));\n}',
        "explanation": "Le panier est persistant grâce à l'API LocalStorage. Les choix du client sont sauvegardés localement, permettant une expérience continue à travers toutes les pages du site."
    },
    {
        "title": "Design System - Variables CSS",
        "image": "screenshots/accueil_features.png",
        "code_css": ':root {\n  --color-primary: #6f240a;\n  --color-gold: #fed65b;\n  --pattern-bogolan: url("...");\n}\n[data-theme="dark"] {\n  --color-bg: #12100e;\n}',
        "explanation": "L'utilisation de variables CSS centralisées permet de maintenir une cohérence visuelle parfaite. Le passage au mode sombre (Sahara Luxury) se fait dynamiquement via l'attribut data-theme."
    }
]

with open('slides_content.json', 'w', encoding='utf-8') as f:
    json.dump(slides_data, f, ensure_ascii=False, indent=2)

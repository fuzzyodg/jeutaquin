/* ============================================
   A'KADI - Script principal
   ============================================ */

/* ---- Slideshow (accueil) ---- */
(function () {
  const slides = document.querySelectorAll('.hero__slide');
  const dots   = document.querySelectorAll('.hero__dot');
  if (!slides.length) return;

  let current = 0;
  function goTo(idx) {
    slides[current].classList.remove('active');
    if (dots[current]) dots[current].classList.remove('active');
    current = (idx + slides.length) % slides.length;
    slides[current].classList.add('active');
    if (dots[current]) dots[current].classList.add('active');
  }
  dots.forEach((d, i) => d.addEventListener('click', () => goTo(i)));
  goTo(0);
  setInterval(() => goTo(current + 1), 4000);
})();

/* ---- Theme Toggle (Mode Clair/Sombre) ---- */
(function () {
  const themeToggle = document.getElementById('theme-toggle');
  const themeIcon = document.getElementById('theme-icon');
  const htmlElement = document.documentElement;

  // Charger le thème sauvegardé
  const savedTheme = localStorage.getItem('akadi_theme') || 'light';
  htmlElement.setAttribute('data-theme', savedTheme);
  updateIcon(savedTheme);

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const currentTheme = htmlElement.getAttribute('data-theme');
      const newTheme = currentTheme === 'light' ? 'dark' : 'light';

      htmlElement.setAttribute('data-theme', newTheme);
      localStorage.setItem('akadi_theme', newTheme);
      updateIcon(newTheme);
    });
  }

  function updateIcon(theme) {
    if (!themeIcon) return;
    // Si vous voulez changer l'image selon le mode, démentez ici
    // themeIcon.src = theme === 'dark' ? 'lampe_on.png' : 'lampe.png';
  }
})();

/* ---- Burger / Nav mobile ---- */
(function () {
  const burger  = document.querySelector('.burger');
  const navMob  = document.querySelector('.nav-mobile');
  const overlay = document.querySelector('.nav-overlay');
  if (!burger) return;

  function close() {
    burger.classList.remove('active');
    navMob.classList.remove('active');
    overlay.classList.remove('active');
  }
  burger.addEventListener('click', () => {
    burger.classList.toggle('active');
    navMob.classList.toggle('active');
    overlay.classList.toggle('active');
  });
  overlay.addEventListener('click', close);
  document.querySelectorAll('.nav-mobile__link').forEach(l => l.addEventListener('click', close));
})();

/* ---- Scroll infini tactile ---- */
(function () {
  const track = document.querySelector('.infinite-scroll__track');
  if (!track) return;

  let isDown = false;
  let startX;
  let scrollLeft;

  // Pour mobile: mettre l'animation en pause quand on touche
  track.addEventListener('touchstart', (e) => {
    isDown = true;
    track.style.animationPlayState = 'paused';
    startX = e.touches[0].pageX - track.offsetLeft;
    scrollLeft = track.scrollLeft;
  }, { passive: true });

  track.addEventListener('touchend', () => {
    isDown = false;
    track.style.animationPlayState = 'running';
  });

  track.addEventListener('touchmove', (e) => {
    if (!isDown) return;
    // On laisse le scroll naturel ou on peut implémenter un drag manuel
    // Mais avec l'animation active, le scrollLeft manuel peut être capricieux.
    // Pour une meilleure expérience mobile, on garde l'animation automatique et on permet de "freiner/stopper" au toucher.
  }, { passive: true });

  // Optionnel: Drag à la souris aussi sur desktop
  track.addEventListener('mousedown', (e) => {
    isDown = true;
    track.style.animationPlayState = 'paused';
    startX = e.pageX - track.offsetLeft;
    scrollLeft = track.scrollLeft;
  });
  track.addEventListener('mouseleave', () => {
    isDown = false;
    track.style.animationPlayState = 'running';
  });
  track.addEventListener('mouseup', () => {
    isDown = false;
    track.style.animationPlayState = 'running';
  });
  track.addEventListener('mousemove', (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - track.offsetLeft;
    const walk = (x - startX) * 2;
    track.scrollLeft = scrollLeft - walk;
  });
})();

/* ---- Filtre menu ---- */
(function () {
  const btns  = document.querySelectorAll('.filter__btn');
  const items = document.querySelectorAll('.menu-item[data-category]');
  const checks = document.querySelectorAll('.allergen-checkbox');
  if (!btns.length) return;

  function applyFilters() {
    const activeBtn = document.querySelector('.filter__btn.active');
    const cat = activeBtn ? activeBtn.dataset.category : 'all';
    const blocked = Array.from(checks).filter(c => c.checked).map(c => c.value);

    items.forEach(item => {
      const itemCat = (item.dataset.category || '').toLowerCase().trim();
      const itemAllergens = (item.dataset.allergens || '').toLowerCase();
      const catOk = cat === 'all' || itemCat.includes(cat.toLowerCase()) || cat.toLowerCase().includes(itemCat);
      const allergenOk = blocked.length === 0 || !blocked.some(b => itemAllergens.includes(b));
      item.classList.toggle('hidden', !(catOk && allergenOk));
    });
  }

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      applyFilters();
    });
  });
  checks.forEach(c => c.addEventListener('change', applyFilters));
})();

/* ---- Modal événements ---- */
(function () {
  const modal = document.getElementById('event-modal');
  if (!modal) return;
  const closeBtn = modal.querySelector('.modal__close');
  const interestBtns = document.querySelectorAll('.event-card .btn--primary');

  function openModal(eventName) {
    modal.querySelector('input[name="event"]').value = eventName || '';
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
  }
  function closeModal() {
    modal.classList.remove('active');
    document.body.style.overflow = '';
  }

  interestBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const title = btn.closest('.event-card')?.querySelector('.event-card__title')?.textContent || '';
      openModal(title);
    });
  });
  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', e => { if (e.target === modal) closeModal(); });

  const form = modal.querySelector('.modal__form');
  if (form) {
    form.addEventListener('submit', e => {
      e.preventDefault();
      closeModal();
      showToast('Votre intérêt a bien été enregistré !');
    });
  }
})();

/* ---- Formulaire réservation (contact) ---- */
(function () {
  const form = document.getElementById('reservation-form');
  if (!form) return;
  // La gestion du formulaire est maintenant faite dans contact.html
  // Cette fonction reste ici au cas où on aurait besoin, mais elle ne fait rien
})();

/* ============================================
   PANIER DÉPLIABLE
   ============================================ */
const Cart = (function () {
  let items = JSON.parse(localStorage.getItem('akadi_cart') || '[]');

  function save() { localStorage.setItem('akadi_cart', JSON.stringify(items)); }

  function add(name, price, imgSrc) {
    const existing = items.find(i => i.name === name);
    if (existing) { existing.qty++; }
    else { items.push({ name, price, imgSrc, qty: 1 }); }
    save(); render(); showToast(`${name} ajouté au panier`);
  }

  function remove(name) {
    items = items.filter(i => i.name !== name);
    save(); render();
  }

  function changeQty(name, delta) {
    const item = items.find(i => i.name === name);
    if (!item) return;
    item.qty += delta;
    if (item.qty <= 0) remove(name);
    else { save(); render(); }
  }

  function clear() { items = []; save(); render(); }

  function total() { return items.reduce((sum, i) => sum + i.price * i.qty, 0); }
  function count() { return items.reduce((sum, i) => sum + i.qty, 0); }

  function render() {
    const body   = document.getElementById('cart-body');
    const badge  = document.getElementById('cart-count');
    const totalEl = document.getElementById('cart-total');
    if (!body) return;

    const n = count();
    if (badge) {
      badge.textContent = n;
      badge.classList.toggle('visible', n > 0);
    }
    if (totalEl) totalEl.textContent = total().toLocaleString('fr-FR') + ' CFA';

    if (items.length === 0) {
      body.innerHTML = `
        <div class="cart-empty">
          <div class="cart-empty__icon">🛒</div>
          <p>Votre panier est vide</p>
          <p style="font-size:0.85rem;margin-top:8px;color:#bbb;">Ajoutez des plats depuis le menu</p>
        </div>`;
      return;
    }

    body.innerHTML = items.map(item => `
      <div class="cart-item">
        ${item.imgSrc
          ? `<img class="cart-item__img" src="${item.imgSrc}" alt="${item.name}" onerror="this.style.display='none'">`
          : `<div class="cart-item__img-placeholder">🍽️</div>`}
        <div class="cart-item__info">
          <div class="cart-item__name">${item.name}</div>
          <div class="cart-item__price">${(item.price * item.qty).toLocaleString('fr-FR')} CFA</div>
        </div>
        <div class="cart-item__qty">
          <button class="cart-item__qty-btn" onclick="Cart.changeQty('${esc(item.name)}', -1)">−</button>
          <span class="cart-item__qty-num">${item.qty}</span>
          <button class="cart-item__qty-btn" onclick="Cart.changeQty('${esc(item.name)}', 1)">+</button>
        </div>
        <span class="cart-item__remove" onclick="Cart.remove('${esc(item.name)}')">🗑</span>
      </div>`).join('');
  }

  function esc(s) { return s.replace(/'/g, "\\'"); }

  function open() {
    document.getElementById('cart-panel')?.classList.add('open');
    document.getElementById('cart-overlay')?.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function close() {
    document.getElementById('cart-panel')?.classList.remove('open');
    document.getElementById('cart-overlay')?.classList.remove('open');
    document.body.style.overflow = '';
  }

  // Initialisation
  document.addEventListener('DOMContentLoaded', () => {
    render();

    document.getElementById('cart-btn')?.addEventListener('click', open);
    document.getElementById('cart-close')?.addEventListener('click', close);
    document.getElementById('cart-overlay')?.addEventListener('click', close);
    document.getElementById('cart-clear')?.addEventListener('click', () => { clear(); });
    document.getElementById('cart-checkout')?.addEventListener('click', () => {
  if (count() === 0) return;
  const summary = items.map(i => `${i.name} x${i.qty}`).join(', ');
  localStorage.setItem('akadi_order', JSON.stringify({ items, summary }));
  close();
  window.location.href = 'contact.html';
});

    // Boutons "Ajouter au panier" dans menu-item
    document.querySelectorAll('.menu-item__add-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const item = btn.closest('.menu-item');
        const name  = item?.querySelector('.menu-item__name')?.textContent?.trim() || 'Plat';
        const priceText = item?.querySelector('.menu-item__price')?.textContent?.replace(/[^\d]/g, '') || '0';
        const price = parseInt(priceText, 10);
        const imgSrc = item?.querySelector('.menu-item__image')?.src || '';
        Cart.add(name, price, imgSrc);
      });
    });
  });

  return { add, remove, changeQty, clear, open, close };
})();

/* ---- Toast notification ---- */
function showToast(msg) {
  let toast = document.getElementById('cart-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'cart-toast';
    toast.className = 'cart-toast';
    document.body.appendChild(toast);
  }
  toast.textContent = msg;
  toast.classList.add('show');
  clearTimeout(toast._timer);
  toast._timer = setTimeout(() => toast.classList.remove('show'), 2500);
}

/* ============================================
   FORMULAIRE RÉSERVATION/COMMANDE (contact.html)
   ============================================ */
(function () {
  // Pré-remplir la date avec aujourd'hui
  const dateInput = document.getElementById('date');
  if (dateInput) {
    const today = new Date().toISOString().split('T')[0];
    dateInput.value = today;
  }

  // Afficher le résumé de commande si venu du panier
  const order = JSON.parse(localStorage.getItem('akadi_order') || 'null');
  
  if (order) {
    // === MODE COMMANDE ===
    const block = document.getElementById('order-summary-block');
    const text  = document.getElementById('order-summary-text');
    if (block && text) {
      block.style.display = 'block';
      text.textContent = order.summary;
    }

    // Masquer la section réservation, afficher la section commande
    const reservationSection = document.getElementById('reservation-section');
    const orderTimeSection = document.getElementById('order-time-section');
    const guestsGroup = document.getElementById('guests-group');
    
    if (reservationSection) reservationSection.style.display = 'none';
    if (orderTimeSection) orderTimeSection.style.display = 'block';
    if (guestsGroup) guestsGroup.style.display = 'none';

    // Rendre l'heure de réservation non requise
    const reservationTimeSelect = document.getElementById('reservation-time');
    if (reservationTimeSelect) {
      reservationTimeSelect.required = false;
    }

    // Afficher/masquer les champs selon le mode choisi
    document.querySelectorAll('input[name="mode"]').forEach(radio => {
      radio.addEventListener('change', () => {
        const addr = document.getElementById('address-block');
        const pickupBlock = document.getElementById('pickup-time-block');
        const deliveryBlock = document.getElementById('delivery-time-block');
        const pickupSelect = document.getElementById('pickup-time');
        const deliverySelect = document.getElementById('delivery-time');

        // Affichage conditionnel des blocs
        if (radio.value === 'livraison') {
          addr.style.display = 'block';
          pickupBlock.style.display = 'none';
          deliveryBlock.style.display = 'block';

          // Rendre obligatoires les champs de livraison
          const input = document.getElementById('delivery-address');
          input.required = true;
          deliverySelect.required = true;
          pickupSelect.required = false;
        } else { // sur_place
          addr.style.display = 'none';
          pickupBlock.style.display = 'block';
          deliveryBlock.style.display = 'none';

          // Rendre obligatoire le champ de récupération, pas la livraison
          const input = document.getElementById('delivery-address');
          input.required = false;
          pickupSelect.required = true;
          deliverySelect.required = false;
        }
      });
    });

    // Initialiser l'état au chargement (mode par défaut: sur_place)
    const defaultMode = document.querySelector('input[name="mode"]:checked');
    if (defaultMode) {
      const event = new Event('change', { bubbles: true });
      defaultMode.dispatchEvent(event);
    }

    // Gérer la soumission du formulaire
    const form = document.getElementById('reservation-form');
    if (form) {
      form.addEventListener('submit', e => {
        e.preventDefault();
        
        let valid = true;
        form.querySelectorAll('[required]').forEach(field => {
          const err = field.nextElementSibling;
          if (!field.value.trim()) {
            field.classList.add('error');
            if (err) err.classList.add('show');
            valid = false;
          } else {
            field.classList.remove('error');
            if (err) err.classList.remove('show');
          }
        });

        if (valid) {
          // Déterminer le mode (récupération ou livraison)
          const mode = document.querySelector('input[name="mode"]:checked')?.value || 'sur_place';
          let successMessage = '';

          if (mode === 'livraison') {
            const address = document.getElementById('delivery-address').value;
            const time = document.getElementById('delivery-time').value;
            successMessage = `Réservation faite. Le livreur passera à ${address}, à ${time}.`;
          } else {
            const time = document.getElementById('pickup-time').value;
            successMessage = `Réservation faite. Merci de respecter l'heure de récupération : ${time}.`;
          }

          // Afficher le message personnalisé
          const successText = document.getElementById('form-success-text');
          if (successText) {
            successText.textContent = successMessage;
          }

          // Masquer le formulaire et afficher le message de succès
          form.style.display = 'none';
          const success = document.getElementById('form-success');
          if (success) success.classList.add('show');

          // Vider le panier
          Cart.clear();

          // Nettoyer le localStorage
          localStorage.removeItem('akadi_order');
        }
      });
    }

    // Nettoyer le localStorage après lecture
    localStorage.removeItem('akadi_order');
  } else {
    // === MODE RÉSERVATION (accès direct au formulaire) ===
    const form = document.getElementById('reservation-form');
    if (form) {
      form.addEventListener('submit', e => {
        e.preventDefault();
        
        let valid = true;
        form.querySelectorAll('[required]').forEach(field => {
          const err = field.nextElementSibling;
          if (!field.value.trim()) {
            field.classList.add('error');
            if (err) err.classList.add('show');
            valid = false;
          } else {
            field.classList.remove('error');
            if (err) err.classList.remove('show');
          }
        });

        if (valid) {
          const reservationTime = document.getElementById('reservation-time').value;
          const guestCount = document.getElementById('guests').value || 'non spécifié';
          
          // Message de succès pour réservation
          const successText = document.getElementById('form-success-text');
          if (successText) {
            successText.textContent = `Réservation confirmée pour ${guestCount} personne(s) à ${reservationTime}. Merci pour votre confiance !`;
          }

          // Masquer le formulaire et afficher le message de succès
          form.style.display = 'none';
          const success = document.getElementById('form-success');
          if (success) success.classList.add('show');
        }
      });
    }
  }
})();

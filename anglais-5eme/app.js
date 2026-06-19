// Éléments du DOM
const sectionContainer = document.getElementById('section-container');
const currentSectionName = document.getElementById('current-section-name');
const globalScoreDisplay = document.getElementById('global-score');
const apiModal = document.getElementById('api-modal');
const apiKeyInput = document.getElementById('api-key-input');
const saveApiKeyBtn = document.getElementById('save-api-key');
const navLinks = document.querySelectorAll('.nav-links li');
const resetApiKeyBtn = document.getElementById('reset-api-key');

// État de l'application
let state = {
    currentSection: 'home',
    score: 0,
    audioLoading: false
};

// Initialisation
document.addEventListener('DOMContentLoaded', () => {
    initApp();
});

function initApp() {
    checkApiKey();
    setupNavigation();
    renderSection('home');

    resetApiKeyBtn.addEventListener('click', () => {
        apiModal.classList.remove('hidden');
        apiKeyInput.value = localStorage.getItem('el_api_key') || '';
    });

    saveApiKeyBtn.addEventListener('click', () => {
        const key = apiKeyInput.value.trim();
        if (key) {
            localStorage.setItem('el_api_key', key);
            apiModal.classList.add('hidden');
        } else {
            alert('Veuillez saisir une clé valide.');
        }
    });
}

function checkApiKey() {
    if (!localStorage.getItem('el_api_key')) {
        apiModal.classList.remove('hidden');
    }
}

function setupNavigation() {
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            const section = link.getAttribute('data-section');
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
            renderSection(section);
        });
    });
}

// Moteur de rendu des sections
function renderSection(sectionId) {
    state.currentSection = sectionId;
    sectionContainer.innerHTML = '<div class="loader-container"><div class="spinner"></div></div>';

    // Petite pause pour l'effet visuel
    setTimeout(() => {
        switch(sectionId) {
            case 'home': renderHome(); break;
            case 'pronouns': renderPronouns(); break;
            case 'adjectives': renderAdjectives(); break;
            case 'prepositions': renderPrepositions(); break;
            case 'verbs': renderVerbs(); break;
            case 'conjugation': renderConjugation(); break;
            case 'translation': renderTranslation(); break;
            case 'active-passive': renderActivePassive(); break;
        }
    }, 300);
}

// --- AUDIO ELEVENLABS ---

async function playAudio(text) {
    const apiKey = localStorage.getItem('el_api_key');
    if (!apiKey) {
        apiModal.classList.remove('hidden');
        return;
    }

    const cleanText = text.replace(/'/g, "\\'");
    const cacheKey = 'audio_' + btoa(unescape(encodeURIComponent(cleanText))).slice(0, 40);
    const cached = localStorage.getItem(cacheKey);

    try {
        let audioData;
        if (cached) {
            const parsed = JSON.parse(cached);
            audioData = parsed.data;
            // Optionnel: rafraîchir le timestamp pour marquer l'utilisation récente
            try {
                parsed.ts = Date.now();
                localStorage.setItem(cacheKey, JSON.stringify(parsed));
            } catch(e) {}
        } else {
            showAudioLoading(true);

            const response = await fetch(
                'https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM',
                {
                    method: 'POST',
                    headers: {
                        'xi-api-key': apiKey,
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        text: text,
                        model_id: 'eleven_multilingual_v2',
                        voice_settings: { stability: 0.5, similarity_boost: 0.75 }
                    })
                }
            );

            if (!response.ok) throw new Error('API Error');

            const blob = await response.blob();
            audioData = await blobToBase64(blob);

            const cacheEntry = { ts: Date.now(), data: audioData };
            try {
                localStorage.setItem(cacheKey, JSON.stringify(cacheEntry));
            } catch(e) {
                console.warn('Cache plein, nettoyage...');
                clearOldestCache();
                try { localStorage.setItem(cacheKey, JSON.stringify(cacheEntry)); } catch(e2) {}
            }
        }

        const audio = new Audio(audioData);
        audio.play();
        showAudioLoading(false);
    } catch (err) {
        console.error('ElevenLabs error:', err);
        showAudioLoading(false);
        alert('Erreur audio. Vérifie ta clé API ou ta connexion.');
    }
}

function showAudioLoading(show) {
    const loader = document.getElementById('audio-loading');
    if (show) loader.classList.remove('hidden');
    else loader.classList.add('hidden');
}

function blobToBase64(blob) {
    return new Promise((resolve, _) => {
        const reader = new FileReader();
        reader.onloadend = () => resolve(reader.result);
        reader.readAsDataURL(blob);
    });
}

function clearOldestCache() {
    let items = [];
    for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key.startsWith('audio_')) {
            try {
                const val = JSON.parse(localStorage.getItem(key));
                items.push({ key, ts: val.ts || 0 });
            } catch(e) {}
        }
    }
    // Trier par timestamp croissant (plus anciens en premier)
    items.sort((a, b) => a.ts - b.ts);
    // Supprimer les 20 plus anciens pour faire de la place
    items.slice(0, 20).forEach(item => localStorage.removeItem(item.key));
}

// Helper pour créer un bouton audio
function createAudioBtn(text) {
    return `<button class="audio-btn" onclick="playAudio('${text.replace(/'/g, "\\'")}')" title="Écouter">🔊</button>`;
}

// --- VUES DES SECTIONS ---

function renderHome() {
    currentSectionName.innerText = "Accueil";
    sectionContainer.innerHTML = `
        <div class="home-hero card">
            <h1>Welcome to English Academy! 🎓</h1>
            <p>Prêt à booster ton anglais niveau 5ème ? Explore les modules, écoute la prononciation parfaite et gagne des étoiles !</p>
            <div class="home-grid">
                <div class="stat-card">
                    <h3>Prononciation</h3>
                    <p>Propulsé par ElevenLabs AI</p>
                </div>
                <div class="stat-card">
                    <h3>Modules</h3>
                    <p>7 thématiques clés</p>
                </div>
            </div>
        </div>
        <div class="card">
            <h3>Astuce :</h3>
            <p>Utilise le bouton 🔊 à côté de chaque mot pour entendre Rachel, ta professeure virtuelle.</p>
        </div>
    `;
}

// Les autres fonctions de rendu (renderPronouns, etc.) seront implémentées dans l'étape suivante.
// Je les déclare vides ici pour éviter les erreurs.
function updateScore(points) {
    state.score += points;
    globalScoreDisplay.innerText = state.score;
}

async function listenToAllPronouns() {
    const examples = ENGLISH_DATA.pronouns.map(p => p.example);
    for (const text of examples) {
        await playAudio(text);
        await new Promise(r => setTimeout(r, 1500)); // Pause de 1.5s
    }
}

// --- MODULE 1: PRONOMS ---
function renderPronouns() {
    currentSectionName.innerText = "Les Pronoms Personnels";
    let html = `
        <div class="section-actions">
            <button class="btn-primary" onclick="listenToAllPronouns()">🔊 Écouter toute la leçon</button>
        </div>
        <div class="card">
            <h3>Tableau des Pronoms</h3>
            <table class="data-table">
                <thead>
                    <tr>
                        <th>Type</th>
                        <th>Anglais</th>
                        <th>Français</th>
                        <th>Exemple</th>
                        <th>Écouter</th>
                    </tr>
                </thead>
                <tbody>
    `;

    ENGLISH_DATA.pronouns.forEach(p => {
        html += `
            <tr>
                <td><strong>${p.type}</strong></td>
                <td><span class="highlight">${p.en}</span></td>
                <td>${p.fr}</td>
                <td><small>${p.example}</small></td>
                <td>${createAudioBtn(p.example)}</td>
            </tr>
        `;
    });

    html += `
                </tbody>
            </table>
        </div>
        <div class="quiz-container">
            <div class="card">
                <h3>Quiz : Choisis le bon pronom</h3>
                <div id="pronoun-quiz-box">
                    <button class="btn-primary" onclick="startPronounQuiz()">Lancer le Quiz (10 questions)</button>
                </div>
            </div>
        </div>
    `;
    sectionContainer.innerHTML = html;
}

let currentQuiz = null;
function startPronounQuiz() {
    const questions = [
        { q: "___ am happy.", o: ["I", "Me", "My", "Mine"], a: "I" },
        { q: "Look at ___!", o: ["I", "Me", "My", "Mine"], a: "Me" },
        { q: "This is ___ book.", o: ["I", "Me", "My", "Mine"], a: "My" },
        { q: "The pen is ___.", o: ["I", "Me", "My", "Mine"], a: "Mine" },
        { q: "___ plays football.", o: ["He", "Him", "His", "Himself"], a: "He" },
        { q: "Give it to ___.", o: ["He", "Him", "His", "Himself"], a: "Him" },
        { q: "It is ___ car.", o: ["He", "Him", "His", "Himself"], a: "His" },
        { q: "He did it ___.", o: ["He", "Him", "His", "Himself"], a: "Himself" },
        { q: "___ are students.", o: ["We", "Us", "Our", "Ours"], a: "We" },
        { q: "Join ___.", o: ["We", "Us", "Our", "Ours"], a: "Us" },
        { q: "___ names are Tom and Ben.", o: ["They", "Them", "Their", "Theirs"], a: "Their" },
        { q: "I see ___ in the park.", o: ["They", "Them", "Their", "Theirs"], a: "Them" },
        { q: "That house is ___.", o: ["They", "Them", "Their", "Theirs"], a: "Theirs" },
        { q: "She loves ___ cat.", o: ["She", "Her", "Hers", "Herself"], a: "Her" },
        { q: "The victory is ___.", o: ["She", "Her", "Hers", "Herself"], a: "Hers" }
    ];
    runQuiz("pronoun-quiz-box", questions);
}

function runQuiz(containerId, questions) {
    const container = document.getElementById(containerId);
    let index = 0;
    let score = 0;

    function showQuestion() {
        if (index >= questions.length) {
            container.innerHTML = `<h4>Bravo ! Score : ${score}/${questions.length}</h4>
            <button class="btn-primary" onclick="renderSection(state.currentSection)">Recommencer</button>`;
            updateScore(score * 5);
            return;
        }
        const q = questions[index];
        container.innerHTML = `
            <div class="question-card">
                <p>Question ${index + 1}/${questions.length}</p>
                <h3>${q.q.replace("___", "______")}</h3>
                <div class="options-grid">
                    ${q.o.map(opt => `<button class="option-btn" onclick="checkAnswer(this, '${opt}', '${q.a}')">${opt}</button>`).join('')}
                </div>
            </div>
        `;
    }

    window.checkAnswer = (btn, selected, correct) => {
        const buttons = btn.parentElement.querySelectorAll('.option-btn');
        buttons.forEach(b => b.disabled = true);
        if (selected === correct) {
            btn.classList.add('correct');
            score++;
        } else {
            btn.classList.add('wrong');
            buttons.forEach(b => { if(b.innerText === correct) b.classList.add('correct'); });
        }
        setTimeout(() => {
            index++;
            showQuestion();
        }, 1500);
    };

    showQuestion();
}

// --- MODULE 2: ADJECTIFS ---
function renderAdjectives() {
    currentSectionName.innerText = "Les Adjectifs";
    let html = `
        <div class="card">
            <h3>Règle d'or : L'adjectif se place AVANT le nom !</h3>
            <p>Exemple: A <strong>red</strong> car (Une voiture rouge), A <strong>big</strong> house (Une grande maison).</p>
        </div>
        <div class="tabs-nav">
            <button class="tab-btn active" onclick="showAdjTab('list')">Liste</button>
            <button class="tab-btn" onclick="showAdjTab('quiz')">Quiz</button>
        </div>
        <div id="adj-content"></div>
    `;
    sectionContainer.innerHTML = html;
    showAdjTab('list');
}

window.showAdjTab = (tab) => {
    const container = document.getElementById('adj-content');
    const btns = document.querySelectorAll('.tab-btn');
    btns.forEach(b => b.classList.toggle('active', b.innerText.toLowerCase().includes(tab)));

    if (tab === 'list') {
        let html = `<div class="vocab-grid">`;
        ENGLISH_DATA.adjectives.forEach(adj => {
            html += `
                <div class="vocab-card">
                    <div><strong>${adj.en}</strong><br><small>${adj.fr}</small></div>
                    ${createAudioBtn(adj.en)}
                </div>
            `;
        });
        html += `</div>`;
        container.innerHTML = html;
    } else {
        container.innerHTML = `<div id="adj-quiz-box"></div>`;
        const questions = [
            { q: "Une voiture rouge", o: ["A car red", "A red car", "Red a car", "Car red a"], a: "A red car" },
            { q: "Un grand homme", o: ["A man tall", "A tall man", "Tall a man", "Man a tall"], a: "A tall man" },
            { q: "Elephants are ___ than cats.", o: ["bigger", "more big", "bigest", "biger"], a: "bigger" },
            { q: "This is the ___ book in the shop.", o: ["best", "goodest", "better", "most good"], a: "best" },
            { q: "She is ___ than me.", o: ["happier", "more happy", "happyer", "happiest"], a: "happier" }
        ];
        runQuiz("adj-quiz-box", questions);
    }
}

// --- MODULE 3: PREPOSITIONS ---
function renderPrepositions() {
    currentSectionName.innerText = "Les Prépositions";
    sectionContainer.innerHTML = `
        <div class="tabs-nav">
            <button class="tab-btn active" onclick="showPrepTab('list')">Illustrations</button>
            <button class="tab-btn" onclick="showPrepTab('quiz')">Quiz</button>
        </div>
        <div id="prep-content"></div>
    `;
    showPrepTab('list');
}

window.showPrepTab = (tab) => {
    const container = document.getElementById('prep-content');
    if (tab === 'list') {
        let html = `<div class="card"><h3>Les Prépositions de Lieu</h3><div class="vocab-grid">`;
        ENGLISH_DATA.prepositions.filter(p => p.type === "Lieu").forEach(p => {
            html += `
                <div class="vocab-card">
                    <div><strong>${p.en}</strong> (${p.fr})<br><small>${p.example}</small></div>
                    ${createAudioBtn(p.example)}
                </div>
            `;
        });
        html += `</div></div>`;
        container.innerHTML = html;
    } else {
        container.innerHTML = `<div id="prep-quiz-box"></div>`;
        const questions = [
            { q: "The book is ___ the table (sur).", o: ["in", "on", "under", "at"], a: "on" },
            { q: "The cat is ___ the chair (sous).", o: ["behind", "between", "under", "next to"], a: "under" },
            { q: "I meet you ___ 5 o'clock.", o: ["on", "at", "in", "by"], a: "at" },
            { q: "I am good ___ English.", o: ["at", "in", "on", "with"], a: "at" },
            { q: "She is afraid ___ spiders.", o: ["of", "at", "with", "from"], a: "of" }
        ];
        runQuiz("prep-quiz-box", questions);
    }
}

// --- MODULE 4: VERBES ---
function renderVerbs() {
    currentSectionName.innerText = "80 Verbes Fréquents";
    sectionContainer.innerHTML = `
        <div class="tabs-nav">
            <button class="tab-btn active" onclick="showVerbTab('list')">Liste & Recherche</button>
            <button class="tab-btn" onclick="showVerbTab('flashcards')">Flashcards</button>
            <button class="tab-btn" onclick="showVerbTab('quiz')">Quiz Prétérit</button>
        </div>
        <div id="verb-content"></div>
    `;
    showVerbTab('list');
}

window.showVerbTab = (tab) => {
    const container = document.getElementById('verb-content');
    if (tab === 'list') {
        let html = `
            <div class="card"><input type="text" id="verb-search" placeholder="Chercher un verbe..." oninput="filterVerbs(this.value)"></div>
            <div id="verbs-list" class="vocab-grid">
        `;
        ENGLISH_DATA.verbs.forEach(v => {
            html += `
                <div class="card verb-card" data-base="${v.base.toLowerCase()}" data-fr="${v.fr.toLowerCase()}">
                    <h4>${v.base} - ${v.fr}</h4>
                    <p><small>Prétérit: ${v.preterit} | P.Passé: ${v.participle}</small></p>
                    <div class="verb-examples">
                        ${v.examples.map(ex => `<div class="ex-line">${createAudioBtn(ex)} <span>${ex}</span></div>`).join('')}
                    </div>
                </div>
            `;
        });
        html += `</div>`;
        container.innerHTML = html;
    } else if (tab === 'flashcards') {
        renderVerbFlashcards(container);
    } else {
        renderVerbQuiz(container);
    }
}

function renderVerbFlashcards(container) {
    let idx = 0;
    function show() {
        const v = ENGLISH_DATA.verbs[idx];
        container.innerHTML = `
            <div class="quiz-container">
                <div class="card flashcard" onclick="this.classList.toggle('flipped')" style="height:250px; cursor:pointer; perspective: 1000px;">
                    <div class="flashcard-inner" style="position:relative; width:100%; height:100%; text-align:center; transition: transform 0.6s; transform-style: preserve-3d;">
                        <div class="front" style="position:absolute; width:100%; height:100%; backface-visibility: hidden; display:flex; align-items:center; justify-content:center; font-size:2rem; background:#f1f3f5; border-radius:12px;">
                            ${v.base}
                        </div>
                        <div class="back" style="position:absolute; width:100%; height:100%; backface-visibility: hidden; transform: rotateY(180deg); display:flex; align-items:center; justify-content:center; font-size:2rem; background:var(--accent); color:var(--primary); border-radius:12px;">
                            ${v.fr}
                        </div>
                    </div>
                </div>
                <div style="text-align:center; margin-top:20px;">
                    ${createAudioBtn(v.base)}
                    <button class="btn-primary" onclick="window.nextFlashcard()">Suivant</button>
                </div>
            </div>
        `;
    }
    window.nextFlashcard = () => { idx = (idx + 1) % ENGLISH_DATA.verbs.length; show(); };
    show();
}

function renderVerbQuiz(container) {
    let idx = 0;
    let score = 0;
    function show() {
        if (idx >= 10) {
            container.innerHTML = `<div class="card"><h3>Terminé ! Score : ${score}/10</h3><button class="btn-primary" onclick="showVerbTab('quiz')">Recommencer</button></div>`;
            return;
        }
        const v = ENGLISH_DATA.verbs[idx];
        container.innerHTML = `
            <div class="card quiz-container">
                <h3>Trouve le prétérit du verbe : <strong>${v.base}</strong></h3>
                <input type="text" id="verb-quiz-input" placeholder="Saisis le prétérit...">
                <button class="btn-primary" onclick="checkVerbQuiz('${v.preterit.toLowerCase()}')">Valider</button>
                <div id="verb-quiz-feedback"></div>
            </div>
        `;
    }
    window.checkVerbQuiz = (correct) => {
        const val = document.getElementById('verb-quiz-input').value.trim().toLowerCase();
        const feedback = document.getElementById('verb-quiz-feedback');
        if (val === correct || correct.includes(val)) {
            feedback.innerHTML = `<p class="success">Bravo !</p>`;
            score++;
        } else {
            feedback.innerHTML = `<p class="error">Non, c'était : ${correct}</p>`;
        }
        setTimeout(() => { idx++; show(); }, 1500);
    };
    show();
}

window.filterVerbs = (val) => {
    const cards = document.querySelectorAll('.verb-card');
    cards.forEach(c => {
        if (c.dataset.base.includes(val.toLowerCase()) || c.dataset.fr.includes(val.toLowerCase())) {
            c.style.display = 'block';
        } else {
            c.style.display = 'none';
        }
    });
};

// --- MODULE 5: CONJUGAISON ---
function renderConjugation() {
    currentSectionName.innerText = "La Conjugaison";
    sectionContainer.innerHTML = `
        <div class="card">
            <div class="tabs-nav">
                <button class="tab-btn active" onclick="showTense('present-simple')">Present Simple</button>
                <button class="tab-btn" onclick="showTense('present-continuous')">Present Continuous</button>
                <button class="tab-btn" onclick="showTense('preterit')">Prétérit</button>
                <button class="tab-btn" onclick="showTense('present-perfect')">Present Perfect</button>
                <button class="tab-btn" onclick="showTense('future')">Futur (Will)</button>
                <button class="tab-btn" onclick="showTense('modals')">Modaux</button>
            </div>
            <div id="tense-content" class="tense-content">
                <!-- Contenu injecté ici -->
            </div>
        </div>
    `;
    showTense('present-simple');
}

window.showTense = (tense) => {
    const container = document.getElementById('tense-content');
    const btns = document.querySelectorAll('.tab-btn');
    btns.forEach(b => b.classList.toggle('active', b.onclick.toString().includes(tense)));

    let content = "";
    if (tense === 'present-simple') {
        content = `
            <h3>Present Simple</h3>
            <p>Utilisé pour les vérités générales et les habitudes.</p>
            <ul>
                <li>I play ${createAudioBtn("I play")}</li>
                <li>You play ${createAudioBtn("You play")}</li>
                <li>He/She/It play<strong>s</strong> ${createAudioBtn("He plays")}</li>
            </ul>
            <div class="card"><h4>Quiz Rapide</h4><div id="tense-quiz"></div></div>
        `;
    } else if (tense === 'present-continuous') {
        content = `
            <h3>Present Continuous (BE + ING)</h3>
            <p>Action en cours au moment où l'on parle.</p>
            <p>Exemple: I am eating. ${createAudioBtn("I am eating")}</p>
            <div class="card"><h4>Quiz Rapide</h4><div id="tense-quiz"></div></div>
        `;
    } else if (tense === 'preterit') {
        content = `
            <h3>Le Prétérit</h3>
            <p>Action passée et terminée.</p>
            <p>Régulier: Verbe + <strong>ED</strong></p>
            <p>Exemple: I walked. ${createAudioBtn("I walked")}</p>
            <div class="card"><h4>Quiz Rapide</h4><div id="tense-quiz"></div></div>
        `;
    } else if (tense === 'present-perfect') {
        content = `
            <h3>Le Present Perfect (HAVE + Participe Passé)</h3>
            <p>Lien entre le passé et le présent.</p>
            <p>Exemple: I have lost my keys. ${createAudioBtn("I have lost my keys")}</p>
            <div class="card"><h4>Quiz Rapide</h4><div id="tense-quiz"></div></div>
        `;
    } else if (tense === 'future') {
        content = `
            <h3>Futur Simple (WILL)</h3>
            <p>Décision soudaine ou prédiction.</p>
            <p>Exemple: I will help you. ${createAudioBtn("I will help you")}</p>
            <div class="card"><h4>Quiz Rapide</h4><div id="tense-quiz"></div></div>
        `;
    } else if (tense === 'modals') {
        content = `
            <h3>Les Modaux</h3>
            <p>CAN (capacité), MUST (obligation), SHOULD (conseil)...</p>
            <ul>
                <li>I can swim. ${createAudioBtn("I can swim")}</li>
                <li>You must study. ${createAudioBtn("You must study")}</li>
            </ul>
            <div class="card"><h4>Quiz Rapide</h4><div id="tense-quiz"></div></div>
        `;
    }
    container.innerHTML = content;

    if (tense === 'present-simple') {
        runQuiz("tense-quiz", [{q: "She ___ (like) pizza.", o: ["like", "likes", "liking", "liked"], a: "likes"}]);
    } else if (tense === 'present-continuous') {
        runQuiz("tense-quiz", [{q: "They ___ (watch) TV now.", o: ["is watching", "are watching", "watch", "watches"], a: "are watching"}]);
    } else if (tense === 'preterit') {
        runQuiz("tense-quiz", [{q: "He ___ (finish) yesterday.", o: ["finish", "finishing", "finished", "was finish"], a: "finished"}]);
    } else if (tense === 'future') {
        runQuiz("tense-quiz", [{q: "I ___ (be) there.", o: ["will be", "am be", "shall be", "be"], a: "will be"}]);
    } else if (tense === 'modals') {
        runQuiz("tense-quiz", [{q: "You ___ study for the test (conseil).", o: ["must", "should", "can", "may"], a: "should"}]);
    }
}

// --- MODULE 6: TRADUCTION ---
function renderTranslation() {
    currentSectionName.innerText = "Exercices de Traduction";
    let index = 0;

    function showTranslateTask() {
        const t = ENGLISH_DATA.translations[index];
        sectionContainer.innerHTML = `
            <div class="card quiz-container">
                <h3>Traduire en anglais :</h3>
                <div class="translation-task">
                    <p class="source-text">${createAudioBtn(t.fr)} <strong>${t.fr}</strong></p>
                    <input type="text" id="trans-input" placeholder="Ta traduction ici...">
                    <button class="btn-primary" onclick="checkTranslation(${index})">Valider</button>
                </div>
                <div id="trans-feedback"></div>
            </div>
        `;
    }

    window.checkTranslation = (idx) => {
        const input = document.getElementById('trans-input').value.trim().toLowerCase();
        const correct = ENGLISH_DATA.translations[idx].en.toLowerCase();
        const feedback = document.getElementById('trans-feedback');

        if (input === correct) {
            feedback.innerHTML = `<p class="success">Excellent ! ${createAudioBtn(ENGLISH_DATA.translations[idx].en)}</p>`;
            updateScore(10);
            setTimeout(() => {
                index = (index + 1) % ENGLISH_DATA.translations.length;
                showTranslateTask();
            }, 2000);
        } else {
            feedback.innerHTML = `<p class="error">Presque ! La bonne réponse était : <strong>${ENGLISH_DATA.translations[idx].en}</strong> ${createAudioBtn(ENGLISH_DATA.translations[idx].en)}</p>
            <button class="btn-small" onclick="nextTrans()">Passer à la suivante</button>`;
        }
    };

    window.nextTrans = () => {
        index = (index + 1) % ENGLISH_DATA.translations.length;
        showTranslateTask();
    };

    showTranslateTask();
}

// --- MODULE 7: ACTIF / PASSIF ---
function renderActivePassive() {
    currentSectionName.innerText = "Voix Active vs Voix Passive";
    sectionContainer.innerHTML = `
        <div class="tabs-nav">
            <button class="tab-btn active" onclick="showPassiveTab('lesson')">Leçon</button>
            <button class="tab-btn" onclick="showPassiveTab('animation')">Animation</button>
            <button class="tab-btn" onclick="showPassiveTab('quiz')">Exercices</button>
        </div>
        <div id="passive-content"></div>
    `;
    showPassiveTab('lesson');
}

window.showPassiveTab = (tab) => {
    const container = document.getElementById('passive-content');
    if (tab === 'lesson') {
        container.innerHTML = `
            <div class="card">
                <h3>Voix Active vs Passive</h3>
                <p><strong>Active :</strong> Le sujet fait l'action. <em>(The cat eats the mouse)</em></p>
                <p><strong>Passive :</strong> Le sujet subit l'action. <em>(The mouse is eaten by the cat)</em></p>
                <hr>
                <h4>Formation : BE (conjugué) + Participe Passé</h4>
                <table class="data-table">
                    <tr><td>Present Simple</td><td>The room is cleaned.</td></tr>
                    <tr><td>Prétérit</td><td>The room was cleaned.</td></tr>
                    <tr><td>Futur</td><td>The room will be cleaned.</td></tr>
                </table>
            </div>
        `;
    } else if (tab === 'animation') {
        container.innerHTML = `
            <div class="card">
                <h3>Animation de transformation</h3>
                <div class="transformation-box" id="transfo-box">
                    <div class="word-tag active" style="order:1">Tom</div>
                    <div class="word-tag active" style="order:2">reads</div>
                    <div class="word-tag active" style="order:3">the book</div>
                </div>
                <button class="btn-primary" onclick="runAdvancedPassiveAnim()">Lancer la transformation</button>
            </div>
        `;
    } else {
        container.innerHTML = `<div id="passive-quiz-box"></div>`;
        const questions = [
            { q: "The cake ___ eaten by Sarah (present).", o: ["is", "was", "be", "has"], a: "is" },
            { q: "The windows ___ broken yesterday.", o: ["is", "are", "was", "were"], a: "were" },
            { q: "Active: 'He stole my bag' -> Passive: 'My bag ___ stolen'.", o: ["is", "was", "were", "be"], a: "was" },
            { q: "Passive: 'The letter was written by her'. Active ?", o: ["She wrote the letter", "She writes the letter", "She will write the letter"], a: "She wrote the letter" }
        ];
        runQuiz("passive-quiz-box", questions);
    }
}

window.runAdvancedPassiveAnim = () => {
    const box = document.getElementById('transfo-box');
    const tags = box.querySelectorAll('.word-tag');

    tags[0].style.transition = "all 1s ease";
    tags[2].style.transition = "all 1s ease";

    tags[0].style.order = "5"; // Tom passe à la fin
    tags[2].style.order = "1"; // The book passe au début

    setTimeout(() => {
        tags[1].innerHTML = "is read"; // Verbe change
        tags[0].innerHTML = "by Tom"; // Ajout de "by"
        tags.forEach(t => { t.classList.remove('active'); t.classList.add('passive'); });
        playAudio("The book is read by Tom");
    }, 1000);
}

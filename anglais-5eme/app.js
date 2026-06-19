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
            // Petit test audio après sauvegarde
            playAudio("API Key saved successfully. Let's learn English!");
        } else {
            alert('Veuillez saisir une clé valide.');
        }
    });

    // Bouton de test dans la modale
    const testAudioBtn = document.createElement('button');
    testAudioBtn.innerText = "🔊 Tester l'audio";
    testAudioBtn.className = "btn-small";
    testAudioBtn.style.marginTop = "10px";
    testAudioBtn.onclick = () => {
        const key = apiKeyInput.value.trim();
        if (!key) return alert("Saisis d'abord une clé.");
        localStorage.setItem('el_api_key', key);
        playAudio("Hello, I am Rachel. If you hear me, your API key is working perfectly!");
    };
    document.querySelector('.modal-actions').appendChild(testAudioBtn);
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

    // On utilise le texte brut pour le cache et l'API (pas d'échappement ici)
    const cacheKey = 'audio_' + btoa(unescape(encodeURIComponent(text))).slice(0, 40);
    const cached = localStorage.getItem(cacheKey);

    try {
        let audioData;
        if (cached) {
            const parsed = JSON.parse(cached);
            audioData = parsed.data;
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
                        'Content-Type': 'application/json',
                        'accept': 'audio/mpeg'
                    },
                    body: JSON.stringify({
                        text: text,
                        model_id: 'eleven_multilingual_v2',
                        voice_settings: { stability: 0.5, similarity_boost: 0.75 }
                    })
                }
            );

            if (!response.ok) {
                const errorData = await response.json().catch(() => ({ detail: 'Erreur inconnue' }));
                throw new Error(errorData.detail?.message || errorData.detail || 'Erreur API');
            }

            const blob = await response.blob();
            audioData = await blobToBase64(blob);

            const cacheEntry = { ts: Date.now(), data: audioData };
            try {
                localStorage.setItem(cacheKey, JSON.stringify(cacheEntry));
            } catch(e) {
                clearOldestCache();
                try { localStorage.setItem(cacheKey, JSON.stringify(cacheEntry)); } catch(e2) {}
            }
        }

        const audio = new Audio(audioData);
        await audio.play().catch(e => console.warn("Lecture auto bloquée par le navigateur, clic nécessaire."));
        showAudioLoading(false);
    } catch (err) {
        console.error('ElevenLabs error:', err);
        showAudioLoading(false);
        alert('Erreur ElevenLabs : ' + err.message + '\nVérifie ta clé API (xi-api-key) et ton crédit.');
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
    await listenSequentially(examples);
}

async function listenSequentially(texts) {
    for (const text of texts) {
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
        <div class="section-actions">
            <button class="btn-primary" onclick="listenSequentially(ENGLISH_DATA.adjectives.slice(0,10).map(a => a.en))">🔊 Écouter les 10 premiers</button>
        </div>
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
        <div class="section-actions">
            <button class="btn-primary" onclick="listenSequentially(ENGLISH_DATA.prepositions.map(p => p.example))">🔊 Écouter toute la leçon</button>
        </div>
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
                <button class="tab-btn" onclick="showTense('past-perfect')">Past Perfect</button>
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

    let html = "";

    if (tense === 'present-simple') {
        html = `
            <div class="lesson-section">
                <h3>Simple Present (Présent Simple)</h3>
                <p>Le Présent Simple s'utilise pour exprimer des **habitudes**, des **vérités générales** ou des **goûts**.</p>

                <div class="card">
                    <h4>1. Les Auxiliaires (Indispensables !)</h4>
                    <div class="flex-grid">
                        <div>
                            <strong>TO BE (Être)</strong>
                            <ul class="conj-list">
                                <li>I **am** ${createAudioBtn("I am")}</li>
                                <li>You **are** ${createAudioBtn("You are")}</li>
                                <li>He/She/It **is** ${createAudioBtn("He is")}</li>
                                <li>We **are** ${createAudioBtn("We are")}</li>
                                <li>They **are** ${createAudioBtn("They are")}</li>
                            </ul>
                        </div>
                        <div>
                            <strong>TO HAVE (Avoir)</strong>
                            <ul class="conj-list">
                                <li>I **have** ${createAudioBtn("I have")}</li>
                                <li>You **have** ${createAudioBtn("You have")}</li>
                                <li>He/She/It **has** (Attention !) ${createAudioBtn("He has")}</li>
                                <li>We **have** ${createAudioBtn("We have")}</li>
                                <li>They **have** ${createAudioBtn("They have")}</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="card">
                    <h4>2. Verbes Ordinaires (Ex: TO PLAY)</h4>
                    <p>**Règle Affirmative :** On utilise la base du verbe, mais on ajoute un **-S** à la 3ème personne du singulier (**He, She, It**).</p>
                    <ul class="conj-list">
                        <li>I play / He play**s** ${createAudioBtn("I play, He plays")}</li>
                    </ul>

                    <p>**Règle Négative :** On utilise l'auxiliaire **DO / DOES** + **NOT** + Verbe (base).</p>
                    <ul class="conj-list">
                        <li>I **do not** (don't) play ${createAudioBtn("I don't play")}</li>
                        <li>He **does not** (doesn't) play ${createAudioBtn("He doesn't play")}</li>
                    </ul>

                    <p>**Règle Interrogative :** On commence par **DO / DOES** + Sujet + Verbe (base) ?</p>
                    <ul class="conj-list">
                        <li>**Do** you play? ${createAudioBtn("Do you play?")}</li>
                        <li>**Does** she play? ${createAudioBtn("Does she play?")}</li>
                    </ul>

                    <p>**Règle Interro-Négative :** On utilise la contraction **DON'T / DOESN'T** en début de phrase.</p>
                    <ul class="conj-list">
                        <li>**Don't** you play? ${createAudioBtn("Don't you play?")}</li>
                        <li>**Doesn't** he play? ${createAudioBtn("Doesn't he play?")}</li>
                    </ul>
                </div>
            </div>
        `;
    } else if (tense === 'present-continuous') {
        html = `
            <div class="lesson-section">
                <h3>Present Progressive (ou Present Continuous)</h3>
                <p>On l'utilise pour une **action qui se passe maintenant**, au moment où l'on parle.</p>
                <div class="card">
                    <h4>Structure : Sujet + BE (au présent) + Verbe-ING</h4>
                    <p>**Affirmatif :**</p>
                    <ul class="conj-list">
                        <li>I **am eating** ${createAudioBtn("I am eating")}</li>
                        <li>He **is working** ${createAudioBtn("He is working")}</li>
                        <li>They **are playing** ${createAudioBtn("They are playing")}</li>
                    </ul>
                    <p>**Négatif :** On ajoute **NOT** après l'auxiliaire BE.</p>
                    <ul class="conj-list">
                        <li>I **am not** eating ${createAudioBtn("I am not eating")}</li>
                        <li>She **is not** (isn't) working ${createAudioBtn("She isn't working")}</li>
                    </ul>
                    <p>**Interrogatif :** On inverse le sujet et l'auxiliaire BE.</p>
                    <ul class="conj-list">
                        <li>**Are** you eating? ${createAudioBtn("Are you eating?")}</li>
                        <li>**Is** he working? ${createAudioBtn("Is he working?")}</li>
                    </ul>
                    <p>**Interro-Négatif :**</p>
                    <ul class="conj-list">
                        <li>**Aren't** you eating? ${createAudioBtn("Aren't you eating?")}</li>
                        <li>**Isn't** he working? ${createAudioBtn("Isn't he working?")}</li>
                    </ul>
                </div>
                <div class="card">
                    <h4>Auxiliaires au Présent Continu</h4>
                    <p>**BE** n'est généralement pas utilisé au continu, mais **HAVE** peut l'être pour une action (ex: having lunch).</p>
                    <ul class="conj-list">
                        <li>I **am having** lunch ${createAudioBtn("I am having lunch")}</li>
                    </ul>
                </div>
            </div>
        `;
    } else if (tense === 'preterit') {
        html = `
            <div class="lesson-section">
                <h3>Simple Past (Prétérit Simple)</h3>
                <p>On l'utilise pour une **action passée, datée et terminée**.</p>
                <div class="card">
                    <h4>1. Les Auxiliaires au passé</h4>
                    <div class="flex-grid">
                        <div>
                            <strong>TO BE (Was/Were)</strong>
                            <ul class="conj-list">
                                <li>I **was** / You **were** ${createAudioBtn("I was, You were")}</li>
                                <li>He/She/It **was** ${createAudioBtn("He was")}</li>
                                <li>We/They **were** ${createAudioBtn("They were")}</li>
                            </ul>
                        </div>
                        <div>
                            <strong>TO HAVE (Had)</strong>
                            <ul class="conj-list">
                                <li>I/You/He/They **had** ${createAudioBtn("I had")}</li>
                            </ul>
                            <p>(**Had** est le même pour tous !)</p>
                        </div>
                    </div>
                </div>
                <div class="card">
                    <h4>2. Verbes Ordinaires (Ex: TO WORK)</h4>
                    <p>**Affirmatif :** On ajoute **-ED** (verbes réguliers) ou on utilise la 2ème colonne (irréguliers).</p>
                    <ul class="conj-list"><li>I work**ed** / I **went** ${createAudioBtn("I worked, I went")}</li></ul>
                    <p>**Négatif / Interrogatif :** On utilise l'auxiliaire **DID** pour TOUS les sujets.</p>
                    <p>**Règle d'or :** Quand **DID** arrive, le verbe perd son **-ED** et revient à sa **forme de base** !</p>
                    <ul class="conj-list">
                        <li>**Négatif :** I **did not (didn't)** work ${createAudioBtn("I didn't work")}</li>
                        <li>**Interrogatif :** **Did** you work? ${createAudioBtn("Did you work?")}</li>
                        <li>**Interro-Négatif :** **Didn't** you work? ${createAudioBtn("Didn't you work?")}</li>
                    </ul>
                </div>
            </div>
        `;
    } else if (tense === 'present-perfect') {
        html = `
            <div class="lesson-section">
                <h3>Present Perfect</h3>
                <p>Le lien entre le passé et le présent (constat d'une action terminée ou bilan).</p>
                <div class="card">
                    <h4>Structure : Sujet + HAVE / HAS + Participe Passé</h4>
                    <ul class="conj-list">
                        <li>**Affirmatif :** I **have been** / She **has had** ${createAudioBtn("I have been, She has had")}</li>
                        <li>**Négatif :** I **haven't (have not)** been ${createAudioBtn("I haven't been")}</li>
                        <li>**Interrogatif :** **Have** you been? ${createAudioBtn("Have you been?")}</li>
                        <li>**Interro-Négatif :** **Hasn't** she had lunch? ${createAudioBtn("Hasn't she had lunch?")}</li>
                    </ul>
                </div>
            </div>
        `;
    } else if (tense === 'past-perfect') {
        html = `
            <div class="lesson-section">
                <h3>Past Perfect (Plus-que-parfait)</h3>
                <p>On l'utilise pour parler d'une action passée qui s'est déroulée **AVANT** une autre action passée.</p>
                <div class="card">
                    <h4>Structure : Sujet + HAD + Participe Passé</h4>
                    <p>**Affirmatif :** I **had seen** / She **had been** ${createAudioBtn("I had seen, She had been")}</p>
                    <p>**Négatif :** I **had not (hadn't)** seen ${createAudioBtn("I hadn't seen")}</p>
                    <p>**Interrogatif :** **Had** you seen? ${createAudioBtn("Had you seen?")}</p>
                    <p>**Interro-Négatif :** **Hadn't** they seen it? ${createAudioBtn("Hadn't they seen it?")}</p>
                </div>
            </div>
        `;
    } else if (tense === 'future') {
        html = `
            <div class="lesson-section">
                <h3>Simple Future (Futur Simple)</h3>
                <p>On l'utilise pour une **prédiction** ou une **décision soudaine**.</p>
                <div class="card">
                    <h4>Structure : Sujet + WILL + Verbe (base)</h4>
                    <ul class="conj-list">
                        <li>**Affirmatif :** I **will be** / He **will have** ${createAudioBtn("I will be, He will have")}</li>
                        <li>**Négatif :** I **will not (won't)** be ${createAudioBtn("I won't be")}</li>
                        <li>**Interrogatif :** **Will** you be there? ${createAudioBtn("Will you be there?")}</li>
                        <li>**Interro-Négatif :** **Won't** they help us? ${createAudioBtn("Won't they help us?")}</li>
                    </ul>
                </div>
            </div>
        `;
    } else if (tense === 'modals') {
        html = `
            <div class="lesson-section">
                <h3>Les Modaux (Can, Must, Should...)</h3>
                <p>Les modaux sont des petits mots qui changent le sens du verbe (capacité, obligation, conseil).</p>
                <div class="card">
                    <ul class="conj-list">
                        <li>**CAN** (Capacité) : I **can** swim. ${createAudioBtn("I can swim")}</li>
                        <li>**MUST** (Obligation) : You **must** listen. ${createAudioBtn("You must listen")}</li>
                        <li>**SHOULD** (Conseil) : You **should** sleep. ${createAudioBtn("You should sleep")}</li>
                        <li>**MAY** (Permission) : **May** I enter? ${createAudioBtn("May I enter?")}</li>
                    </ul>
                    <p>**Règle d'or :** Ils ne prennent **JAMAIS de -S** à la 3ème personne et sont suivis de la **base verbale**.</p>
                </div>
            </div>
        `;
    }

    html += `<div class="card quiz-card"><h4>Prêt pour un petit test ?</h4><div id="tense-quiz"></div></div>`;
    container.innerHTML = html;

    // Quiz automatiques selon le temps
    let questions = [];
    if (tense === 'present-simple') {
        questions = [
            { q: "He ___ (like) chocolate.", o: ["like", "likes", "liking", "liked"], a: "likes" },
            { q: "___ you speak English?", o: ["Do", "Does", "Are", "Is"], a: "Do" },
            { q: "She ___ (not work) on Sundays.", o: ["don't work", "doesn't work", "not work", "isn't work"], a: "doesn't work" },
            { q: "___ he like pizza?", o: ["Do", "Does", "Is", "Has"], a: "Does" },
            { q: "___ you want to come?", o: ["Don't", "Doesn't", "Aren't", "Isn't"], a: "Don't" }
        ];
    } else if (tense === 'present-continuous') {
        questions = [
            { q: "They ___ (play) football now.", o: ["is playing", "are playing", "play", "playing"], a: "are playing" },
            { q: "What ___ you doing?", o: ["do", "is", "are", "have"], a: "are" },
            { q: "___ he coming tonight?", o: ["Is", "Are", "Does", "Has"], a: "Is" },
            { q: "I ___ (not sleep) at the moment.", o: ["am not sleeping", "is not sleeping", "not sleep", "don't sleeping"], a: "am not sleeping" }
        ];
    } else if (tense === 'preterit') {
        questions = [
            { q: "I ___ (watch) a movie last night.", o: ["watch", "watching", "watched", "was watch"], a: "watched" },
            { q: "___ he call you yesterday?", o: ["Do", "Does", "Did", "Was"], a: "Did" },
            { q: "We ___ (not go) to school yesterday.", o: ["didn't go", "didn't went", "not went", "doesn't go"], a: "didn't go" },
            { q: "___ you see the movie?", o: ["Did", "Do", "Were", "Had"], a: "Did" }
        ];
    } else if (tense === 'future') {
        questions = [{ q: "I ___ (be) 15 next year.", o: ["will be", "am", "was", "will"], a: "will be" }];
    } else if (tense === 'present-perfect') {
        questions = [{ q: "She ___ (already see) this film.", o: ["have seen", "has see", "has seen", "seen"], a: "has seen" }];
    } else if (tense === 'modals') {
        questions = [{ q: "You ___ not smoke in the hospital.", o: ["must", "can", "should", "may"], a: "must" }];
    } else if (tense === 'past-perfect') {
        questions = [{ q: "The train ___ (leave) when I arrived.", o: ["has left", "had left", "was left", "leaves"], a: "had left" }];
    }

    if (questions.length > 0) runQuiz("tense-quiz", questions);
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
        <div class="section-actions">
            <button class="btn-primary" onclick="listenSequentially(['The cat eats the mouse', 'The mouse is eaten by the cat'])">🔊 Écouter l'essentiel</button>
        </div>
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
                <p><strong>Active :</strong> Le sujet fait l'action. <em>(The cat eats the mouse)</em> ${createAudioBtn("The cat eats the mouse")}</p>
                <p><strong>Passive :</strong> Le sujet subit l'action. <em>(The mouse is eaten by the cat)</em> ${createAudioBtn("The mouse is eaten by the cat")}</p>
                <hr>
                <h4>Formation : BE (conjugué) + Participe Passé</h4>
                <table class="data-table">
                    <tr><td>Present Simple</td><td>The room is cleaned. ${createAudioBtn("The room is cleaned")}</td></tr>
                    <tr><td>Prétérit</td><td>The room was cleaned. ${createAudioBtn("The room was cleaned")}</td></tr>
                    <tr><td>Futur</td><td>The room will be cleaned. ${createAudioBtn("The room will be cleaned")}</td></tr>
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

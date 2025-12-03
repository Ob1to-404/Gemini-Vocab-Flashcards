// =======================================================
// 1. Dastlabki Ma'lumotlar (JSON)
// =======================================================
let topics = [
    {
        id: 'formal_business',
        name: "💼 Formal va Ishbilarmonlik",
        words: [
            // Nouns (Otlar)
            { id: 1, word: "Accusation", meaning: "ayblov", known: 0 },
            { id: 2, word: "Authority", meaning: "hokimiyat, vakolat", known: 0 },
            { id: 3, word: "Circumstances", meaning: "sharoitlar", known: 0 },
            { id: 4, word: "Commitment", meaning: "sadoqat, majburiyat", known: 0 },
            { id: 5, word: "Complaint", meaning: "shikoyat", known: 0 },
            { id: 6, word: "Contribution", meaning: "hissa, qo'shiq", known: 0 },
            { id: 7, word: "Dilemma", meaning: "ikkilanma, muammo", known: 0 },
            { id: 8, word: "Distribution", meaning: "taqsimot", known: 0 },
            { id: 9, word: "Permission", meaning: "ruxsat", known: 0 },
            // Verbs (Fe'llar)
            { id: 10, word: "Acknowledge", meaning: "tan olmoq", known: 0 },
            { id: 11, word: "Approve", meaning: "ma'qullamoq", known: 0 },
            { id: 12, word: "Require", meaning: "talab qilmoq", known: 0 },
            { id: 13, word: "Regulate", meaning: "boshqarmoq, nazorat qilmoq", known: 0 },
            { id: 14, word: "Reject", meaning: "rad etmoq", known: 0 },
            { id: 15, word: "Assume", meaning: "taxmin qilmoq", known: 0 },
            { id: 16, word: "Affect", meaning: "ta'sir qilmoq", known: 0 },
            { id: 17, word: "Maintain", meaning: "saqlamoq, davom ettirmoq", known: 0 },
            { id: 18, word: "Persuade", meaning: "ko'ndirmoq", known: 0 },
            { id: 19, word: "Expand", meaning: "kengaymoq", known: 0 },
            { id: 20, word: "Evaluate", meaning: "baholamoq", known: 0 },
        ]
    },
    {
        id: 'quality_and_action',
        name: "✨ Sifat va Harakat",
        words: [
            // Nouns (Otlar)
            { id: 21, word: "Tough", meaning: "qiyin, kuchli, qattiq", known: 0 },
            { id: 22, word: "Achievement", meaning: "yutuq", known: 0 },
            { id: 23, word: "Alternatives", meaning: "muqobillar", known: 0 },
            { id: 24, word: "Assistance", meaning: "yordam, ko'mak", known: 0 },
            { id: 25, word: "Breakthrough", meaning: "katta yutuq", known: 0 },
            { id: 26, word: "Comparison", meaning: "taqqoslash", known: 0 },
            { id: 27, word: "Conflict", meaning: "mojaro", known: 0 },
            { id: 28, word: "Decline", meaning: "pasayish", known: 0 },
            { id: 29, word: "Disaster", meaning: "falokat", known: 0 },
            { id: 30, word: "Reaction", meaning: "reaksiya", known: 0 },
            { id: 31, word: "Strategy", meaning: "strategiya", known: 0 },
            // Verbs (Fe'llar)
            { id: 32, word: "Attempt", meaning: "urinish", known: 0 },
            { id: 33, word: "Capture", meaning: "qo'lga olmoq, egallamoq", known: 0 },
            { id: 34, word: "Collapse", meaning: "qulamoq", known: 0 },
            { id: 35, word: "Contribute", meaning: "hissa qo'shmoq", known: 0 },
            { id: 36, word: "Decrease", meaning: "kamaymoq", known: 0 },
            { id: 37, word: "Encounter", meaning: "duch kelmoq", known: 0 },
            { id: 38, word: "Identify", meaning: "aniqlamoq, tanimoq", known: 0 },
            { id: 39, word: "Object", meaning: "e'tiroz bildirmoq", known: 0 },
            { id: 40, word: "Summarize", meaning: "qisqacha bayon qilmoq", known: 0 },
            { id: 41, word: "Generate", meaning: "yaratmoq, hosil qilmoq", known: 0 },
            // Adjectives (Sifatlar)
            { id: 42, word: "Accurate", meaning: "aniq, to'g'ri", known: 0 },
            { id: 43, word: "Appropriate", meaning: "mos, to'g'ri", known: 0 },
            { id: 44, word: "Consistent", meaning: "izchil", known: 0 },
            { id: 45, word: "Deliberate", meaning: "ataylab qilingan", known: 0 },
            { id: 46, word: "Efficient", meaning: "samarali", known: 0 },
            { id: 47, word: "Inevitable", meaning: "muqarrar", known: 0 },
            { id: 48, word: "Reasonable", meaning: "oqilona", known: 0 },
            { id: 49, word: "Sufficient", meaning: "yetarli", known: 0 },
            { id: 50, word: "Temporary", meaning: "vaqtinchalik", known: 0 },
            { id: 51, word: "Widespread", meaning: "keng tarqalgan", known: 0 },
            { id: 52, word: "Ambitious", meaning: "maqsadli, katta orzuli", known: 0 },
            { id: 53, word: "Beneficial", meaning: "foydali", known: 0 },
            { id: 54, word: "Complex", meaning: "murakkab", known: 0 },
            { id: 55, word: "Delighted", meaning: "hursand, mamnun", known: 0 },
            { id: 56, word: "Enormous", meaning: "juda katta", known: 0 },
            { id: 57, word: "Incredible", meaning: "ishonib bo'lmaydigan", known: 0 },
            { id: 58, word: "Logical", meaning: "mantiqiy", known: 0 },
            { id: 59, word: "Permanent", meaning: "doimiy", known: 0 },
            { id: 60, word: "Sensible", meaning: "oqilona, tushunarli", known: 0 },
        ]
    },
];

let currentTopicId = topics[0].id; 
let words = topics[0].words; 
let currentWord = null;
let unknownWords = [...words];
// =======================================================
// 2. DOM Elementlari
// =======================================================
const currentWordEl = document.getElementById('current-word');
const currentMeaningEl = document.getElementById('current-meaning');
const wordCountEl = document.getElementById('word-count');
const btnKnow = document.getElementById('btn-know');
const btnDontKnow = document.getElementById('btn-dont-know');
const btnReset = document.getElementById('btn-reset');
const topicListEl = document.getElementById('topic-list'); 
const btnAddWord = document.getElementById('btn-add-word'); 
const btnStats = document.getElementById('btn-stats');  
const cardEl = document.getElementById('card'); // Kartaning asosiy qismi

// =======================================================
// 3. Mavzularni Boshqarish Funksiyalari
// =======================================================

function loadTopic(topicId) {
    const newTopic = topics.find(t => t.id === topicId);
    if (!newTopic) return;

    currentTopicId = topicId;
    words = newTopic.words;
    
    unknownWords = words.filter(w => w.known === 0);
    if (unknownWords.length === 0 && words.length > 0) {
        unknownWords = [...words]; 
    }
    
    highlightActiveTopic(topicId);
    init();
}

function renderTopics() {
    if (!topicListEl) return;
    topicListEl.innerHTML = ''; 

    topics.forEach(topic => {
        const listItem = document.createElement('li');
        listItem.dataset.topicId = topic.id;
        
        const button = document.createElement('button');
        button.textContent = topic.name;
        
        button.addEventListener('click', () => {
            loadTopic(topic.id);
        });

        listItem.appendChild(button);
        topicListEl.appendChild(listItem);
    });
    
    highlightActiveTopic(currentTopicId);
}

function highlightActiveTopic(topicId) {
    if (!topicListEl) return;
    topicListEl.querySelectorAll('li').forEach(li => {
        li.classList.remove('active');
    });
    
    const activeItem = topicListEl.querySelector(`[data-topic-id="${topicId}"]`);
    if (activeItem) {
        activeItem.classList.add('active');
    }
}

// =======================================================
// 4. Asosiy Mantıq (So'zlar, Hisoblagich, Reset)
// =======================================================

function updateCount() {
    const totalWords = words.length;
    const knownCount = words.filter(w => w.known > 0).length; 
    if (wordCountEl) {
        wordCountEl.textContent = `${knownCount}/${totalWords}`;
    }
}

function getNextWord() {
    // YENGI QO'SHIMCHA: Keyingi so'zni yuklaganda tarjimani yashirish
    if (currentMeaningEl) {
        currentMeaningEl.classList.remove('show');
    }
    
    if (unknownWords.length === 0) {
        const topicName = topics.find(t=>t.id===currentTopicId).name;
        if (currentWordEl && currentMeaningEl) {
            currentWordEl.textContent = `🥳 Tabriklaymiz! "${topicName}" mavzusini o'rgandingiz!`;
            currentMeaningEl.textContent = "Boshqa mavzuga o'ting yoki qayta ishlang.";
        }
        if (btnKnow) btnKnow.disabled = true;
        if (btnDontKnow) btnDontKnow.disabled = true;
        currentWord = null;
        return;
    }

    const randomIndex = Math.floor(Math.random() * unknownWords.length);
    currentWord = unknownWords[randomIndex];
    
    if (currentWordEl) currentWordEl.textContent = currentWord.word;
    if (currentMeaningEl) currentMeaningEl.textContent = currentWord.meaning;
    
    if (btnKnow) btnKnow.disabled = false;
    if (btnDontKnow) btnDontKnow.disabled = false;
}

// script.js faylidagi updateWordStatus funksiyasini almashtiring:

function updateWordStatus(isKnown) {
    if (!currentWord) return;

    // Tugma bosilganda darhol tarjimani ko'rsatish
    if (currentMeaningEl) {
        currentMeaningEl.classList.add('show');
    }

    const wordIndex = words.findIndex(w => w.id === currentWord.id);
    
    if (isKnown) {
        words[wordIndex].known++;
        unknownWords = unknownWords.filter(w => w.id !== currentWord.id);
    } else {
        words[wordIndex].known = 0;
        if (!unknownWords.some(w => w.id === currentWord.id)) {
            unknownWords.push(currentWord);
        }
        unknownWords.sort(() => Math.random() - 0.5);
    }

    // Keyingi so'zni tezda yuklash (setTimeout o'rniga juda qisqa kechikish)
    // 50ms qoldiramiz, shunda tarjima ko'rinishi uchun biroz vaqt qoladi.
    setTimeout(() => {
        updateCount();
        getNextWord();
    }, 50); // Kechikishni 50ms ga tushirdik
    
    // Agar umuman kechikishni xohlamasangiz, quyidagicha qoldiring:
    /* updateCount();
    getNextWord();
    */
}


function resetApp() {
    words.forEach(w => w.known = 0);
    unknownWords = [...words];
    unknownWords.sort(() => Math.random() - 0.5);
    init();
    alert(`"${topics.find(t=>t.id===currentTopicId).name}" mavzusi qayta ishga tushirildi! Yodlashni boshlang.`);
}

function dummyAction(action) {
    alert(`"${action}" funksiyasi hozircha faol emas. Kodlashni boshlash uchun tayyor!`);
}

function toggleMeaning() {
    if (!currentMeaningEl) return;
    
    currentMeaningEl.classList.toggle('show');
}


// =======================================================
// 5. Tugma Hodisalari
// =======================================================

// 1. Karta ustiga bosish hodisasi
if (cardEl) {
    cardEl.addEventListener('click', toggleMeaning);
}

// 2. I KNOW / I DON'T KNOW tugmalari
// Eslatma: Bu yerda endi `updateWordStatus` chaqiriladi, u tarjimani o'zi ko'rsatadi.
if (btnKnow) btnKnow.addEventListener('click', () => updateWordStatus(true));
if (btnDontKnow) btnDontKnow.addEventListener('click', () => updateWordStatus(false));

if (btnAddWord) btnAddWord.addEventListener('click', () => dummyAction("So'z qo'shish"));
if (btnStats) btnStats.addEventListener('click', () => dummyAction("Statistika"));
if (btnReset) btnReset.addEventListener('click', resetApp);

// =======================================================
// 6. Ilovani Ishga Tushirish
// =======================================================
function init() {
    renderTopics(); 
    updateCount();
    getNextWord();
}

// Ilovani boshlash
init();
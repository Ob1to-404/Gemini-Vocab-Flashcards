import streamlit as st
import json
import pandas as pd

# --- Fayl Nomlari ---
ENG_FILE = "eng_uzb.json"
UZB_FILE = "uzb_eng.json"

# --- Matn Resurslari (Localization) ---
TEXTS = {
    # ----------------------------------------------------------------------
    # INGLIZ TILI INTERFEYSI (ENG -> UZB rejimini tanlaganda)
    "ENG_UZB": {
        "app_title": "📚 English-Uzbek Vocabulary System",
        "mode_header": "Language Mode",
        "mode_select": "Select Mode:",
        "categories_header": "Categories",
        "mode_name": "English Word",
        "example": "Example",
        "translation_header": "Uzbek Translation",
        "show_translation": "👁️ Show Translation",
        "hide_translation": "↩️ Hide Translation",
        "knowledge_question": "Do you know this word?",
        "i_know": "✅ I KNOW",
        "i_dont_know": "❌ I DON'T KNOW",
        "sidebar_title": "📊 Statistics",
        "total": "Total words",
        "known": "Known",
        "unknown": "Unknown",
        "remaining": "Untested",
        "no_words": "No words found in the selected category.",
        # Yangi qo'shilgan matnlar:
        "list_button_show": "📋 Show All Words List",
        "list_button_hide": "⬅️ Back to Card Mode",
        "list_main_word": "English Word",
        "list_translation": "Uzbek Translation",
        "list_example": "Example Sentence"
    },
    # ----------------------------------------------------------------------
    # O'ZBEK TILI INTERFEYSI (UZB -> ENG rejimini tanlaganda)
    "UZB_ENG": {
        "app_title": "📚 O'zbekcha-Inglizcha Lug'at Tizimi",
        "mode_header": "Til Rejimi",
        "mode_select": "Tanlang:",
        "categories_header": "Mavzular",
        "mode_name": "O'zbekcha so'z",
        "example": "Misol",
        "translation_header": "Inglizcha Tarjimasi",
        "show_translation": "👁️ Tarjimani Ko'rsatish",
        "hide_translation": "↩️ Tarjimani Yashirish",
        "knowledge_question": "Bu so'zni bilasizmi?",
        "i_know": "✅ BILAMAN",
        "i_dont_know": "❌ BILMAYMAN",
        "sidebar_title": "📊 Statistika",
        "total": "Jami so'zlar",
        "known": "Bilinadi",
        "unknown": "Bilinmaydi",
        "remaining": "Tekshirilmagan",
        "no_words": "Tanlangan mavzuda so'zlar topilmadi.",
        # Yangi qo'shilgan matnlar:
        "list_button_show": "📋 Barcha So'zlar Ro'yxatini Ko'rsatish",
        "list_button_hide": "⬅️ Kartochka Rejimiga Qaytish",
        "list_main_word": "O'zbekcha So'z",
        "list_translation": "Inglizcha Tarjimasi",
        "list_example": "Misol Gap"
    }
}

# --- Konfiguratsiya va Ma'lumotlarni Yuklash ---
st.set_page_config(layout="wide", page_title="Shaxsiy Lug'at Ustasi 📚")


@st.cache_resource
def load_vocab_data(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        st.error(f"Error: '{file_name}' not found. Please check file path.")
        return {}
    except json.JSONDecodeError:
        st.error(f"Error: '{file_name}' is in an invalid JSON format.")
        return {}


# --- Session State'ni Initsializatsiya qilish ---
def init_session_state():
    if 'mode' not in st.session_state:
        st.session_state.mode = "Eng -> Uzb"

    if 'VOCAB_DATA' not in st.session_state:
        st.session_state.VOCAB_DATA = load_vocab_data(ENG_FILE)

    if 'current_category' not in st.session_state:
        if st.session_state.VOCAB_DATA:
            st.session_state.current_category = list(st.session_state.VOCAB_DATA.keys())[0]
        else:
            st.session_state.current_category = ""

    if 'word_index' not in st.session_state:
        st.session_state.word_index = 0

    if 'show_translation' not in st.session_state:
        st.session_state.show_translation = False

    if 'user_knowledge' not in st.session_state:
        st.session_state.user_knowledge = {}

    if 'show_list' not in st.session_state:
        st.session_state.show_list = False


init_session_state()


# --- Funksiya: Til Rejimini O'zgartirish ---
def change_language_mode():
    new_mode = st.session_state.mode_selector

    if new_mode != st.session_state.mode:
        st.session_state.mode = new_mode

        if new_mode == "Eng -> Uzb":
            st.session_state.VOCAB_DATA = load_vocab_data(ENG_FILE)
        else:
            st.session_state.VOCAB_DATA = load_vocab_data(UZB_FILE)

        st.session_state.word_index = 0
        st.session_state.show_translation = False
        st.session_state.show_list = False
        st.session_state.current_category = list(st.session_state.VOCAB_DATA.keys())[
            0] if st.session_state.VOCAB_DATA else ""
        st.session_state.user_knowledge = {}

        st.rerun()


# --- Asosiy Funksiyalar ---

def get_current_word_list():
    category = st.session_state.current_category
    return st.session_state.VOCAB_DATA.get(category, [])


def go_to_next_word():
    word_list = get_current_word_list()
    if not word_list: return

    st.session_state.word_index = (st.session_state.word_index + 1) % len(word_list)
    st.session_state.show_translation = False


def update_knowledge(status):
    word_list = get_current_word_list()
    if word_list:
        current_word_obj = word_list[st.session_state.word_index]
        word = current_word_obj['word']
        st.session_state.user_knowledge[word] = status
        go_to_next_word()

    # --- YANGI FUNKSIYA: Ro'yxatni Ko'rsatish ---


def show_all_words_list(current_text, current_data):
    st.header(current_text["list_button_show"])

    all_words = []
    for category, words in current_data.items():
        for item in words:
            all_words.append({
                current_text["list_main_word"]: item['word'],
                current_text["list_translation"]: item['translation'],
                current_text["list_example"]: item['example'],
                "Category": category
            })

    if all_words:
        df = pd.DataFrame(all_words)

        df = df[[current_text["list_main_word"], current_text["list_translation"], "Category",
                 current_text["list_example"]]]

        # use_container_width=True o'rniga width='stretch' ishlatildi
        st.dataframe(df, width='stretch', height=600)
    else:
        st.warning(current_text["no_words"])


# --- Interfeys (UI) ---

CURRENT_TEXT = TEXTS["ENG_UZB"] if st.session_state.mode == "Eng -> Uzb" else TEXTS["UZB_ENG"]

st.title(CURRENT_TEXT["app_title"])

col1, col2, col3 = st.columns([1, 2.5, 0.5])

# 1. Chap Panel: Til va Mavzular (col1)
with col1:
    st.header(CURRENT_TEXT["mode_header"])
    st.selectbox(
        CURRENT_TEXT["mode_select"],
        ("Eng -> Uzb", "Uzb -> Eng"),
        key="mode_selector",
        on_change=change_language_mode
    )

    st.header(CURRENT_TEXT["categories_header"])
    CATEGORIES = list(st.session_state.VOCAB_DATA.keys())
    for category in CATEGORIES:
        is_selected = (category == st.session_state.current_category)
        # use_container_width=True o'rniga width='stretch' ishlatildi
        if st.button(category, width='stretch', type=("primary" if is_selected else "secondary")):
            if category != st.session_state.current_category:
                st.session_state.current_category = category
                st.session_state.word_index = 0
                st.session_state.show_translation = False
                st.session_state.show_list = False
                st.rerun()

            # 3. Kichik Tugma Ustuni (col3)
with col3:
    st.markdown(" ")

    if st.session_state.show_list:
        button_label = CURRENT_TEXT["list_button_hide"]
    else:
        button_label = CURRENT_TEXT["list_button_show"]

    # use_container_width=True o'rniga width='stretch' ishlatildi
    if st.button(button_label, key='toggle_list', width='stretch'):
        st.session_state.show_list = not st.session_state.show_list
        st.rerun()

# 2. O'ng Panel: Karta yoki Ro'yxat (col2)
with col2:
    if st.session_state.show_list:
        show_all_words_list(CURRENT_TEXT, st.session_state.VOCAB_DATA)
    else:
        current_word_list = get_current_word_list()

        if not current_word_list:
            st.warning(CURRENT_TEXT["no_words"])
        else:
            current_word_obj = current_word_list[st.session_state.word_index]
            word = current_word_obj['word']

            st.header(f"➡️ {CURRENT_TEXT['mode_name']}: {word}")
            st.markdown(f"**{CURRENT_TEXT['example']}:** *{current_word_obj.get('example', 'Misol gap mavjud emas.')}*")
            st.markdown("---")

            # Tarjima qismi
            st.subheader(f"{CURRENT_TEXT['translation_header']}:")

            if st.session_state.show_translation:
                st.success(f"**{CURRENT_TEXT['translation_header']}:** {current_word_obj['translation']}")

                # use_container_width=True o'rniga width='stretch' ishlatildi
                st.button(CURRENT_TEXT["hide_translation"],
                          on_click=lambda: st.session_state.update(show_translation=False),
                          width='stretch')

            else:
                st.markdown("### " + ("*" * len(current_word_obj['translation'])))

                # use_container_width=True o'rniga width='stretch' ishlatildi
                st.button(CURRENT_TEXT["show_translation"],
                          on_click=lambda: st.session_state.update(show_translation=True),
                          width='stretch',
                          type="secondary")

            st.markdown("---")
            st.subheader(CURRENT_TEXT["knowledge_question"])

            col_k, col_uk = st.columns(2)

            with col_k:
                # use_container_width=True o'rniga width='stretch' ishlatildi
                st.button(CURRENT_TEXT["i_know"],
                          on_click=update_knowledge,
                          args=('known',),
                          width='stretch',
                          type="primary")
            with col_uk:
                # use_container_width=True o'rniga width='stretch' ishlatildi
                st.button(CURRENT_TEXT["i_dont_know"],
                          on_click=update_knowledge,
                          args=('unknown',),
                          width='stretch',
                          type="secondary")

# --- Pastki Qism: Statistika ---
st.sidebar.markdown("---")
st.sidebar.header(CURRENT_TEXT["sidebar_title"])

total_words = sum(len(v) for v in st.session_state.VOCAB_DATA.values())
known_count = list(st.session_state.user_knowledge.values()).count('known')
unknown_count = list(st.session_state.user_knowledge.values()).count('unknown')
remaining_count = total_words - (known_count + unknown_count)

st.sidebar.markdown(f"*{CURRENT_TEXT['total']}: **{total_words}***")
st.sidebar.markdown(f"*{CURRENT_TEXT['known']}: **{known_count}**")
st.sidebar.markdown(f"*{CURRENT_TEXT['unknown']}: **{unknown_count}**")
st.sidebar.markdown(f"*{CURRENT_TEXT['remaining']}: **{remaining_count}**")

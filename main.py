import streamlit as st
import json

# --- Konfiguratsiya va Ma'lumotlarni Yuklash ---
st.set_page_config(layout="wide", page_title="Shaxsiy Lug'at Ustasi 📚")

DATA_FILE = "name.json"


@st.cache_resource
def load_vocab_data():
    """JSON faylini yuklaydi."""
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        st.error(f"Xatolik: '{DATA_FILE}' fayli topilmadi. Iltimos, fayl mavjudligini tekshiring.")
        return {}
    except json.JSONDecodeError:
        st.error(f"Xatolik: '{DATA_FILE}' fayl noto'g'ri JSON formatida.")
        return {}


# Boshlang'ich ma'lumotlarni yuklash
VOCAB_DATA = load_vocab_data()
CATEGORIES = list(VOCAB_DATA.keys())


# --- Session State'ni Initsializatsiya qilish ---
def init_session_state():
    if 'current_category' not in st.session_state and CATEGORIES:
        st.session_state.current_category = CATEGORIES[0]

    if 'word_index' not in st.session_state:
        st.session_state.word_index = 0

    if 'show_translation' not in st.session_state:
        st.session_state.show_translation = False

    if 'user_knowledge' not in st.session_state:
        st.session_state.user_knowledge = {}


init_session_state()


# --- Asosiy Funksiyalar ---

def get_current_word_list():
    """Tanlangan kategoriya bo'yicha so'zlar ro'yxatini qaytaradi."""
    category = st.session_state.current_category
    return VOCAB_DATA.get(category, [])


def go_to_next_word():
    """Keyingi so'zga o'tish va tarjimani yopish."""
    word_list = get_current_word_list()
    if not word_list:
        return

    st.session_state.word_index = (st.session_state.word_index + 1) % len(word_list)
    st.session_state.show_translation = False  # Keyingi so'zga o'tganda tarjimani yashirish


def update_knowledge(status):
    """'Bilaman' yoki 'Bilmayman' tugmalarini bosishda holatni yangilash va keyingi so'zga o'tish."""
    word_list = get_current_word_list()
    if word_list:
        current_word_obj = word_list[st.session_state.word_index]
        word = current_word_obj['word']
        st.session_state.user_knowledge[word] = status
        go_to_next_word()  # Har doim keyingi so'zga o'tish


# --- Foydalanuvchi Interfeysi (UI) ---

st.title("📚 Shaxsiy Lug'at Yodlash Tizimi")

col1, col2 = st.columns([1, 3])

# --- 1. Chap Panel: Mavzular ---
# --- 1. Chap Panel: Mavzular ---
with col1:
    st.header("Mavzular")
    for category in CATEGORIES:
        is_selected = (category == st.session_state.current_category)
        if st.button(category, use_container_width=True, type=("primary" if is_selected else "secondary")):
            if category != st.session_state.current_category:
                st.session_state.current_category = category
                st.session_state.word_index = 0
                st.session_state.show_translation = False
                st.rerun() # <--- O'ZGARTIRILGAN QATOR: 'experimental_' olib tashlandi

# --- 2. O'ng Panel: So'z Kartochkasi ---
with col2:
    current_word_list = get_current_word_list()

    if not current_word_list:
        st.warning("Tanlangan mavzuda (kategoriyada) so'zlar topilmadi.")
    else:
        current_word_obj = current_word_list[st.session_state.word_index]
        word = current_word_obj['word']

        st.header(f"➡️ So'z: {word}")
        st.markdown(f"**Misol:** *{current_word_obj.get('example', 'Misol gap mavjud emas.')}*")
        st.markdown("---")

        # Tarjima qismi
        st.subheader("Tarjimasi:")

        if st.session_state.show_translation:
            # Tarjima ko'rinib turgan holat
            st.success(f"**Tarjimasi:** {current_word_obj['translation']}")

            # Tarjimani yashirish tugmasi (user tarjimani qayta yashirishi mumkin)
            st.button("↩️ Tarjimani Yashirish",
                      on_click=lambda: st.session_state.update(show_translation=False),
                      use_container_width=True)

        else:
            # Tarjima yashirilgan holat
            st.markdown("### " + ("*" * len(current_word_obj['translation'])))

            # Tarjimani ko'rsatish tugmasi
            st.button("👁️ Tarjimani Ko'rsatish",
                      on_click=lambda: st.session_state.update(show_translation=True),
                      use_container_width=True,
                      type="secondary")

        st.markdown("---")
        st.subheader("Bu so'zni bilasizmi? (Tanlang va keyingi so'zga o'ting)")

        # Bilaman / Bilmayman tugmalari har doim ko'rinib turadi
        col_k, col_uk = st.columns(2)

        with col_k:
            st.button("✅ I KNOW (Bilaman)",
                      on_click=update_knowledge,
                      args=('known',),
                      use_container_width=True,
                      type="primary")
        with col_uk:
            st.button("❌ I DON'T KNOW (Bilmayman)",
                      on_click=update_knowledge,
                      args=('unknown',),
                      use_container_width=True,
                      type="secondary")

# --- Pastki Qism: Statistika ---
st.sidebar.markdown("---")
st.sidebar.header("📊 Statistika")

total_words = sum(len(v) for v in VOCAB_DATA.values())
known_count = list(st.session_state.user_knowledge.values()).count('known')
unknown_count = list(st.session_state.user_knowledge.values()).count('unknown')
remaining_count = total_words - (known_count + unknown_count)

st.sidebar.markdown(f"*Jami so'zlar: **{total_words}***")
st.sidebar.markdown(f"*Bilinadi: **{known_count}**")
st.sidebar.markdown(f"*Bilinmaydi: **{unknown_count}**")
st.sidebar.markdown(f"*Tekshirilmagan: **{remaining_count}**")
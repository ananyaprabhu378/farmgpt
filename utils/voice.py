from gtts import gTTS
import tempfile
import streamlit as st

def speak(text, language="English"):
    try:
        # 🧠 Language mapping
        lang_map = {
            "English": "en",
            "Hindi": "hi",
            "Kannada": "kn",
            "Tamil": "ta",
            "Telugu": "te",
            "Marathi": "mr",
        }

        lang_code = lang_map.get(language, "en")

        # 🧼 Ensure text is string
        if not isinstance(text, str):
            text = str(text)

        clean = text.strip()

        if not clean:
            return

        # 🔥 Remove emojis (important for better voice)
        clean = clean.encode("ascii", "ignore").decode() if language == "English" else clean

        # 🎤 Generate voice
        tts = gTTS(text=clean, lang=lang_code, tld="co.in")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            fname = f.name

        tts.save(fname)

        # 🔊 Play in Streamlit
        st.audio(fname)

    except Exception as e:
        st.error(f"Speech error: {e}")
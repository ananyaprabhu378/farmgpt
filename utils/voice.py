from gtts import gTTS
import tempfile
import streamlit as st

def speak(text, language="English"):
    try:
        lang_map = {
            "English": "en",
            "Hindi": "hi",
            "Kannada": "kn",
            "Tamil": "ta",
            "Telugu": "te",
            "Marathi": "mr",
        }

        lang_code = lang_map.get(language, "en")

        clean = text.strip()

        clean = clean.strip()
        if not clean:
            return

        tts = gTTS(text=clean, lang=lang_code, tld="co.in")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            fname = f.name

        tts.save(fname)

        # ✅ THIS IS THE FIX (plays in browser)
        st.audio(fname)

    except Exception as e:
        st.error(f"Speech error: {e}")
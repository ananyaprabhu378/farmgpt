from gtts import gTTS
import tempfile
import streamlit as st

def speak(text, language="English"):
    try:
        # 🚨 IMPORTANT: stop if empty / None
        if not text:
            st.warning("⚠️ No text received for speech")
            return

        # 🧠 Convert to string safely
        text = str(text)

        # 🧼 Clean text properly
        clean = ""
        for char in text:
            if char.isalnum() or char.isspace():
                clean += char
            else:
                clean += " "

        clean = clean.strip()

        # 🚨 STILL EMPTY → STOP
        if not clean:
            st.warning("⚠️ Text became empty after cleaning")
            return

        # 🧠 Language mapping
        lang_map = {
            "English": "en",
            "Hindi": "hi",
            "Kannada": "kn",
            "Tamil": "ta",
            "Telugu": "te",
            "Marathi": "mr",
        }

        lang_code = "en"

        # 🎤 Generate speech
        tts = gTTS(text=clean, lang="en", tld="co.in")

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            fname = f.name

        tts.save(fname)

        # 🔊 Play audio
        st.audio(fname)

    except Exception as e:
        st.error(f"Speech error: {e}")
from gtts import gTTS
import tempfile
import streamlit as st

def speak(text, language="English"):
    try:
        if not text:
            return

        text = str(text)

        # Clean text — keep language characters too
        clean = ""
        for char in text:
            if char.isalnum() or char.isspace() or ord(char) > 127:
                clean += char
            else:
                clean += " "

        clean = clean.strip()

        if not clean:
            return

        lang_map = {
            "English": ("en", "co.in"),
            "Hindi":   ("hi", "co.in"),
            "Kannada": ("kn", "co.in"),
            "Tamil":   ("ta", "co.in"),
            "Telugu":  ("te", "co.in"),
            "Marathi": ("mr", "co.in"),
        }

        lang_code, tld = lang_map.get(language, ("en", "co.in"))

        tts = gTTS(text=clean, lang=lang_code, tld=tld, slow=False)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            fname = f.name

        tts.save(fname)
        st.audio(fname, autoplay=True)

    except Exception as e:
        st.error(f"Speech error: {e}")
from gtts import gTTS
import tempfile
import streamlit as st

def speak(text, language="English"):
    try:
        # 🚨 1. Check if text exists
        if not text:
            return

        # 🧠 2. Convert to string safely
        text = str(text).strip()

        if not text:
            return

        # 🧼 3. Clean text (VERY IMPORTANT)
        # Only remove newlines, keep all characters (for Kannada/Hindi)
        clean = text.replace("\n", " ").strip()

        # 🎯 4. FORCE ENGLISH VOICE (fix foreign accent issue)
        lang_code = "en"

        # 🎤 5. Generate speech
        tts = gTTS(
            text=clean,
            lang=lang_code,
            tld="co.in",   # Indian voice server
            slow=False
        )

        # 💾 6. Save audio file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            fname = f.name

        tts.save(fname)

        # 🔊 7. Play in Streamlit
        st.audio(fname)

    except Exception as e:
        st.error(f"Speech error: {e}")
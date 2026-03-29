from gtts import gTTS
import tempfile
import os

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
        clean = ""
        for char in text:
            if ord(char) < 8000:
                clean += char
        clean = clean.strip()
        if not clean:
            return
        tts = gTTS(text=clean, lang=lang_code, slow=False)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            fname = f.name
        tts.save(fname)
        os.system(f'start /min wmplayer "{fname}"')
    except Exception as e:
        print(f"Speech error: {e}")
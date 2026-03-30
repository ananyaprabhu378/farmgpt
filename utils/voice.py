import streamlit as st
import streamlit.components.v1 as components

def speak(text, language="English"):
    try:
        # 🚨 1. Check text
        if not text:
            return

        # 🧠 2. Clean text
        text = str(text).replace("\n", " ").replace('"', "'").strip()

        if not text:
            return

        # 🌐 3. Language mapping (natural voices)
        lang_map = {
            "English": "en-IN",
            "Hindi": "hi-IN",
            "Kannada": "kn-IN",
            "Tamil": "ta-IN",
            "Telugu": "te-IN",
            "Marathi": "mr-IN"
        }

        lang_code = lang_map.get(language, "en-IN")

        # 🎤 4. Browser Speech (BEST QUALITY)
        js_code = f"""
        <script>
        var msg = new SpeechSynthesisUtterance("{text}");
        msg.lang = "{lang_code}";
        msg.rate = 1;
        msg.pitch = 1;

        // Stop previous speech
        window.speechSynthesis.cancel();

        // Speak
        window.speechSynthesis.speak(msg);
        </script>
        """

        components.html(js_code, height=0)

    except Exception as e:
        st.error(f"Speech error: {e}")
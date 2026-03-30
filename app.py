import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime
from utils.llm import get_llm_response
from utils.weather import get_weather
from utils.news import get_agri_articles
from utils.voice import speak
from utils.market import get_market_prices
from data.schemes import SCHEMES
import urllib.parse
from data.crops import CROP_DATA, DEFAULT_CROPS
from utils.auth import signup, login, save_user_data, get_user_data
import streamlit as st
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# ── Page Config (MUST be first Streamlit call) ────────────
st.set_page_config(page_title="Dhara-AI 🌾", page_icon="🌾", layout="wide")

# ── LOGIN SYSTEM ─────────────────────

if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user is None:
    st.title("🔐 Login to Dhara-AI")

    tab1, tab2 = st.tabs(["Login", "Signup"])

    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if login(username, password):
                st.session_state.user = username
                st.success("Logged in!")
                st.rerun()
            else:
                st.error("Invalid credentials")

    with tab2:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Signup"):
            if signup(new_user, new_pass):
                st.success("Account created!")
            else:
                st.error("User exists")

    st.stop()

# ── Global CSS ────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap');

:root {
    --green-primary: #4ade80;
    --green-deep:    #166534;
    --green-glow:    rgba(74,222,128,0.25);
    --bg-main:       #081a0c;
    --bg-card:       rgba(255,255,255,0.04);
    --bg-card-hover: rgba(255,255,255,0.07);
    --border:        rgba(74,222,128,0.18);
    --text-primary:  #e2f5e8;
    --text-muted:    #86efac;
    --text-dim:      #4ade8077;
}

*, *::before, *::after { box-sizing: border-box; }

/* ── App background ── */
.stApp {
    background: var(--bg-main);
    background-image:
        radial-gradient(ellipse 80% 50% at 10% 5%,  rgba(74,222,128,0.07) 0%, transparent 60%),
        radial-gradient(ellipse 60% 40% at 90% 95%, rgba(22,101,52,0.12)  0%, transparent 60%);
    font-family: 'Sora', sans-serif;
}

/* ── Sidebar ── */
section[data-testid="stSidebar"] {
    background: #040f06 !important;
    border-right: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] > div { padding-top: 1.5rem; }
section[data-testid="stSidebar"] * { color: var(--text-primary) !important; }
section[data-testid="stSidebar"] .stRadio > label {
    font-size: 13px !important;
    font-weight: 500 !important;
    letter-spacing: 0.3px;
}

/* ── Typography ── */
h1 {
    font-family: 'Space Mono', monospace !important;
    color: var(--green-primary) !important;
    font-size: clamp(1.4rem, 3vw, 2rem) !important;
    letter-spacing: -1px !important;
    text-shadow: 0 0 40px var(--green-glow), 0 0 80px rgba(74,222,128,0.1);
    margin-bottom: 0 !important;
}
h2, h3 {
    font-family: 'Space Mono', monospace !important;
    color: var(--green-primary) !important;
    letter-spacing: -0.5px !important;
}
p, li, span, div, label { color: var(--text-primary); font-family: 'Sora', sans-serif; }
.stCaption, [data-testid="stCaption"] {
    color: var(--text-muted) !important;
    font-size: 12px !important;
    letter-spacing: 0.3px;
}
.stMarkdown strong { color: var(--green-primary) !important; }

/* ── Metric cards ── */
[data-testid="metric-container"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
    padding: 14px 16px !important;
    backdrop-filter: blur(12px);
    transition: border-color 0.2s, background 0.2s;
}
[data-testid="metric-container"]:hover {
    background: var(--bg-card-hover) !important;
    border-color: rgba(74,222,128,0.35) !important;
}
[data-testid="metric-container"] label {
    color: var(--text-muted) !important;
    font-size: 10px !important;
    font-weight: 600 !important;
    letter-spacing: 1.2px !important;
    text-transform: uppercase !important;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 28px !important;
    font-weight: 700 !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, #166534 0%, #15803d 50%, #16a34a 100%) !important;
    color: #ffffff !important;
    border: 1px solid rgba(74,222,128,0.3) !important;
    border-radius: 10px !important;
    height: 46px !important;
    width: 100% !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 600 !important;
    font-size: 14px !important;
    letter-spacing: 0.4px !important;
    transition: all 0.25s ease !important;
    box-shadow: 0 4px 15px rgba(22,101,52,0.4), inset 0 1px 0 rgba(255,255,255,0.1) !important;
    cursor: pointer !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(74,222,128,0.35), inset 0 1px 0 rgba(255,255,255,0.15) !important;
    border-color: rgba(74,222,128,0.5) !important;
    background: linear-gradient(135deg, #15803d 0%, #16a34a 50%, #22c55e 100%) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── Inputs ── */
.stTextInput > div > div > input {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--text-primary) !important;
    font-family: 'Sora', sans-serif !important;
    font-size: 14px !important;
    padding: 10px 14px !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}
.stTextInput > div > div > input:focus {
    border-color: var(--green-primary) !important;
    box-shadow: 0 0 0 3px rgba(74,222,128,0.12) !important;
    outline: none !important;
}
.stTextInput > div > div > input::placeholder { color: #4ade8055 !important; }

/* ── Selectbox ── */
.stSelectbox [data-baseweb="select"] > div {
    background: rgba(0,0,0,0.6) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: #ffffff !important;
    font-family: 'Sora', sans-serif !important;
}
.stSelectbox [data-baseweb="select"] > div:hover {
    border-color: rgba(74,222,128,0.4) !important;
}

/* ── Chat input ── */
[data-testid="stChatInput"] {
    background: rgba(255,255,255,0.04) !important;
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
}
[data-testid="stChatInput"] textarea {
    background: transparent !important;
    color: var(--text-primary) !important;
    font-family: 'Sora', sans-serif !important;
    font-size: 14px !important;
}
[data-testid="stChatInput"] textarea::placeholder { color: #4ade8044 !important; }

/* ── Chat messages ── */
[data-testid="stChatMessage"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
    padding: 14px 18px !important;
    backdrop-filter: blur(10px);
    margin-bottom: 10px !important;
    transition: border-color 0.2s;
}
[data-testid="stChatMessage"]:hover { border-color: rgba(74,222,128,0.3) !important; }

/* ── Alert boxes ── */
.stSuccess {
    background: rgba(74,222,128,0.08) !important;
    border: 1px solid rgba(74,222,128,0.3) !important;
    border-radius: 12px !important;
    color: #bbf7d0 !important;
}
.stInfo {
    background: rgba(56,189,248,0.08) !important;
    border: 1px solid rgba(56,189,248,0.25) !important;
    border-radius: 12px !important;
    color: #bae6fd !important;
}
.stError {
    background: rgba(248,113,113,0.08) !important;
    border: 1px solid rgba(248,113,113,0.25) !important;
    border-radius: 12px !important;
    color: #fecaca !important;
}
.stWarning {
    background: rgba(251,191,36,0.08) !important;
    border: 1px solid rgba(251,191,36,0.25) !important;
    border-radius: 12px !important;
    color: #fde68a !important;
}

/* ── Dataframe / Table ── */
[data-testid="stDataFrame"] {
    border: 1px solid var(--border) !important;
    border-radius: 14px !important;
    overflow: hidden !important;
}
[data-testid="stDataFrame"] thead th {
    background: rgba(74,222,128,0.12) !important;
    color: var(--green-primary) !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    letter-spacing: 0.8px !important;
    text-transform: uppercase !important;
    padding: 10px 14px !important;
    border-bottom: 1px solid var(--border) !important;
}
[data-testid="stDataFrame"] tbody td {
    color: var(--text-primary) !important;
    font-size: 13px !important;
    padding: 9px 14px !important;
    border-bottom: 1px solid rgba(74,222,128,0.07) !important;
}
[data-testid="stDataFrame"] tbody tr:hover td {
    background: rgba(74,222,128,0.05) !important;
}

/* ── Expander ── */
.streamlit-expanderHeader {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--green-primary) !important;
    font-weight: 600 !important;
    font-family: 'Sora', sans-serif !important;
    transition: background 0.2s !important;
}
.streamlit-expanderHeader:hover { background: var(--bg-card-hover) !important; }
.streamlit-expanderContent {
    background: rgba(255,255,255,0.02) !important;
    border: 1px solid var(--border) !important;
    border-top: none !important;
    border-radius: 0 0 10px 10px !important;
}

/* ── Divider ── */
hr { border-color: var(--border) !important; margin: 1rem 0 !important; }

/* ── Spinner ── */
.stSpinner > div { border-top-color: var(--green-primary) !important; }

/* ── Radio buttons ── */
.stRadio [data-testid="stMarkdownContainer"] p { color: var(--text-primary) !important; }
.stRadio label { gap: 8px !important; padding: 6px 0 !important; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: rgba(255,255,255,0.02); }
::-webkit-scrollbar-thumb { background: rgba(74,222,128,0.25); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: rgba(74,222,128,0.4); }

/* ── Toast ── */
[data-testid="stToast"] {
    background: rgba(22,101,52,0.9) !important;
    border: 1px solid var(--green-primary) !important;
    border-radius: 10px !important;
    backdrop-filter: blur(12px) !important;
}


/*  FIX TEXT INPUT (Your state, city, etc.) */
.stTextInput input {
    color: #ffffff !important;
    background-color: rgba(0,0,0,0.5) !important;
}

/* 🔥 FIX SELECTBOX MAIN FIELD */
.stSelectbox div[data-baseweb="select"] > div {
    color: #ffffff !important;
    background-color: rgba(0,0,0,0.5) !important;
}

/* 🔥 FIX SELECTED VALUE TEXT */
[data-baseweb="select"] span {
    color: #ffffff !important;
}

/* 🔥 DROPDOWN MENU BACKGROUND */
div[role="listbox"] {
    background-color: #081a0c !important;
}

/* 🔥 DROPDOWN OPTIONS TEXT */
div[role="option"] {
    color: #ffffff !important;
}

/* 🔥 LABEL TEXT (Your state, crop, language) */
.stTextInput label,
.stSelectbox label {
    color: #86efac !important;
    font-weight: 500 !important;
}

/* 🔥 PLACEHOLDER TEXT */
.stTextInput input::placeholder {
    color: #86efac !important;
}

</style>
""", unsafe_allow_html=True)



# ── Language Config ───────────────────────────────────────
LANGUAGE_CODES = {
    "English": "en-IN",
    "Hindi": "hi-IN",
    "Kannada": "kn-IN",
    "Tamil": "ta-IN",
    "Telugu": "te-IN",
    "Marathi": "mr-IN",
}

UI_TEXT = {
    "English": {
        "title": "🌾 Dhara-AI – AI Advisory Assistant",
        "caption": "Your smart farming companion — ask anything about your crops!",
        "speak_btn": "🎙️ Click to Speak",
        "listening": "Listening... Speak now!",
        "chat_placeholder": "Describe your crop problem...",
        "stop_btn": "⏹️ Stop",
        "menu": "Navigate",
        "stats": "📊 Stats",
        "messages": "Messages",
        "alerts": "Alerts",
        "language": "Language",
        "weather": "🌤️ Weather",
        "lang_tab": "🌐 Language",
        "calendar": "📅 Harvest Calendar",
        "articles": "📰 Agri Articles",
        "market": "📈 Market Prices",
        "schemes": "🏛️ Govt Schemes",
        "notif": "🔔 Notifications",
        "your_city": "Your city:",
        "get_advice": "Get Farming Advice",
        "set_lang": "Set Language",
        "your_crop": "Your crop:",
        "your_region": "Your region:",
        "gen_calendar": "Generate Calendar",
        "fetch_articles": "Fetch Articles",
        "farmer_type": "Farmer type:",
        "get_schemes": "Get AI Recommendations",
        "clear_all": "🗑️ Clear All",
        "no_notif": "No notifications yet!",
        "weather_err": "❌ Check OPENWEATHER_API_KEY",
        "articles_err": "❌ Check NEWSDATA_API_KEY",
        "your_commodity": "Select crop:",
        "your_state": "Your state:",
        "get_prices": "Get Market Prices",
    },
    "Kannada": {
        "title": "🌾 ಫಾರ್ಮ್‌GPT – AI ಕೃಷಿ ಸಹಾಯಕ",
        "caption": "ನಿಮ್ಮ ಬೆಳೆಗಳ ಬಗ್ಗೆ ಯಾವುದೇ ಪ್ರಶ್ನೆ ಕೇಳಿ!",
        "speak_btn": "🎙️ ಮಾತನಾಡಲು ಕ್ಲಿಕ್ ಮಾಡಿ",
        "listening": "ಕೇಳುತ್ತಿದ್ದೇನೆ... ಈಗ ಮಾತನಾಡಿ!",
        "chat_placeholder": "ನಿಮ್ಮ ಬೆಳೆ ಸಮಸ್ಯೆ ವಿವರಿಸಿ...",
        "stop_btn": "⏹️ ನಿಲ್ಲಿಸಿ",
        "menu": "ಮೆನು",
        "stats": "📊 ಅಂಕಿಅಂಶ",
        "messages": "ಸಂದೇಶಗಳು",
        "alerts": "ಎಚ್ಚರಿಕೆಗಳು",
        "language": "ಭಾಷೆ",
        "weather": "🌤️ ಹವಾಮಾನ",
        "lang_tab": "🌐 ಭಾಷೆ",
        "calendar": "📅 ಕೊಯ್ಲು ಕ್ಯಾಲೆಂಡರ್",
        "articles": "📰 ಕೃಷಿ ಸುದ್ದಿ",
        "market": "📈 ಮಾರುಕಟ್ಟೆ ಬೆಲೆಗಳು",
        "schemes": "🏛️ ಸರ್ಕಾರಿ ಯೋಜನೆಗಳು",
        "notif": "🔔 ಅಧಿಸೂಚನೆಗಳು",
        "your_city": "ನಿಮ್ಮ ನಗರ:",
        "get_advice": "ಕೃಷಿ ಸಲಹೆ ಪಡೆಯಿರಿ",
        "set_lang": "ಭಾಷೆ ಹೊಂದಿಸಿ",
        "your_crop": "ನಿಮ್ಮ ಬೆಳೆ:",
        "your_region": "ನಿಮ್ಮ ಪ್ರದೇಶ:",
        "gen_calendar": "ಕ್ಯಾಲೆಂಡರ್ ರಚಿಸಿ",
        "fetch_articles": "ಲೇಖನಗಳನ್ನು ತರಿಸಿ",
        "farmer_type": "ರೈತ ವಿಧ:",
        "get_schemes": "AI ಶಿಫಾರಸುಗಳು",
        "clear_all": "🗑️ ಎಲ್ಲ ತೆರವುಗೊಳಿಸಿ",
        "no_notif": "ಇನ್ನೂ ಅಧಿಸೂಚನೆಗಳಿಲ್ಲ!",
        "weather_err": "❌ OPENWEATHER_API_KEY ಪರಿಶೀಲಿಸಿ",
        "articles_err": "❌ NEWSDATA_API_KEY ಪರಿಶೀಲಿಸಿ",
        "your_commodity": "ಬೆಳೆ ಆಯ್ಕೆ:",
        "your_state": "ನಿಮ್ಮ ರಾಜ್ಯ:",
        "get_prices": "ಮಾರುಕಟ್ಟೆ ಬೆಲೆ ಪಡೆಯಿರಿ",
    },
    "Hindi": {
        "title": "🌾 फार्मGPT – AI कृषि सहायक",
        "caption": "अपनी फसल के बारे में कुछ भी पूछें!",
        "speak_btn": "🎙️ बोलने के लिए क्लिक करें",
        "listening": "सुन रहा हूँ... अभी बोलें!",
        "chat_placeholder": "अपनी फसल की समस्या बताएं...",
        "stop_btn": "⏹️ रोकें",
        "menu": "मेनू",
        "stats": "📊 आँकड़े",
        "messages": "संदेश",
        "alerts": "अलर्ट",
        "language": "भाषा",
        "weather": "🌤️ मौसम",
        "lang_tab": "🌐 भाषा",
        "calendar": "📅 फसल कैलेंडर",
        "articles": "📰 कृषि समाचार",
        "market": "📈 बाजार भाव",
        "schemes": "🏛️ सरकारी योजनाएं",
        "notif": "🔔 सूचनाएं",
        "your_city": "आपका शहर:",
        "get_advice": "कृषि सलाह पाएं",
        "set_lang": "भाषा सेट करें",
        "your_crop": "आपकी फसल:",
        "your_region": "आपका क्षेत्र:",
        "gen_calendar": "कैलेंडर बनाएं",
        "fetch_articles": "लेख लाएं",
        "farmer_type": "किसान प्रकार:",
        "get_schemes": "AI सुझाव पाएं",
        "clear_all": "🗑️ सब साफ करें",
        "no_notif": "अभी कोई सूचना नहीं!",
        "weather_err": "❌ OPENWEATHER_API_KEY जांचें",
        "articles_err": "❌ NEWSDATA_API_KEY जांचें",
        "your_commodity": "फसल चुनें:",
        "your_state": "आपका राज्य:",
        "get_prices": "भाव देखें",
    },
    "Tamil": {
        "title": "🌾 பண்ணைGPT – AI வேளாண் உதவியாளர்",
        "caption": "உங்கள் பயிர்களைப் பற்றி எதையும் கேளுங்கள்!",
        "speak_btn": "🎙️ பேச கிளிக் செய்யுங்கள்",
        "listening": "கேட்கிறேன்... இப்போது பேசுங்கள்!",
        "chat_placeholder": "உங்கள் பயிர் பிரச்சனையை விவரிக்கவும்...",
        "stop_btn": "⏹️ நிறுத்து",
        "menu": "மெனு",
        "stats": "📊 புள்ளிவிவரங்கள்",
        "messages": "செய்திகள்",
        "alerts": "எச்சரிக்கைகள்",
        "language": "மொழி",
        "weather": "🌤️ வானிலை",
        "lang_tab": "🌐 மொழி",
        "calendar": "📅 அறுவடை நாட்காட்டி",
        "articles": "📰 வேளாண் செய்திகள்",
        "market": "📈 சந்தை விலைகள்",
        "schemes": "🏛️ அரசு திட்டங்கள்",
        "notif": "🔔 அறிவிப்புகள்",
        "your_city": "உங்கள் நகரம்:",
        "get_advice": "விவசாய ஆலோசனை பெறுங்கள்",
        "set_lang": "மொழி அமைக்கவும்",
        "your_crop": "உங்கள் பயிர்:",
        "your_region": "உங்கள் பகுதி:",
        "gen_calendar": "நாட்காட்டி உருவாக்கவும்",
        "fetch_articles": "கட்டுரைகள் கொண்டு வாருங்கள்",
        "farmer_type": "விவசாயி வகை:",
        "get_schemes": "AI பரிந்துரைகள்",
        "clear_all": "🗑️ அனைத்தையும் அழி",
        "no_notif": "இன்னும் அறிவிப்புகள் இல்லை!",
        "weather_err": "❌ OPENWEATHER_API_KEY சரிபார்க்கவும்",
        "articles_err": "❌ NEWSDATA_API_KEY சரிபார்க்கவும்",
        "your_commodity": "பயிர் தேர்ந்தெடு:",
        "your_state": "உங்கள் மாநிலம்:",
        "get_prices": "விலை பெறுங்கள்",
    },
    "Telugu": {
        "title": "🌾 వ్యవసాయGPT – AI వ్యవసాయ సహాయకుడు",
        "caption": "మీ పంటల గురించి ఏదైనా అడగండి!",
        "speak_btn": "🎙️ మాట్లాడటానికి క్లిక్ చేయండి",
        "listening": "వింటున్నాను... ఇప్పుడు మాట్లాడండి!",
        "chat_placeholder": "మీ పంట సమస్యను వివరించండి...",
        "stop_btn": "⏹️ ఆపు",
        "menu": "మెను",
        "stats": "📊 గణాంకాలు",
        "messages": "సందేశాలు",
        "alerts": "హెచ్చరికలు",
        "language": "భాష",
        "weather": "🌤️ వాతావరణం",
        "lang_tab": "🌐 భాష",
        "calendar": "📅 పంట క్యాలెండర్",
        "articles": "📰 వ్యవసాయ వార్తలు",
        "market": "📈 మార్కెట్ ధరలు",
        "schemes": "🏛️ ప్రభుత్వ పథకాలు",
        "notif": "🔔 నోటిఫికేషన్లు",
        "your_city": "మీ నగరం:",
        "get_advice": "వ్యవసాయ సలహా పొందండి",
        "set_lang": "భాష సెట్ చేయండి",
        "your_crop": "మీ పంట:",
        "your_region": "మీ ప్రాంతం:",
        "gen_calendar": "క్యాలెండర్ రూపొందించండి",
        "fetch_articles": "వ్యాసాలు తీసుకురండి",
        "farmer_type": "రైతు రకం:",
        "get_schemes": "AI సిఫార్సులు",
        "clear_all": "🗑️ అన్నీ తొలగించు",
        "no_notif": "ఇంకా నోటిఫికేషన్లు లేవు!",
        "weather_err": "❌ OPENWEATHER_API_KEY తనిఖీ చేయండి",
        "articles_err": "❌ NEWSDATA_API_KEY తనిఖీ చేయండి",
        "your_commodity": "పంట ఎంచుకోండి:",
        "your_state": "మీ రాష్ట్రం:",
        "get_prices": "ధరలు చూడండి",
    },
    "Marathi": {
        "title": "🌾 शेतGPT – AI कृषी सहाय्यक",
        "caption": "आपल्या पिकांबद्दल काहीही विचारा!",
        "speak_btn": "🎙️ बोलण्यासाठी क्लिक करा",
        "listening": "ऐकतोय... आता बोला!",
        "chat_placeholder": "तुमच्या पिकाची समस्या सांगा...",
        "stop_btn": "⏹️ थांबा",
        "menu": "मेनू",
        "stats": "📊 आकडेवारी",
        "messages": "संदेश",
        "alerts": "सूचना",
        "language": "भाषा",
        "weather": "🌤️ हवामान",
        "lang_tab": "🌐 भाषा",
        "calendar": "📅 कापणी दिनदर्शिका",
        "articles": "📰 कृषी बातम्या",
        "market": "📈 बाजार भाव",
        "schemes": "🏛️ सरकारी योजना",
        "notif": "🔔 सूचना",
        "your_city": "तुमचे शहर:",
        "get_advice": "शेती सल्ला मिळवा",
        "set_lang": "भाषा सेट करा",
        "your_crop": "तुमचे पीक:",
        "your_region": "तुमचा प्रदेश:",
        "gen_calendar": "दिनदर्शिका तयार करा",
        "fetch_articles": "लेख आणा",
        "farmer_type": "शेतकरी प्रकार:",
        "get_schemes": "AI शिफारसी",
        "clear_all": "🗑️ सर्व साफ करा",
        "no_notif": "अजून सूचना नाहीत!",
        "weather_err": "❌ OPENWEATHER_API_KEY तपासा",
        "articles_err": "❌ NEWSDATA_API_KEY तपासा",
        "your_commodity": "पीक निवडा:",
        "your_state": "तुमचे राज्य:",
        "get_prices": "भाव पहा",
    },
}

# ── Session State ─────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "notifications" not in st.session_state:
    st.session_state.notifications = []
if "language" not in st.session_state:
    st.session_state.language = "English"
if "voice_query" not in st.session_state:
    st.session_state.voice_query = ""

# ── Get UI text ───────────────────────────────────────────
ui = UI_TEXT.get(st.session_state.language, UI_TEXT["English"])
lang_code = LANGUAGE_CODES.get(st.session_state.language, "en-IN")

# ── Header ────────────────────────────────────────────────
st.markdown(f"""
<div style="
padding:14px 18px;
border-radius:12px;
background:rgba(74,222,128,0.08);
border:1px solid rgba(74,222,128,0.2);
margin-bottom:12px;
">
<h3 style="margin:0;color:#4ade80;">🌾 Dhara-AI</h3>
<p style="margin:2px 0 0;font-size:13px;color:#86efac;">
{ui["caption"]}
</p>
</div>
""", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"## ⚙️ {ui['menu']}")
    tab = st.radio(ui["menu"], [
        ui["weather"],
        ui["lang_tab"],
        ui["calendar"],
        ui["articles"],
        ui["market"],
        ui["schemes"],
        ui["notif"],
    ])

    # ── Weather ───────────────────────────────────────────
    if tab == ui["weather"]:
        st.markdown(f"### {ui['weather']}")
        city = st.text_input(ui["your_city"], "Bengaluru")
        if city:
            weather = get_weather(city)
            if weather:
                st.success(weather["display"])
                if st.button(ui["get_advice"]):
                    with st.spinner("..."):
                        advice = get_llm_response([{
                            "role": "user",
                            "content": f"Weather in {city}: {weather['display']}. Give farming advice in {st.session_state.language}."
                        }], st.session_state.language)
                        st.info(advice)
                        speak(advice, st.session_state.language)
                        st.session_state.notifications.append(
                            f"{ui['weather']} {city} — {datetime.now().strftime('%H:%M')}"
                        )
            else:
                st.error(ui["weather_err"])

    # ── Language ──────────────────────────────────────────
    elif tab == ui["lang_tab"]:
        st.markdown(f"### {ui['lang_tab']}")
        lang = st.selectbox(ui["language"], list(LANGUAGE_CODES.keys()))
        if st.button(ui["set_lang"]):
            st.session_state.language = lang
            st.session_state.notifications.append(
                f"🌐 → {lang} — {datetime.now().strftime('%H:%M')}"
            )
            st.rerun()

    # ── Harvest Calendar ──────────────────────────────────
    elif tab == ui["calendar"]:
        st.markdown(f"### {ui['calendar']}")

        from data.crops import CROP_DATA, DEFAULT_CROPS

        crop = st.selectbox(ui["your_crop"], DEFAULT_CROPS)
        region = st.text_input(ui["your_region"], "Karnataka")

        if st.button(ui["gen_calendar"]):

            crop_info = CROP_DATA.get(crop, {})

            if not crop_info:
                st.error("No data found for this crop")
            else:
                # 🌤 Weather
                weather = get_weather(region)
                weather_display = weather["display"] if weather else "Weather unavailable"

                # 🎯 Summary Cards
                col1, col2, col3 = st.columns(3)
                col1.metric("🌾 Crop", crop)
                col2.metric("⏱ Duration", crop_info.get("duration", "-"))
                col3.metric("💧 Water", crop_info.get("water", "-"))

                st.caption(f"🌤 {weather_display}")

                st.divider()

                # 📊 TABLE (REAL DATA)
                import pandas as pd
                df = pd.DataFrame(crop_info.get("calendar", []))

                if not df.empty:
                    st.dataframe(df, use_container_width=True)
    
                else:
                    st.warning("No calendar data available")


                st.divider()

                # 💡 INSIGHT
                if crop_info.get("insights"):
                    st.info(f"💡 {crop_info['insights']}")

            st.session_state.notifications.append(
                f"{ui['calendar']} {crop} — {datetime.now().strftime('%H:%M')}"
            )

    # ── Agri Articles ─────────────────────────────────────
    elif tab == ui["articles"]:
        st.markdown(f"### {ui['articles']}")
        if st.button(ui["fetch_articles"]):
            with st.spinner("..."):
                articles = get_agri_articles()
                if articles:
                    for a in articles:
                        st.markdown(f"**{a.get('title', 'No Title')}**")

                        source = a.get("source_id", a.get("source", "Unknown"))
                        date = str(a.get("pubDate", a.get("date", "")))[:10]
                        st.caption(f"🗞️ {source} | {date}")
                        desc = a.get("description", a.get("content", ""))
                        if desc:
                            st.write(str(desc)[:200])
                        link = a.get("link", a.get("url", ""))
                        if link:
                            st.markdown(f"[↗️ Read more]({link})")
                        st.divider()
                    st.session_state.notifications.append(
                        f"{ui['articles']} — {datetime.now().strftime('%H:%M')}"
                    )
                else:
                    st.error(ui["articles_err"])

    # ── Market Prices ─────────────────────────────────────
    elif tab == ui["market"]:
        st.markdown(f"### {ui['market']}")

        commodity = st.selectbox(ui["your_commodity"], [
            "Tomato", "Potato", "Onion", "Rice",
            "Wheat", "Cotton", "Sugarcane", "Maize",
            "Chilli", "Groundnut", "Soybean", "Banana"
        ])

        state = st.text_input(ui["your_state"], "Karnataka")

        if st.button(ui["get_prices"]):
            with st.spinner("Fetching prices..."):

                result = get_market_prices(commodity, state)

                if not result:
                    st.error("❌ Could not fetch prices")
                    st.stop()

                data = result.get("data", [])

                # 🔥 HANDLE LIST (API case)
                if isinstance(data, list):
                    if len(data) == 0:
                        st.warning("No data available")
                    else:
                        st.success("✅ Live Market Prices")

                        for p in data:
                            col1, col2, col3 = st.columns(3)

                            with col1:
                                st.metric("💰 Min", f"₹{p.get('min_price','N/A')}")
                            with col2:
                                st.metric("💰 Modal", f"₹{p.get('modal_price','N/A')}")
                            with col3:
                                st.metric("💰 Max", f"₹{p.get('max_price','N/A')}")

                            st.caption(f"📍 {p.get('market','')} | 📅 {p.get('date','')}")
                            st.divider()

                # 🔥 HANDLE DICT (AI case)
                elif isinstance(data, dict):
                    st.info("🤖 AI Estimated Prices")

                    st.markdown(f"**{data.get('commodity','')} in {data.get('state','')}**")

                    trend = data.get("trend", "Stable")

                    if trend == "Rising":
                        st.success(f"📈 Trend: {trend}")
                    elif trend == "Falling":
                        st.error(f"📉 Trend: {trend}")
                    else:
                        st.warning(f"➡️ Trend: {trend}")

                    for m in data.get("markets", []):
                        col1, col2, col3 = st.columns(3)

                        with col1:
                            st.metric("💰 Min", f"₹{m.get('min_price','N/A')}")
                        with col2:
                            st.metric("💰 Modal", f"₹{m.get('modal_price','N/A')}")
                        with col3:
                            st.metric("💰 Max", f"₹{m.get('max_price','N/A')}")

                        st.caption(f"📍 {m.get('market','')} | 📅 {m.get('date','')}")
                        st.divider()

                    if data.get("tip"):
                        st.info(f"💡 {data['tip']}")

                st.session_state.notifications.append(
                    f"📈 {commodity} prices — {datetime.now().strftime('%H:%M')}"
                )

    # ── Govt Schemes ──────────────────────────────────────
    elif tab == ui["schemes"]:
        st.markdown(f"### {ui['schemes']}")
        farmer_type = st.selectbox(ui["farmer_type"], [
            "Small & Marginal Farmer",
            "Large Scale Farmer",
            "Organic Farmer",
            "Women Farmer"
        ])
        for s in SCHEMES:
            with st.expander(f"📋 {s['name']}"):
                st.markdown(f"**Benefit:** {s['benefit']}")
                st.markdown(f"**Eligibility:** {s['eligibility']}")
                st.markdown(f"**Apply:** {s['apply']}")
        if st.button(ui["get_schemes"]):
            with st.spinner("..."):
                rec = get_llm_response([{
                    "role": "user",
                    "content": f"Top 3 govt schemes for {farmer_type} in India with reasons. Respond entirely in {st.session_state.language}."
                }], st.session_state.language)
                st.info(rec)
                speak(rec, st.session_state.language)
                st.session_state.notifications.append(
                    f"{ui['schemes']} — {datetime.now().strftime('%H:%M')}"
                )

    # ── Notifications ─────────────────────────────────────
    elif tab == ui["notif"]:
        st.markdown(f"### {ui['notif']}")
        if st.session_state.notifications:
            for n in reversed(st.session_state.notifications):
                st.info(n)
            if st.button(ui["clear_all"]):
                st.session_state.notifications = []
                st.rerun()
        else:
            st.info(ui["no_notif"])

# ── Main Chat ─────────────────────────────────────────────
col1, col2 = st.columns([3, 1])

with col1:

    # ── Process pending voice query ───────────────────────
    if st.session_state.voice_query:
        query = st.session_state.voice_query
        st.session_state.voice_query = ""
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.markdown(f"🎙️ *{query}*")
        with st.chat_message("assistant"):
            with st.spinner("🤖 ..."):
                reply = get_llm_response(
                    st.session_state.messages,
                    st.session_state.language
                )
                st.markdown(reply)
                st.session_state.messages.append({
                    "role": "assistant", "content": reply
                })
                speak(reply, st.session_state.language)
                st.session_state.notifications.append(
                    f"🎙️ — {datetime.now().strftime('%H:%M')}"
                )

    # ── Voice Input Component ─────────────────────────────
    components.html(f"""
        <style>
            body {{ margin: 0; font-family: 'Sora', sans-serif; }}
            #mic-btn {{
                background: linear-gradient(135deg, #166534, #16a34a);
                color: white;
                border: 1px solid rgba(74,222,128,0.4);
                padding: 14px 0;
                font-size: 15px;
                font-weight: 600;
                border-radius: 10px;
                cursor: pointer;
                width: 100%;
                letter-spacing: 0.3px;
                box-shadow: 0 4px 15px rgba(22,101,52,0.4);
                transition: all 0.25s ease;
            }}
            #mic-btn:hover {{
                background: linear-gradient(135deg, #15803d, #22c55e);
                box-shadow: 0 6px 22px rgba(74,222,128,0.35);
                transform: translateY(-1px);
            }}
            #mic-btn.listening {{
                background: linear-gradient(135deg, #991b1b, #dc2626);
                border-color: rgba(248,113,113,0.4);
                animation: pulse 1.2s infinite;
            }}
            @keyframes pulse {{
                0%,100% {{ opacity:1; box-shadow: 0 4px 15px rgba(220,38,38,0.3); }}
                50%      {{ opacity:0.8; box-shadow: 0 4px 25px rgba(220,38,38,0.6); }}
            }}
            #status {{
                margin-top: 8px;
                font-size: 13px;
                color: #86efac;
                letter-spacing: 0.2px;
            }}
            #transcript {{
                margin-top: 10px;
                padding: 10px 14px;
                background: rgba(74,222,128,0.08);
                border: 1px solid rgba(74,222,128,0.25);
                border-radius: 8px;
                font-size: 14px;
                color: #d1fae5;
                display: none;
                border-left: 3px solid #4ade80;
            }}
        </style>

        <button id="mic-btn" onclick="toggleMic()">{ui['speak_btn']}</button>
        <div id="status">🗣️ {ui['listening']}</div>
        <div id="transcript"></div>

        <script>
            const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
            if (!SR) {{
                document.getElementById('status').textContent = '❌ Use Google Chrome!';
            }} else {{
                const r = new SR();
                r.lang = '{lang_code}';
                r.continuous = false;
                r.interimResults = false;
                let on = false;

                function toggleMic() {{
                    if (!on) {{
                        r.start(); on = true;
                        document.getElementById('mic-btn').textContent = '{ui["stop_btn"]}';
                        document.getElementById('mic-btn').classList.add('listening');
                        document.getElementById('status').textContent = '🎙️ {ui["listening"]}';
                    }} else {{ r.stop(); }}
                }}

                r.onresult = function(e) {{
                    const text = e.results[0][0].transcript;
                    document.getElementById('transcript').style.display = 'block';
                    document.getElementById('transcript').textContent = '🗣️ ' + text;
                    document.getElementById('status').textContent = '✅ Sending...';
                    const url = new URL(window.parent.location.href);
                    url.searchParams.set('voice', encodeURIComponent(text));
                    window.parent.history.replaceState(null, '', url);
                    window.parent.location.reload();
                }};

                r.onend = function() {{
                    on = false;
                    document.getElementById('mic-btn').textContent = '{ui["speak_btn"]}';
                    document.getElementById('mic-btn').classList.remove('listening');
                }};

                r.onerror = function(e) {{
                    on = false;
                    document.getElementById('mic-btn').textContent = '{ui["speak_btn"]}';
                    document.getElementById('mic-btn').classList.remove('listening');
                    const msgs = {{
                        'network': '❌ Network error — use Chrome!',
                        'not-allowed': '❌ Allow mic in browser settings!',
                        'no-speech': '❌ No speech detected. Try again!',
                    }};
                    document.getElementById('status').textContent = msgs[e.error] || '❌ ' + e.error;
                }};
            }}
        </script>
    """, height=150)

    # ── Catch voice from URL params ───────────────────────
    params = st.query_params
    if "voice" in params:
        voice_text = urllib.parse.unquote(params["voice"])
        st.query_params.clear()
        if voice_text and voice_text not in [
            m["content"] for m in st.session_state.messages
        ]:
            st.session_state.voice_query = voice_text
            st.rerun()

    st.divider()

    # ── Chat History ──────────────────────────────────────
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # ── Text Input ────────────────────────────────────────
    if prompt := st.chat_input(ui["chat_placeholder"]):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("🤖 ..."):
                reply = get_llm_response(
                    st.session_state.messages,
                    st.session_state.language
                )
                st.markdown(reply)
                st.session_state.messages.append({
                    "role": "assistant", "content": reply
                })
                speak(reply, st.session_state.language)
                st.session_state.notifications.append(
                    f"💬 — {datetime.now().strftime('%H:%M')}"
                )
                st.toast("✅", icon="🌾")

with col2:
    st.markdown(f"### {ui['stats']}")
    st.metric(ui["messages"], len(st.session_state.messages))
    st.metric(ui["alerts"], len(st.session_state.notifications))
    st.metric(ui["language"], st.session_state.language)
    st.caption(f"🕐 {datetime.now().strftime('%d %b %Y, %H:%M')}")
CROP_DATA = {

# 🍅 TOMATO
"Tomato": {
    "duration": "90–110 days",
    "cycles_per_year": 2,
    "seasons": ["Kharif", "Rabi"],

    "calendar": [
        {"month":"Jun","stage":{"English":"Nursery","Kannada":"ನರ್ಸರಿ","Hindi":"नर्सरी"},"temp":"25–32°C","rainfall":"High",
         "problem":{"English":"Damping off","Kannada":"ರೋಗ","Hindi":"रोग"},
         "action":{"English":"Raised beds","Kannada":"ಎತ್ತರದ ಬೆಡ್","Hindi":"ऊँचे बेड"},
         "tip":{"English":"Good drainage","Kannada":"ನೀರಿನ ಹರಿವು","Hindi":"जल निकासी"}},

        {"month":"Jul","stage":{"English":"Transplant","Kannada":"ನೆಡುವುದು","Hindi":"रोपाई"},"temp":"24–30°C","rainfall":"High",
         "problem":{"English":"Root rot","Kannada":"ಮೂಲ ಕುಲುಮೆ","Hindi":"जड़ सड़न"},
         "action":{"English":"Avoid overwatering","Kannada":"ಹೆಚ್ಚು ನೀರು ಬೇಡ","Hindi":"पानी कम करें"},
         "tip":{"English":"Proper spacing","Kannada":"ಅಂತರ","Hindi":"दूरी रखें"}},

        {"month":"Aug","stage":{"English":"Growth","Kannada":"ಬೆಳವಣಿಗೆ","Hindi":"विकास"},"temp":"24–30°C","rainfall":"Medium",
         "problem":{"English":"Fungal disease","Kannada":"ಫಂಗಲ್","Hindi":"फंगल"},
         "action":{"English":"Spray fungicide","Kannada":"ಸ್ಪ್ರೇ","Hindi":"स्प्रे"},
         "tip":{"English":"Air circulation","Kannada":"ಹವಾ ಹರಿವು","Hindi":"हवा"}},

        {"month":"Sep","stage":{"English":"Flowering","Kannada":"ಹೂ ಬೀಳು","Hindi":"फूल"},"temp":"22–28°C","rainfall":"Medium",
         "problem":{"English":"Flower drop","Kannada":"ಹೂ ಬೀಳುವುದು","Hindi":"फूल गिरना"},
         "action":{"English":"Use NPK","Kannada":"ಎನ್‌ಪಿಕೆ","Hindi":"एनपीके"},
         "tip":{"English":"Regular watering","Kannada":"ನೀರಾವರಿ","Hindi":"सिंचाई"}},

        {"month":"Oct","stage":{"English":"Fruiting","Kannada":"ಹಣ್ಣು","Hindi":"फल"},"temp":"20–28°C","rainfall":"Low",
         "problem":{"English":"Fruit borer","Kannada":"ಹುಳು","Hindi":"कीट"},
         "action":{"English":"Pesticide spray","Kannada":"ಔಷಧಿ","Hindi":"कीटनाशक"},
         "tip":{"English":"Monitor plants","Kannada":"ಪರಿಶೀಲನೆ","Hindi":"जांच"}},

        {"month":"Nov","stage":{"English":"Harvest","Kannada":"ಕೊಯ್ಲು","Hindi":"कटाई"},"temp":"18–26°C","rainfall":"Low",
         "problem":{"English":"None","Kannada":"ಯಾವುದೂ ಇಲ್ಲ","Hindi":"कोई नहीं"},
         "action":{"English":"Harvest regularly","Kannada":"ಕೊಯ್ಯಿರಿ","Hindi":"कटाई करें"},
         "tip":{"English":"Frequent picking","Kannada":"ಮರುಮರು","Hindi":"बार-बार"}}
    ],

    "insights": {
        "water": "600–800 mm",
        "soil": "Loamy soil",
        "yield": "25–30 t/ha"
    }
},

# 🧅 ONION
"Onion": {
    "duration": "120–150 days",
    "cycles_per_year": 2,
    "seasons": ["Kharif", "Rabi"],

    "calendar": [
        {"month":"Jun","stage":{"English":"Transplant","Kannada":"ನೆಡುವುದು","Hindi":"रोपाई"},"temp":"25–32°C","rainfall":"High",
         "problem":{"English":"Rot","Kannada":"ಕುಲುಮೆ","Hindi":"सड़न"},
         "action":{"English":"Improve drainage","Kannada":"ನೀರಿನ ಹರಿವು","Hindi":"जल निकासी"},
         "tip":{"English":"Loose soil","Kannada":"ಸಡಿಲ ಮಣ್ಣು","Hindi":"ढीली मिट्टी"}},

        {"month":"Jul","stage":{"English":"Growth","Kannada":"ಬೆಳವಣಿಗೆ","Hindi":"विकास"},"temp":"24–30°C","rainfall":"High",
         "problem":{"English":"Purple blotch","Kannada":"ರೋಗ","Hindi":"रोग"},
         "action":{"English":"Fungicide","Kannada":"ಔಷಧಿ","Hindi":"स्प्रे"},
         "tip":{"English":"Balanced fertilizer","Kannada":"ಸಮತೋಲನ","Hindi":"संतुलन"}},

        {"month":"Aug","stage":{"English":"Bulbing","Kannada":"ಗುಡ್ಡ ರೂಪ","Hindi":"बल्ब बनना"},"temp":"24–30°C","rainfall":"Medium",
         "problem":{"English":"Blight","Kannada":"ಬ್ಲೈಟ್","Hindi":"ब्लाइट"},
         "action":{"English":"Reduce irrigation","Kannada":"ನೀರು ಕಡಿಮೆ","Hindi":"पानी कम"},
         "tip":{"English":"Check leaves","Kannada":"ಪರಿಶೀಲನೆ","Hindi":"जांच"}},

        {"month":"Sep","stage":{"English":"Maturity","Kannada":"ಪಕ್ವ","Hindi":"परिपक्व"},"temp":"22–28°C","rainfall":"Low",
         "problem":{"English":"None","Kannada":"ಯಾವುದೂ ಇಲ್ಲ","Hindi":"कोई नहीं"},
         "action":{"English":"Stop watering","Kannada":"ನೀರು ನಿಲ್ಲಿಸಿ","Hindi":"पानी रोकें"},
         "tip":{"English":"Dry soil","Kannada":"ಒಣ ಮಣ್ಣು","Hindi":"सूखी मिट्टी"}},

        {"month":"Oct","stage":{"English":"Harvest","Kannada":"ಕೊಯ್ಲು","Hindi":"कटाई"},"temp":"20–28°C","rainfall":"Low",
         "problem":{"English":"Storage rot","Kannada":"ಕುಲುಮೆ","Hindi":"सड़न"},
         "action":{"English":"Dry bulbs","Kannada":"ಒಣಗಿಸಿ","Hindi":"सुखाएं"},
         "tip":{"English":"Store properly","Kannada":"ಸಂಗ್ರಹ","Hindi":"भंडारण"}}
    ],

    "insights": {
        "water": "350–550 mm",
        "soil": "Sandy loam",
        "yield": "20–25 t/ha"
    }
},

# 🥔 POTATO
"Potato": {
    "duration": "90–120 days",
    "cycles_per_year": 2,
    "seasons": ["Rabi"],

    "calendar": [
        {"month":"Oct","stage":{"English":"Planting","Kannada":"ನೆಡುವುದು","Hindi":"रोपण"},"temp":"20–25°C","rainfall":"Low",
         "problem":{"English":"None","Kannada":"ಯಾವುದೂ ಇಲ್ಲ","Hindi":"कोई नहीं"},
         "action":{"English":"Use treated tubers","Kannada":"ಉತ್ತಮ ಬೀಜ","Hindi":"बीज उपयोग"},
         "tip":{"English":"Good spacing","Kannada":"ಅಂತರ","Hindi":"दूरी"}},

        {"month":"Nov","stage":{"English":"Growth","Kannada":"ಬೆಳವಣಿಗೆ","Hindi":"विकास"},"temp":"15–25°C","rainfall":"Low",
         "problem":{"English":"Blight","Kannada":"ಬ್ಲೈಟ್","Hindi":"ब्लाइट"},
         "action":{"English":"Fungicide spray","Kannada":"ಸ್ಪ್ರೇ","Hindi":"स्प्रे"},
         "tip":{"English":"Check leaves","Kannada":"ಪರಿಶೀಲನೆ","Hindi":"जांच"}},

        {"month":"Dec","stage":{"English":"Bulking","Kannada":"ಗುಡ್ಡ ಬೆಳವಣಿಗೆ","Hindi":"कंद वृद्धि"},"temp":"10–20°C","rainfall":"Low",
         "problem":{"English":"Late blight","Kannada":"ಬ್ಲೈಟ್","Hindi":"ब्लाइट"},
         "action":{"English":"Regular spray","Kannada":"ಸ್ಪ್ರೇ","Hindi":"स्प्रे"},
         "tip":{"English":"Proper irrigation","Kannada":"ನೀರಾವರಿ","Hindi":"सिंचाई"}},

        {"month":"Jan","stage":{"English":"Harvest","Kannada":"ಕೊಯ್ಲು","Hindi":"कटाई"},"temp":"10–20°C","rainfall":"Low",
         "problem":{"English":"None","Kannada":"ಯಾವುದೂ ಇಲ್ಲ","Hindi":"कोई नहीं"},
         "action":{"English":"Harvest carefully","Kannada":"ಜಾಗ್ರತೆ","Hindi":"सावधानी"},
         "tip":{"English":"Store dry","Kannada":"ಒಣಗಿಸಿ","Hindi":"सूखा रखें"}}
    ],

    "insights": {
        "water": "500–700 mm",
        "soil": "Sandy loam",
        "yield": "20–30 t/ha"
    }
},

# 🍆 BRINJAL
"Brinjal": {
    "duration": "150–180 days",
    "cycles_per_year": 2,
    "seasons": ["Year-round"],

    "calendar": [
        {"month":"Jun","stage":{"English":"Transplant","Kannada":"ನೆಡುವುದು","Hindi":"रोपाई"},"temp":"25–32°C","rainfall":"High",
         "problem":{"English":"Wilt","Kannada":"ಒಣಗುವುದು","Hindi":"मुरझाना"},
         "action":{"English":"Soil treatment","Kannada":"ಮಣ್ಣು ಚಿಕಿತ್ಸೆ","Hindi":"उपचार"},
         "tip":{"English":"Mulching","Kannada":"ಮಲ್ಚಿಂಗ್","Hindi":"मल्चिंग"}},

        {"month":"Jul","stage":{"English":"Growth","Kannada":"ಬೆಳವಣಿಗೆ","Hindi":"विकास"},"temp":"24–30°C","rainfall":"High",
         "problem":{"English":"Borer","Kannada":"ಹುಳು","Hindi":"कीट"},
         "action":{"English":"Pesticide","Kannada":"ಔಷಧಿ","Hindi":"कीटनाशक"},
         "tip":{"English":"Remove infected","Kannada":"ತೆಗೆದುಹಾಕಿ","Hindi":"हटाएं"}},

        {"month":"Aug","stage":{"English":"Flowering","Kannada":"ಹೂ","Hindi":"फूल"},"temp":"24–30°C","rainfall":"High",
         "problem":{"English":"Blight","Kannada":"ಬ್ಲೈಟ್","Hindi":"ब्लाइट"},
         "action":{"English":"Spray","Kannada":"ಸ್ಪ್ರೇ","Hindi":"स्प्रे"},
         "tip":{"English":"Nutrition","Kannada":"ಪೋಷಣೆ","Hindi":"पोषण"}},

        {"month":"Sep","stage":{"English":"Fruiting","Kannada":"ಹಣ್ಣು","Hindi":"फल"},"temp":"22–28°C","rainfall":"Medium",
         "problem":{"English":"None","Kannada":"ಯಾವುದೂ ಇಲ್ಲ","Hindi":"कोई नहीं"},
         "action":{"English":"Harvest regularly","Kannada":"ಕೊಯ್ಯಿರಿ","Hindi":"कटाई करें"},
         "tip":{"English":"Continuous picking","Kannada":"ಮರುಮರು","Hindi":"बार-बार"}}
    ],

    "insights": {
        "water": "600–1000 mm",
        "soil": "Fertile soil",
        "yield": "25–35 t/ha"
    }
},

# 🌶️ CHILLI
"Chilli": {
    "duration": "150–200 days",
    "cycles_per_year": 1,
    "seasons": ["Kharif", "Rabi"],

    "calendar": [
        {"month":"Jun","stage":{"English":"Transplant","Kannada":"ನೆಡುವುದು","Hindi":"रोपाई"},"temp":"25–32°C","rainfall":"High",
         "problem":{"English":"Rot","Kannada":"ಕುಲುಮೆ","Hindi":"सड़न"},
         "action":{"English":"Avoid waterlogging","Kannada":"ನೀರು ಬೇಡ","Hindi":"पानी न भरें"},
         "tip":{"English":"Good drainage","Kannada":"ನೀರಿನ ಹರಿವು","Hindi":"निकासी"}},

        {"month":"Jul","stage":{"English":"Growth","Kannada":"ಬೆಳವಣಿಗೆ","Hindi":"विकास"},"temp":"24–30°C","rainfall":"High",
         "problem":{"English":"Anthracnose","Kannada":"ರೋಗ","Hindi":"रोग"},
         "action":{"English":"Spray fungicide","Kannada":"ಸ್ಪ್ರೇ","Hindi":"स्प्रे"},
         "tip":{"English":"Monitor plants","Kannada":"ಪರಿಶೀಲನೆ","Hindi":"जांच"}},

        {"month":"Aug","stage":{"English":"Flowering","Kannada":"ಹೂ","Hindi":"फूल"},"temp":"24–30°C","rainfall":"High",
         "problem":{"English":"Fruit rot","Kannada":"ಕುಲುಮೆ","Hindi":"सड़न"},
         "action":{"English":"Pesticide","Kannada":"ಔಷಧಿ","Hindi":"कीटनाशक"},
         "tip":{"English":"Proper care","Kannada":"ಜಾಗ್ರತೆ","Hindi":"देखभाल"}},

        {"month":"Sep","stage":{"English":"Fruiting","Kannada":"ಹಣ್ಣು","Hindi":"फल"},"temp":"22–28°C","rainfall":"Medium",
         "problem":{"English":"Thrips","Kannada":"ಹುಳು","Hindi":"कीट"},
         "action":{"English":"Spray","Kannada":"ಸ್ಪ್ರೇ","Hindi":"स्प्रे"},
         "tip":{"English":"Regular check","Kannada":"ಪರಿಶೀಲನೆ","Hindi":"जांच"}},

        {"month":"Oct","stage":{"English":"Harvest","Kannada":"ಕೊಯ್ಲು","Hindi":"कटाई"},"temp":"20–28°C","rainfall":"Low",
         "problem":{"English":"None","Kannada":"ಯಾವುದೂ ಇಲ್ಲ","Hindi":"कोई नहीं"},
         "action":{"English":"Harvest mature fruits","Kannada":"ಕೊಯ್ಯಿರಿ","Hindi":"कटाई करें"},
         "tip":{"English":"Dry properly","Kannada":"ಒಣಗಿಸಿ","Hindi":"सुखाएं"}}
    ],

    "insights": {
        "water": "600–800 mm",
        "soil": "Well-drained",
        "yield": "2–3 t/ha dry"
    }
}

}

DEFAULT_CROPS = list(CROP_DATA.keys())
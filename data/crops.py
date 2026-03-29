CROP_DATA = {

# 🍅 TOMATO
"Tomato": {
    "duration": "90–110 days",
    "cycles_per_year": 2,
    "seasons": ["Kharif (Jun–Jul)", "Rabi (Oct–Nov)"],
    "stages": [
        {"stage": "Nursery", "days": "0–25", "details": "Seed germination & seedling growth"},
        {"stage": "Transplanting", "days": "25–30", "details": "Shift to main field"},
        {"stage": "Vegetative", "days": "30–50", "details": "Leaf and stem growth"},
        {"stage": "Flowering", "days": "50–70", "details": "Flower initiation"},
        {"stage": "Fruiting", "days": "70–90", "details": "Fruit formation"},
        {"stage": "Harvest", "days": "90–110", "details": "Harvest every 3–4 days"},
    ],
    "calendar": [
        {"month":"Jun","activity":"Nursery","temp":"25–32°C","rainfall":"High","tip":"Raised beds","alert":"Damping off"},
        {"month":"Jul","activity":"Transplant","temp":"24–30°C","rainfall":"High","tip":"Spacing 60x45 cm","alert":"Blight"},
        {"month":"Aug","activity":"Growth","temp":"24–30°C","rainfall":"High","tip":"Staking","alert":"Fungal risk"},
        {"month":"Sep","activity":"Flowering","temp":"22–28°C","rainfall":"Medium","tip":"NPK spray","alert":"Fruit borer"},
        {"month":"Oct","activity":"Fruiting","temp":"20–28°C","rainfall":"Low","tip":"Add potassium","alert":"None"},
        {"month":"Nov","activity":"Harvest","temp":"18–26°C","rainfall":"Low","tip":"Frequent picking","alert":"None"},
    ],
    "insights": {
        "water": "600–800 mm",
        "soil": "Loamy, pH 6–7",
        "yield": "25–30 t/ha"
    }
},

# 🧅 ONION
"Onion": {
    "duration": "120–150 days",
    "cycles_per_year": 2,
    "seasons": ["Kharif", "Rabi"],
    "stages": [
        {"stage":"Nursery","days":"0–45","details":"Seedling stage"},
        {"stage":"Transplant","days":"45–60","details":"Shift to field"},
        {"stage":"Vegetative","days":"60–90","details":"Leaf growth"},
        {"stage":"Bulbing","days":"90–120","details":"Bulb formation"},
        {"stage":"Maturity","days":"120–150","details":"Top falling & harvest"},
    ],
    "calendar": [
        {"month":"Jun","activity":"Transplant","temp":"25–32°C","rainfall":"High","tip":"Good drainage","alert":"Rot"},
        {"month":"Jul","activity":"Growth","temp":"24–30°C","rainfall":"High","tip":"Nitrogen dose","alert":"Purple blotch"},
        {"month":"Aug","activity":"Bulbing","temp":"24–30°C","rainfall":"Medium","tip":"Reduce irrigation","alert":"Blight"},
        {"month":"Sep","activity":"Maturity","temp":"22–28°C","rainfall":"Low","tip":"Stop watering","alert":"None"},
        {"month":"Oct","activity":"Harvest","temp":"20–28°C","rainfall":"Low","tip":"Dry bulbs","alert":"None"},
    ],
    "insights": {
        "water": "350–550 mm",
        "soil": "Well-drained sandy loam",
        "yield": "20–25 t/ha"
    }
},

# 🥔 POTATO
"Potato": {
    "duration": "90–120 days",
    "cycles_per_year": 2,
    "seasons": ["Rabi dominant"],
    "stages": [
        {"stage":"Planting","days":"0–10","details":"Seed tuber planting"},
        {"stage":"Vegetative","days":"10–40","details":"Leaf growth"},
        {"stage":"Tuber initiation","days":"40–60","details":"Tuber starts forming"},
        {"stage":"Bulking","days":"60–90","details":"Tuber enlargement"},
        {"stage":"Harvest","days":"90–120","details":"Harvest mature tubers"},
    ],
    "calendar": [
        {"month":"Oct","activity":"Planting","temp":"20–25°C","rainfall":"Low","tip":"Use treated tubers","alert":"None"},
        {"month":"Nov","activity":"Growth","temp":"15–25°C","rainfall":"Low","tip":"Apply NPK","alert":"Blight"},
        {"month":"Dec","activity":"Bulking","temp":"10–20°C","rainfall":"Low","tip":"Irrigate regularly","alert":"Late blight"},
        {"month":"Jan","activity":"Harvest","temp":"10–20°C","rainfall":"Low","tip":"Cure before storage","alert":"None"},
    ],
    "insights": {
        "water": "500–700 mm",
        "soil": "Loose sandy loam",
        "yield": "20–30 t/ha"
    }
},

# 🍆 BRINJAL
"Brinjal": {
    "duration": "150–180 days",
    "cycles_per_year": 2,
    "seasons": ["Year-round (South India)"],
    "stages": [
        {"stage":"Nursery","days":"0–30","details":"Seedling stage"},
        {"stage":"Transplant","days":"30–40","details":"Shift to field"},
        {"stage":"Vegetative","days":"40–80","details":"Plant growth"},
        {"stage":"Flowering","days":"80–100","details":"Flower formation"},
        {"stage":"Fruiting","days":"100–150","details":"Fruit development"},
        {"stage":"Harvest","days":"150+","details":"Continuous harvest"},
    ],
    "calendar": [
        {"month":"Jun","activity":"Transplant","temp":"25–32°C","rainfall":"High","tip":"Mulching","alert":"Wilt"},
        {"month":"Jul","activity":"Growth","temp":"24–30°C","rainfall":"High","tip":"Top dressing","alert":"Borer"},
        {"month":"Aug","activity":"Flowering","temp":"24–30°C","rainfall":"High","tip":"Micronutrients","alert":"Blight"},
        {"month":"Sep","activity":"Fruiting","temp":"22–28°C","rainfall":"Medium","tip":"Regular harvest","alert":"None"},
    ],
    "insights": {
        "water": "600–1000 mm",
        "soil": "Fertile loamy soil",
        "yield": "25–35 t/ha"
    }
},

# 🌶️ CHILLI
"Chilli": {
    "duration": "150–200 days",
    "cycles_per_year": 1,
    "seasons": ["Kharif", "Rabi"],
    "stages": [
        {"stage":"Nursery","days":"0–40","details":"Seedling stage"},
        {"stage":"Transplant","days":"40–50","details":"Shift to field"},
        {"stage":"Vegetative","days":"50–90","details":"Plant growth"},
        {"stage":"Flowering","days":"90–110","details":"Flowering begins"},
        {"stage":"Fruiting","days":"110–150","details":"Fruit growth"},
        {"stage":"Harvest","days":"150+","details":"Green/red harvest"},
    ],
    "calendar": [
        {"month":"Jun","activity":"Transplant","temp":"25–32°C","rainfall":"High","tip":"Avoid waterlogging","alert":"Rot"},
        {"month":"Jul","activity":"Growth","temp":"24–30°C","rainfall":"High","tip":"Nitrogen dose","alert":"Anthracnose"},
        {"month":"Aug","activity":"Flowering","temp":"24–30°C","rainfall":"High","tip":"Foliar spray","alert":"Fruit rot"},
        {"month":"Sep","activity":"Fruiting","temp":"22–28°C","rainfall":"Medium","tip":"Harvest regularly","alert":"Thrips"},
        {"month":"Oct","activity":"Harvest","temp":"20–28°C","rainfall":"Low","tip":"Pick mature fruits","alert":"None"},
    ],
    "insights": {
        "water": "600–800 mm",
        "soil": "Well-drained soil",
        "yield": "2–3 t/ha dry"
    }
}

}

DEFAULT_CROPS = list(CROP_DATA.keys())
import random
from datetime import datetime, timedelta

def get_market_prices(commodity="Tomato", state="Karnataka"):

    base_prices = {
        "Tomato": 1800,
        "Onion": 1500,
        "Potato": 1200,
        "Rice": 2500,
        "Wheat": 2200
    }

    base = base_prices.get(commodity, 1500)

    data = []
    today = datetime.today()

    # Generate last 15 days data
    for i in range(15):
        price = base + random.randint(-200, 200)

        data.append({
            "market": f"{state} Mandi",
            "modal_price": price,
            "min_price": price - random.randint(100, 200),
            "max_price": price + random.randint(100, 200),
            "date": (today - timedelta(days=15-i)).strftime("%Y-%m-%d")
        })

    return {
        "source": "agri_simulated",
        "data": data
    }
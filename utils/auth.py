import json
import os

FILE = "users.json"

def load_users():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(FILE, "w") as f:
        json.dump(users, f)

def signup(username, password):
    users = load_users()

    # 🧼 CLEAN INPUT (VERY IMPORTANT)
    username = username.strip().lower()
    password = password.strip()

    if username in users:
        return False

    users[username] = {
        "password": password,
        "data": []
    }

    save_users(users)
    return True

def login(username, password):
    import json

    # 🧼 Clean input (IMPORTANT for mobile)
    username = username.strip().lower()
    password = password.strip()

    try:
        with open("users.json", "r") as f:
            users = json.load(f)
    except:
        return False

    # 🔍 Check credentials
    if username in users:
        return users[username]["password"] == password

    return False

def save_user_data(username, entry):
    users = load_users()
    users[username]["data"].append(entry)
    save_users(users)

def get_user_data(username):
    users = load_users()
    return users.get(username, {}).get("data", [])
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
    if username in users:
        return False
    users[username] = {
        "password": password,
        "data": []
    }
    save_users(users)
    return True

def login(username, password):
    users = load_users()
    if username in users and users[username]["password"] == password:
        return True
    return False

def save_user_data(username, entry):
    users = load_users()
    users[username]["data"].append(entry)
    save_users(users)

def get_user_data(username):
    users = load_users()
    return users.get(username, {}).get("data", [])
from cryptography.fernet import Fernet
import string
import shutil

def load_key():
    with open("key.key", "rb") as file:
        return file.read()

key = load_key()
fer = Fernet(key)

def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, passw = data.split("|")
                print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())
    except Exception as e:
        print("Error viewing passwords:", e)

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")
    
    # Check password strength
    strength = check_password_strength(pwd)
    print("Password strength:", strength)

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

def check_password_strength(password):
    length_requirements = len(password) >= 8
    uppercase = any(c.isupper() for c in password)
    lowercase = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    special_char = any(c in string.punctuation for c in password)

    strength_score = sum([length_requirements, uppercase, lowercase, digit, special_char])
    return "Weak" if strength_score < 3 else "Strong"


while True:
    mode = input("Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")

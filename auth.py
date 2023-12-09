import json
from termcolor import colored


def validate_name(name):
    return name.isalpha()

def validate_email(email):
    import re
    return re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9]+$", email) is not None

def validate_phone(phone):
    return phone.startswith(("011", "010", "012")) and len(phone) == 11 and phone.isdigit()

def register_user():
    user_data = {}
    while True:
        try:
            first_name = input("Enter your first name: ")
            while not validate_name(first_name):
                first_name = input(colored("Invalid first name format. Enter your first name again: ","red"))
            user_data['first_name'] = first_name

            last_name = input("Enter your last name: ")
            while not validate_name(last_name):
                last_name = input(colored("Invalid last name format. Enter your last name again: ","red"))
            user_data['last_name'] = last_name
            email = input("Enter your email: ")
            while not validate_email(email):
                email = input(colored("Invalid email format. Enter your email again: ","red"))
            user_data['email'] = email
            password = input("Enter your password: ")
            confirm_password = input("Confirm your password: ")
            while password != confirm_password:
                print(colored("Passwords do not match. Please try again.","red"))
                password = input("Enter your password: ")
                confirm_password = input("Confirm your password: ")
            user_data['password'] = password
            phone = input("Enter your mobile phone number: ")
            while not validate_phone(phone):
                phone = input(colored("Invalid phone number format. Must start with 011, 010, or 012. Enter your phone number again: ","red"))
            user_data['phone'] = phone
            user_data['user_id'] = len(get_all_users()) + 1
            save_user(user_data)
            print("\n")
            print(colored("Registration successful!","blue"))
            break
        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")

def save_user(user_data):
    try:
        with open("users.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    data.append(user_data)
    with open("users.json", "w") as file:
        json.dump(data, file, indent=4)

def get_all_users():
    try:
        with open("users.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def login_user():
    email = input("Enter your email:")
    while not validate_email(email):
            email = input(colored("Invalid email format. Enter your email again: ","red"))
    password = input("Enter your password: ")
    try:
        with open("users.json", "r") as file:
            data = json.load(file)
            for user in data:
                if user['email'] == email and user['password'] == password:
                    print(colored("Login successful!","blue"))
                    return user['user_id']
        print(colored("Invalid email or password. Please try again.","red"))
    except FileNotFoundError:
        print(colored("No user registered yet. Please register first.","red"))
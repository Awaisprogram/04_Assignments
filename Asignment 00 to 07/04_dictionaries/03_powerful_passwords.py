from hashlib import sha256

def login(email, stored_login, password_to_check):
    if email in stored_login and stored_login[email] == hash_password(password_to_check):
        return True
    return False

def hash_password(password):
    return sha256(password.encode()).hexdigest()

def main():
    stored_login = {
        "awais@gmail.com": hash_password("awais123"),
        "user@example.com": hash_password("password123"),
        "admin@site.com": hash_password("admin456")
    }

    # Prompt user for login credentials
    email = input("Enter Email: ")
    password = input("Enter Password: ")

    if login(email, stored_login, password):
        print("Login successfull")

    else:
        print("Invalid email or password!")    

# Ensure script runs only when executed directly
if __name__ == "__main__":
    main()

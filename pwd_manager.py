from cryptography.fernet import Fernet

# Uncomment the following function if you need to generate a new key
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

def load_key():
    with open("key.key", "rb") as file:
        key = file.read()
    return key

def main():
    while True:
        print("1. View existing password ")
        print("2. Add new password")
        print("3. Exit")
        option = int(input("Enter a number (1-3): "))
        if option == 1:
            view()
        elif option == 2:
            add()
        elif option == 3:
            break
        else:
            print("Invalid option. Please try again.")

def view():
    with open("password.txt", "r") as passwd_file:
        for line in passwd_file.readlines():
            try:
                username, encrypted_password = line.rstrip().split("|")
                print("Username:", username, "Password:", f.decrypt(encrypted_password.encode()).decode())
            except ValueError:
                print(f"Skipping malformed line: {line.strip()}")

def add():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if "|" in username or "|" in password:
        print("Error: Username and password cannot contain the '|' character.")
        return
    with open("password.txt", "a") as passwd_file:
        encrypted_password = f.encrypt(password.encode()).decode()
        passwd_file.write(f"{username}|{encrypted_password}\n")

if __name__ == "__main__":
    master_key = input("What is the master key? ")
    key = load_key()
    f = Fernet(key)
    if master_key == "Prabin":
        print("---------------------LOGGED IN SUCCESSFULLY-----------------------")
        main()
    else:
        print("Incorrect master key!!!")

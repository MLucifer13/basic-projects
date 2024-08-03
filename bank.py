# balance = 0
# transaction_history = []

# users = {
#     "admin": "admin123",
#     "user": "user123",
#     "guest": "guest123",
#     "manager": "manager123",
#     "employee": "employee123"
# }


# #checks if the input is a valid user and authenticates the user with password
# def authenticate_user(username, password):
#     if username in users and users[username] == password:
#         print("Login Successful")
#         return True
#     else:
#         print("Incorrect username or password")
#         return False
    
# #main function for the banking program and calls all the other functions based on the user input 
# def main():
#     print("*********************************")
#     print("       BANKING PROGRAM           ")
#     print("*********************************")
#     print("1. SHOW BALANCE")
#     print("2. DEPOSIT AMOUNT")
#     print("3. WITHDRAW AMOUNT")
#     print("4. VIEW TRANSACTION HISTORY")
#     print("5. EXIT")
#     print("*********************************")
#     #loops until the user enters a valid choice or if the user chooses to exit
#     while True:
#         try:
#             choice = int(input("Enter your choice (1-5): "))
#             if choice == 1:
#                 show_balance()
#             elif choice == 2:
#                 deposit_amount()
#             elif choice == 3:
#                 withdraw_amount()
#             elif choice == 4:
#                 show_transaction_history()
#             elif choice == 5:
#                 print("Thank you for banking with us.")
#                 break
#             else:
#                 print("Invalid choice. Please enter a number between 1 and 5.")
#         #catches value error if user inputs a string instead of a number
#         except ValueError:
#             print("Invalid input. Please enter a number between 1 and 5.")
# #function to show the balance


# def show_balance():
#     print(f"Your balance is: ${balance:.2f}")
# #function to deposit the amount which uses global variables and appends the transaction history to the list


# def deposit_amount():
#     global balance
#     try:
#         deposit = float(input("Enter the amount you want to deposit: $"))
#         if deposit <= 0:
#             print("Invalid amount. Please enter a positive number.")
#         else:
#             balance += deposit
#             transaction_history.append({"type": "deposit", "amount": deposit, "balance": balance})
#             print(f"Deposit successful. Your new balance is: ${balance:.2f}")
#             notification()
#     except ValueError:
#         print("Invalid input. Please enter a numeric value.")


# #function to withdraw amount and appends it to transaction history and also if the transaction amount is too much, it sends a message
# def withdraw_amount():
#     global balance
#     try:
#         withdraw = float(input("Enter the amount you want to withdraw: $"))
#         if withdraw <= 0:
#             print("Invalid amount. Please enter a positive number.")
#         elif withdraw <= balance:
#             balance -= withdraw
#             transaction_history.append({"type": "withdrawal", "amount": withdraw, "balance": balance})
#             print(f"Withdrawal successful. Your new balance is: ${balance:.2f}")
#             notification()
#         else:
#             print("Insufficient balance.")
#     except ValueError:
#         print("Invalid input. Please enter a numeric value.")


# #function which shows the transaction history
# def show_transaction_history():
#     print("*********************************")
#     print("*       TRANSACTION HISTORY     *")
#     print("*********************************")
#     for transaction in transaction_history:
#         print(f"{transaction['type'].capitalize()}: ${transaction['amount']} | Balance: ${transaction['balance']:.2f}")
#     print("*********************************")


# #notification function which notifies the user if large sum of money is withdrawn or there is low balance
# def notification():
#     global balance
#     if balance < 1:
#         print(f"Your current balance is ${balance}. Please deposit more funds.")
#     last_transaction = transaction_history[-1]
#     if last_transaction["type"] == "withdrawal" and last_transaction["amount"] > 10000:
#         print(f"A withdrawal of ${last_transaction['amount']} has been requested. If this wasn't you, please contact the bank immediately to resolve the issue.")


# #ensures that the main function runs only when authenticate user function completes
# if __name__ == "__main__":
#     id = input("Enter your username: ")
#     pswd = input("Enter your password: ")
#     if authenticate_user(id, pswd):
#         main()

class Account:
    def __init__(self):
        self._balance = 0
    @property
    def balance(self):
        return self._balance
    
    def deposit(self, n):
        self._balance += n
    def withdrawn(self, n):
        self._balance -= n
    
def main():
    account = Account()
    print(account.balance)
    account.deposit(100)
    account.withdrawn(50)
    print(account.balance)

if __name__ == "__main__":
    main()



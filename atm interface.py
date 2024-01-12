class Account:
    def __init__(self, account_no, pin, balance=0):
        self.account_no = account_no
        self.pin = pin
        self.balance = balance
        self.transaction = []
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction.append(f'Deposit: +Rs{amount}')
            return True
        else:
            return False
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction.append(f'Withdrawal: -Rs{amount}')
            return True
        else:
            return False
    def get_balance(self):
        return self.balance
    def get_transaction_history(self):
        return self.transaction
class ATM:
    def __init__(self):
        self.accounts = {}
    def create_account(self, account_no, pin):
        if account_no not in self.accounts:
            self.accounts[account_no] = Account(account_no, pin)
            return True
        else:
            return False
    def authenticate(self, account_no, pin):
        if account_no in self.accounts and self.accounts[account_no].pin == pin:
            return self.accounts[account_no]
        else:
            return None
def display_menu():
    print("1. Create Account")
    print("2. Log In")
    print("3. Quit")
def display_submenu():
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Log Out")
def main():
    atm = ATM()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            account_no = input("Enter your ACCOUNT NO: ")
            pin = input("Enter your PIN: ")
            if atm.create_account(account_no, pin):
                print("Account created successfully!")
                print("-------------------------------------------------------")
            else:
                print("User ID already exists. Please choose another.")
                print("-------------------------------------------------------")
        elif choice == "2":
            account_no = input("Enter your ACCOUNT NO: ")
            pin = input("Enter your PIN: ")
            account = atm.authenticate(account_no, pin)
            if account:
                print("Authentication successful!")
                print("-------------------------------------------------------")
                while True:
                    display_submenu()
                    sub_choice = input("Enter your choice: ")
                    if sub_choice == "1":
                        amount = float(input("Enter the deposit amount: "))
                        if account.deposit(amount):
                            print(f"Deposited Rs{amount} successfully.")
                            print("-------------------------------------------------------")
                        else:
                            print("Invalid deposit amount.")
                            print("-------------------------------------------------------")
                    elif sub_choice == "2":
                        amount = float(input("Enter the withdrawal amount: "))
                        if account.withdraw(amount):
                            print(f"Withdrew Rs{amount} successfully.")
                            print("-------------------------------------------------------")
                        else:
                            print("Insufficient funds or invalid withdrawal amount.")
                            print("-------------------------------------------------------")
                    elif sub_choice == "3":
                        print(f"Current Balance: Rs{account.get_balance()}")
                        print("-------------------------------------------------------")
                    elif sub_choice == "4":
                        history = account.get_transaction_history()
                        print("Transaction History:")
                        for transaction in history:
                            print(transaction)
                            print("-------------------------------------------------------")
                    elif sub_choice == "5":
                        break
                    else:
                        print("Invalid choice.")
                        print("-------------------------------------------------------")
            else:
                print("Authentication failed. Please check your user ID and PIN.")
                print("-------------------------------------------------------")
        elif choice == "3":
            print("Exiting the ATM. Thanks for using, have a nice day.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__=="__main__":
    main()
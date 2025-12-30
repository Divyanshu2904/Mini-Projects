class ATM:
    def __init__(self, pin, balance=0):
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def verify_pin(self):
        entered_pin = input("Enter your PIN: ")
        return entered_pin == self.pin

    def balance_inquiry(self):
        print(f"Your current balance is: ${self.balance:.2f}")
        self.transaction_history.append(f"Check Balance: ${self.balance:.2f}")

    def deposit(self):
        amount = float(input("Enter the amount to deposit: $"))
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited successfully.")
            self.transaction_history.append(f"Deposited: ${amount:.2f}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: $"))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn successfully.")
            self.transaction_history.append(f"Withdrawn: ${amount:.2f}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def change_pin(self):
        old_pin = input("Enter your old PIN: ")
        if old_pin == self.pin:
            new_pin = input("Enter your new PIN: ")
            if len(new_pin) == 4 and new_pin.isdigit():
                self.pin = new_pin
                print("PIN changed successfully.")
                self.transaction_history.append("PIN changed.")
            else:
                print("New PIN must be 4 digits.")
        else:
            print("Incorrect old PIN.")

    def transaction_history_display(self):
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(f" - {transaction}")
        else:
            print("No transactions yet.")

def atm_menu():
    atm = ATM(pin="9110", balance=1000)
    print("Welcome to the ATM Machine!")

    if not atm.verify_pin():
        print("Incorrect PIN. Exiting.")
        return

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Change PIN")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            atm.balance_inquiry()
        elif choice == "2":
            atm.deposit()
        elif choice == "3":
            atm.withdraw()
        elif choice == "4":
            atm.change_pin()
        elif choice == "5":
            atm.transaction_history_display()
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

atm_menu()

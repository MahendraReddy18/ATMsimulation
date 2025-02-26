# Define the ATM class to handle all ATM operations
class ATM:
    def __init__(self):
        # Initialize the account balance with a default value of $5000
        self.balance =5000
        # Initialize the default PIN as "1234"
        self.pin = "1234"
        # Initialize an empty list to store transaction history
        self.transaction_history = []

    # Method to check the current account balance
    def check_balance(self):
        return self.balance

    # Method to withdraw cash from the account
    def withdraw_cash(self, amount):
        # Check if the withdrawal amount exceeds the available balance
        if amount > self.balance:
            return "Insufficient funds"
        # Deduct the withdrawal amount from the balance
        self.balance -= amount
        # Add the withdrawal transaction to the transaction history
        self.transaction_history.append(f"Withdrawal: -${amount}")
        # Return a success message with the updated balance
        return f"Withdrawal successful. Remaining balance: ${self.balance}"

    # Method to deposit cash into the account
    def deposit_cash(self, amount):
        # Add the deposit amount to the balance
        self.balance += amount
        # Add the deposit transaction to the transaction history
        self.transaction_history.append(f"Deposit: +${amount}")
        # Return a success message with the updated balance
        return f"Deposit successful. New balance: ${self.balance}"

    # Method to change the PIN
    def change_pin(self, old_pin, new_pin):
        # Check if the old PIN matches the current PIN
        if old_pin == self.pin:
            # Update the PIN to the new PIN
            self.pin = new_pin
            return "PIN changed successfully"
        else:
            # Return an error message if the old PIN is incorrect
            return "Incorrect old PIN"

    # Method to retrieve the transaction history
    def get_transaction_history(self):
        return self.transaction_history


# Main function to run the ATM system
def main():
    # Create an instance of the ATM class
    atm = ATM()

    # Main loop to display the menu and handle user input
    while True:
        # Display the ATM menu options
        print("\nWelcome to the ATM")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        # Get the user's choice
        choice = input("Enter your choice: ")

        # Handle the user's choice
        if choice == "1":
            # Check and display the account balance
            print(f"Your balance is: ${atm.check_balance()}")

        elif choice == "2":
            # Withdraw cash
            amount = float(input("Enter amount to withdraw: "))
            print(atm.withdraw_cash(amount))

        elif choice == "3":
            # Deposit cash
            amount = float(input("Enter amount to deposit: "))
            print(atm.deposit_cash(amount))

        elif choice == "4":
            # Change the PIN
            old_pin = input("Enter old PIN: ")
            new_pin = input("Enter new PIN: ")
            print(atm.change_pin(old_pin, new_pin))

        elif choice == "5":
            # Display the transaction history
            history = atm.get_transaction_history()
            print("Transaction History:")
            for transaction in history:
                print(transaction)

        elif choice == "6":
            # Exit the ATM system
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            # Handle invalid choices
            print("Invalid choice. Please try again.")


# Run the main function when the script is executed
if __name__ == "__main__":
    main()
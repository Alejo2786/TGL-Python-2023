# Write a Python class called BankAccount with methods for depositing, withdrawing,and checking the account balance.

class BankAccount:
    def __init__(self, balance=0.0):    # Initializes a BankAccount object with an optional initial balance.
        self.balance = balance

    def deposit(self, amount):         # Deposits the specified amount into the account and updates the account balance.

        if amount > 0:
            self.balance += amount
            print(f"${amount} dollars has been deposited into the account and the account balance is ${self.balance} dollars.")

        else:
            print("The deposit is not valid")


    def withdraw(self, amount):       # Withdraws the specified amount from the account if sufficient funds are available.
                                       # Updates the account balance accordingly.
        if amount > 0:

            if self.balance >= amount:
                self.balance -= amount
                print(f"${amount} dollars has been withdrawn from the account and the account balance is ${self.balance} dollars.")

            else:
                print("The account does not have sufficient funds for the withdrawal.")

        else:
            print("The withdrawal is not valid")


    def check_balance(self):                                          # Prints the current account balance.
        print(f"The account balance is ${self.balance} dollars")


def main():
     account = BankAccount(15000)                                     # Create an instance of BankAccount with an initial balance of $15,000
     
     while True:

        print("\nWhat would you like to do?")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        option = input("Enter your choice (1-4): ")

        if option == "1":
            amount = float(input("Enter the amount to deposit in the account: "))    # Call the deposit method of the BankAccount instance
            account.deposit(amount)

        elif option == "2":
            amount = float(input("Enter the amount to withdraw from the account: "))   # Call the withdraw method of the BankAccount instance
            account.withdraw(amount)

        elif option == "3":                                                    # Call the check_balance method of the BankAccount instance
            account.check_balance()

        elif option == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == '__main__':
    main()


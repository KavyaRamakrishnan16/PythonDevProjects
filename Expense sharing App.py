class ExpenseSharingApp:
    def __init__(self):
        self.users = {}
        self.expenses = []

    def add_user(self, username):
        self.users.setdefault(username, {'name': username, 'expenses': 0.0})
        print(f"User '{username}' added successfully.")

    def add_expense(self, payer, amount, description, friends):
        if payer in self.users:
            self.users[payer]['expenses'] += amount
            per_user_share = amount / (len(friends) + 1)

            for friend in friends:
                self.users.setdefault(friend, {'name': friend, 'expenses': 0.0})
                self.users[friend]['expenses'] -= per_user_share

            self.expenses.append({'payer': payer, 'amount': amount, 'description': description, 'friends': friends})
            print("Expense added successfully.")
        else:
            print(f"User '{payer}' does not exist.")

    def display_summary(self):
        print("Users:")
        for user in self.users.values():
            print(f"{user['name']}: ₹{user['expenses']:.2f}")

        print("\nExpenses:")
        for expense in self.expenses:
            print(f"{expense['payer']} paid ₹{expense['amount']:.2f} for {expense['description']}")
            for friend in expense['friends']:
                print(f"  - {friend} owes {expense['payer']} ₹{expense['amount'] / len(expense['friends']):.2f}")

if __name__ == '__main__':
    app = ExpenseSharingApp()

    while True:
        print("\nExpense Sharing App\n1. Add User\n2. Add Expense\n3. Display Summary\n4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1': app.add_user(input("Enter username: "))
        elif choice == '2':
            try:
                user_input = input("Enter payer, amount, description, friends: ").split(', ')
                if len(user_input) >= 4:
                    payer, amount, description, *friends = user_input
                    app.add_expense(payer, float(amount), description, friends)
                else:
                    print("Invalid input. Please provide all required values.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
            except Exception as e:
                print(f"An error occurred: {e}")
        elif choice == '3': app.display_summary()
        elif choice == '4': print("Exiting. Goodbye!"); break
        else: print("Invalid choice. Please try again.")

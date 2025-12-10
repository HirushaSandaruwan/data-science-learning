import numpy as np
from datetime import datetime
import json

categories = ["Food", "Entertainment", "Utilities", "Transport", "Others"]

#define the structure of one expense entry
expense_dtype = np.dtype([
    ("date","U19"),
    ("category", "U20"),
    ("description", "U50"),
    ("amount","f4")
])


# Function to save NumPy expenses to a JSON file
def save_expenses(expenses_np, income, filename="expenses.json"):
    # Convert NumPy array to list of dictionaries
    expenses_list = expenses_np.tolist()  # each row becomes a list
    expenses_list_dict = [
        {"date": row[0], "category": row[1], "description": row[2], "amount": float(row[3])}
        for row in expenses_list
    ]
    # Save as JSON
    with open(filename, "w") as f:
        json.dump({"expenses": expenses_list_dict, "income": income}, f, indent=4)
    print("Expenses saved successfully!")


# Function to load expenses from JSON back to NumPy array
def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            income = data.get("income", 0)
            expenses_list_dict = data.get("expenses", [])
            # Convert list of dicts back to NumPy array
            expenses_np = np.array([
                (e["date"], e["category"], e["description"], e["amount"])
                for e in expenses_list_dict
            ], dtype=expense_dtype)
            return expenses_np, income
    except FileNotFoundError:
        # If no file exists, start fresh
        return np.array([], dtype=expense_dtype), 0


#create a numpy array using the above structure
expenses_np = np.array([], dtype=expense_dtype)


# Function to get a positive number from the user
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a number.")


#predefined categories make analysis easier
def get_category():
    print("Choose a category")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    while True:
        try:
            choice = int(input("Enter your Choice: "))
            if 1<= choice <= len(categories):
                return categories[choice - 1]
            else:
                print("Please enter a valid choice")

        except ValueError:
            print("Invalid input!. Please enter a valid choice")


#choosing how user wants to view the data list
def get_valid_sort_choice():

    while True:
        print("Sort by:")
        print("1. Date")
        print("2. Category")
        try:
            sort_choice = int(input("Enter your choice: "))
            if sort_choice in [1, 2]:
                return sort_choice
            else:
                print("Invalid choice. Please choose either 1 or 2.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# Function to get total income from user
def get_income():
    return get_positive_float("Enter your total income: ")

def main_menu():
    print("\nExpense Tracker (NumPy Version)")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses & Remaining Balance")
    print("4. Update Income")
    print("5. Exit")


# Function to add a new expense to the NumPy array
def add_expense_numpy(expenses_np, income):
    amount = get_positive_float("Enter the amount: ")
    category = get_category()
    description = input("Enter description: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create one new row
    new_row = np.array([(date, category, description, amount)], dtype=expenses_np.dtype)

    # Add the new row to the existing array
    expenses_np = np.concatenate((expenses_np, new_row))

    print("Expense added successfully!")
    save_expenses(expenses_np, income)
    return expenses_np


# Function to view expenses
def view_expenses_numpy(expenses_np):
    if len(expenses_np) == 0:
        print("No expenses recorded.")
        return

    sort_choice = get_valid_sort_choice()

    # Sort the NumPy array
    if sort_choice == 1:  # sort by date descending
        sorted_expenses = np.sort(expenses_np, order = 'date')[::-1]
    else:  # sort by category ascending
        sorted_expenses = np.sort(expenses_np, order = 'category')

    # Display expenses
    print("\nDate | Category | Description | Amount")
    print("-" * 50)
    for expense in sorted_expenses:
        print(f"{expense['date']} | {expense['category']} | {expense['description']} | {expense['amount']:.2f}")
    print("-" * 50)


# Function to calculate total expenses and remaining balance
def total_expenses_numpy(expenses_np, income):
    if len(expenses_np) == 0:
        print("No expenses recorded.")
        return

    # Calculate total expense using NumPy sum
    total_expense = np.sum(expenses_np['amount'])

    remaining_balance = income - total_expense

    print(f"\nTotal expenses: {total_expense:.2f}")
    print(f"Remaining balance: {remaining_balance:.2f}\n")


# Main program loop
def main():
    global expenses_np
    expenses_np, income = load_expenses()  # load saved data

    if income == 0:
        income = get_income()  # ask for income if not saved

    while True:
        main_menu()
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                expenses_np = add_expense_numpy(expenses_np,income)
            elif choice == 2:
                view_expenses_numpy(expenses_np)
            elif choice == 3:
                total_expenses_numpy(expenses_np, income)
            elif choice == 4:
                income = get_income()
                print("Income updated successfully.")
            elif choice == 5:
                save_expenses(expenses_np, income)
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice! Enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Enter a number.")

if __name__ == "__main__":
    main()




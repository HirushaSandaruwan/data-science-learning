import json
from datetime import datetime

categories = ["Food", "Entertainment", "Utilities", "Transport", "Others"]

def save_expenses(expenses,income, filename="expenses.json"):
    """
        Saves the expenses and income to a JSON file.
        Args:
            expenses (list): A list of expense dictionaries.
            income (float): The total income.
            filename (str): The name of the file to save to (default is "expenses.json").
    """
    with open(filename, "w") as f:
        json.dump({"expenses": expenses, "income": income}, f, indent=4)


#load the data from json file to the code
def load_expenses(filename="expenses.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return data.get("expenses", []), data.get("income", 0)
    except FileNotFoundError:
        # Create a new file if it doesn't exist yet
        save_expenses([], 0)  # Save empty data to the file on the first run
        return [], 0


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


#make sure values are numerical and non-negative
def get_positive_float(prompt):
    while True:
        try:
            value= float(input(prompt))
            if value < 0:
                print("Please enter a positive number")
            else:
                return value
        except ValueError:
            print("Invalid input!. Please enter a valid number")


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


def main_menu():
    print("Expense Tracker")
    print("1.Add Expenses")
    print("2.View Expenses")
    print("3.Total Expense")
    print("4.Update Income")
    print("5.Exit")


def add_expenses(expenses, income):

    amount = get_positive_float("Enter the amount: ")
    category = get_category()
    description = input("Enter description of your expense: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #show current time in standard form

    expense = {
        "amount" : amount,
        "category" : category,
        "description" : description,
        "date" : date
    }

    expenses.append(expense)
    save_expenses(expenses, income) #save expense after each data entering
    print("Expense added and saved successfully.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return

    sort_choice = get_valid_sort_choice()

    if sort_choice == 1:
        sorted_expenses = sorted(expenses, key=lambda x: x["date"], reverse=True) #order by date
    elif sort_choice == 2:
        sorted_expenses = sorted(expenses, key=lambda x: x["category"]) #order by category

    for expense in sorted_expenses:
        print(f"{expense['date']} | {expense['category']} | {expense['description']} | {expense['amount']:.2f}")


def total_expenses(expenses, income):
    if not expenses:
        print("No expenses recorded")
        return
    else:
        total_expense = sum(expense['amount'] for expense in expenses)
        remaining_balance = income - total_expense
        print(f"Total expenses: {total_expense:.2f}  Remaining balance: {remaining_balance:.2f}")


def main():
    expenses,income = load_expenses()

    if income <= 0:
        income = get_positive_float("Enter your Total Income: ")

    while True:
        main_menu()
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 5:
                if choice == 1:
                    add_expenses(expenses, income)
                elif choice == 2:
                    view_expenses(expenses)
                elif choice == 3:
                    total_expenses(expenses, income)
                elif choice == 4:
                    income = get_positive_float("Enter your new Total Income: ")
                    print("Income updated successfully.")
                elif choice == 5:
                    save_expenses(expenses, income)  # Save before exiting
                    print("Exiting")
                    break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()










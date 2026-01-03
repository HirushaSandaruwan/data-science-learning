
import pandas as pd
from datetime import datetime
import json

#------------------------------
#Expense Tracker (Pandas Version)
#------------------------------

#creating predefined category list to make analysis easier
categories = ["Food", "Entertainment", "Utilities", "Transport", "Others"]

#create a pandas dataFrame
columns = ["date", "category", "description", "amount"] #columns for the dataFrame
expenses_df = pd.DataFrame(columns= columns)

#-------------------------
#Persistence Functions
#-------------------------

def save_expenses(expenses_df,income,filename= "expenses.json"):
    # Convert date column to string for JSON serialization
    df_copy = expenses_df.copy()
    df_copy["date"] = df_copy["date"].dt.strftime("%Y-%m-%d %H:%M:%S")

    #covert data frame to a list of dictionaries
    #save expenses and income to a JSON file
    expenses_list = df_copy.to_dict(orient ="records")

    #save json
    with open(filename, "w") as f:
        json.dump({"expenses": expenses_list, "income": income}, f, indent=4)

    print("Expenses saved successfully!")


def load_expenses(filename= "expenses.json"):
    #Load expenses and income from JSON file
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            income = data.get("income", 0)
            expenses_list = data.get("expenses", [])

            #convert list of dictionaries back to data Frames
            expenses_df= pd.DataFrame(expenses_list,columns=["date", "category", "description", "amount"])
            if not expenses_df.empty:
                expenses_df["amount"] = expenses_df["amount"].astype(float)
                expenses_df["date"] = pd.to_datetime(expenses_df["date"])
            return expenses_df, income

    except FileNotFoundError:
        #If file not exist, start fresh
        columns = ["date", "category", "description", "amount"]
        return pd.DataFrame(columns=columns), 0

#-----------------------------
#Input Helper Functions
#-----------------------------

def get_positive_float(prompt):
    # make sure value is number and positive value
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a positive number")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a number.")


def get_category():
    #Prompt user to select a category from predefined list
    print("Choose a category")
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print("Invalid choice")
        except ValueError:
            print("Enter a number")


def get_valid_sort_choice():
    # ask user how they want to sort expenses for viewing
    print("Sort by:")
    print("1. Date (latest first)")
    print("2. Category")

    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [1, 2]:
                return choice
            else:
                print("Invalid choice")
        except ValueError:
            print("Enter a number")

#----------------------------
#Main Functions
#----------------------------

def main_menu():
    print("\nExpense Tracker (Pandas Version)")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses & Remaining Balance")
    print("4. Update Income")
    print("5. Category-wise summary")
    print("6. Monthly summary")
    print("7. Exit")


def add_expenses_pandas(expenses_df,income):
    #add a new expense to the DataFrame and save
    amount = get_positive_float("Enter amount to add: ")
    category = get_category()
    description = input("Enter description: ")
    date = datetime.now().replace(microsecond=0)

    #creating a dictionary
    new_expense = {
        "date" : date,
        "category" : category,
        "description" : description,
        "amount" : amount
    }

    # Add a new row at the end of the DataFrame using the next available index
    #pandas automatically transform a dictionary to a row
    expenses_df.loc[len(expenses_df)] = new_expense

    save_expenses(expenses_df,income)
    print("Expenses added successfully!")
    return expenses_df


def view_expenses_pandas(expenses_df,income):
    #view expense sorted by date or category
    if expenses_df.empty:
        print("No expenses recorded!")
        return

    sort_choice = get_valid_sort_choice()

    #sorted_df is still a data frame but in different order
    if sort_choice == 1:
        sorted_df = expenses_df.sort_values(by = "date", ascending = False)
    else:
        sorted_df = expenses_df.sort_values(by = "category")

    print("\nDate | Category | Description | Amount")
    print("-" * 60)
    # to_string = Converting this DataFrame into a nicely formatted text table.
    print(sorted_df.to_string(index=False))
    print("-" * 60)


def total_expenses_pandas(expenses_df,income):
    #show total expenses and remaining balance
    if expenses_df.empty:
        print("No expenses recorded!")
        return

    total_expense = expenses_df["amount"].sum()
    remaining_balance = income - total_expense

    print(f"\nTotal expense : {total_expense:.2f}")
    print(f"Remaining balance : {remaining_balance:.2f}\n")


def category_summary (expenses_df):
    #Display total expenses for each category
    if expenses_df.empty:
        print("No expenses recorded!")
        return

    #Goroup by category and show sum amounts for each category
    summary = expenses_df.groupby("category")["amount"].sum()
    summary = summary.sort_values(ascending = False)

    print("\nCategory-wise Expenses")
    print(summary.to_string())


def monthly_summary (expenses_df):
    #show total expenses grouped by month
    if expenses_df.empty:
        print("No expenses recorded!")
        return

    #create a Year-month column from date
    #'M' = get year-month period
    #Group by month and sum amounts
    summary = expenses_df.groupby(expenses_df["date"].dt.to_period("M"))["amount"].sum()

    print("\nMonthly Expenses Summary")
    print(summary.to_string())


#---------------------
#Main Loop
#---------------------

def main():

    # main() is the main loop of the program.
    # It loads existing data, asks for income if missing, then repeatedly shows the menu.
    # Based on the user’s choice, it calls the appropriate function.
    # Choice 7 saves data and exits the program.

    global expenses_df
    expenses_df, income = load_expenses() #load saved data

    if income == 0:
        income = get_positive_float("Enter your income: ")

    while True:
        main_menu()
        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                expenses_df = add_expenses_pandas(expenses_df,income)
            elif choice == 2:
                view_expenses_pandas(expenses_df,income)
            elif choice == 3:
                total_expenses_pandas(expenses_df,income)
            elif choice == 4:
                income = get_positive_float("Enter your income: ")
                print("Income updated successfully!")
            elif choice == 5:
                category_summary(expenses_df)
            elif choice == 6:
                monthly_summary(expenses_df)
            elif choice == 7:
                save_expenses(expenses_df,income)
                print("Exiting Program,Goodbye!😊")
                break
            else :
                print("Invalid choice. Enter a number between 1 and 7")
        except ValueError:
            print("Invalid Input! Enter a number.")

#----------------------------------
#Entry Point
#----------------------------------

if __name__ == "__main__":
    main()








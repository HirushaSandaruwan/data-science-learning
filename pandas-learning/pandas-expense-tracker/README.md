# Pandas Expense Tracker

This folder contains my **Pandas-based Expense Tracker** project, an upgrade from a previous **NumPy-based version**. This project helps track personal expenses, view summaries, and analyze spending patterns efficiently using **Pandas DataFrame functionalities**.

## Features

1. **Add Expenses**
   - Enter expense amount, category, description.
   - Automatically timestamps each entry.

2. **View Expenses**
   - View all recorded expenses sorted by **Date** or **Category**.
   - Nicely formatted table output.

3. **Total Expenses & Remaining Balance**
   - Calculates total spent and remaining balance based on income.

4. **Update Income**
   - Update total monthly or weekly income anytime.

5. **Category-wise Summary**
   - Shows total expenses grouped by predefined categories:
     - Food, Entertainment, Utilities, Transport, Others.

6. **Monthly Summary**
   - Shows total expenses grouped by month, making trend analysis easier.

7. **Persistence**
   - All expenses and income are saved in a **JSON file**.
   - Automatically loads saved data on program start.

## Improvements Over NumPy Version

- **Easier data manipulation:** Using Pandas DataFrames allows more intuitive data operations (sorting, grouping, filtering).
- **Better summaries and analysis:** Category-wise and monthly summaries are simpler to implement and display.
- **Enhanced readability:** Dates are automatically converted to datetime objects for easy operations.
- **Extensible:** Adding new analysis functions (like visualization) is easier with Pandas.

### How to Use the Pandas Expense Tracker

1. **Clone the repository to your local machine**

git clone https://github.com/HirushaSandaruwan/data-science-learning.git

2. **Navigate to the Pandas tracker folder**

cd data-science-learning/pandas-learning/pandas-expense-tracker

3. **Run the tracker in a Python 3 environment**

python Pandas_Expense_Tracker.py

4. **Follow the on-screen prompts**
   - Add new expenses by entering the amount, category, and description.
   - View all expenses, sort by date or category.
   - Check total expenses and remaining balance.
   - Update your income if needed.
   - See category-wise and monthly summaries for better spending insights.

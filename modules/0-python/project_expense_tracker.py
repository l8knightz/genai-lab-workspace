# Project - Personal Expense Tracker
# This script allows users to track their personal expenses by adding, viewing, and deleting expenses.
# Developed by: Travis B.
# Date: 2025-07-22
import datetime

expenses = [] # List to store expenses

import datetime

## Functions

def main_menu():
    print("Available commands:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    input_command = input("Enter command (1-3): ").strip()
    if input_command == "1":
        add_expense()
    elif input_command == "2":
        display_expenses()
    elif input_command == "3":
        print("Exiting the Expense Tracker. Goodbye!")
    else:
        print("Invalid command. Please enter a number between 1 and 3.")

def display_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nRecorded Expenses:")
    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. Date: {expense['date']}, Category: {expense['category']}, "
              f"Description: {expense['description']}, Amount: ${expense['amount']:.2f}")
    print()

def add_expense():
    date_str = input("Enter the date of expense (YYYY-MM-DD): ")
    try:
        expense_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    category = input("Enter category (food, travel, utilities, entertainment): ").strip().lower()
    description = input("Enter a description: ")
    try:
        amount = float(input("Enter the amount spent: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    if category not in ["food", "travel", "utilities", "entertainment"]:
        print("Invalid category. Please choose from food, travel, utilities, entertainment.")
        return
    print("Adding expense...")

    expense = {
        "date": expense_date,
        "category": category,
        "description": description,
        "amount": amount
    }
    expenses.append(expense)
    print(f"Expense added: {expense['date']} - {expense['category']} - {expense['description']} - ${expense['amount']:.2f}\n")

    if input("would you like to add another expense? (yes/no): ").strip().lower() == "yes":
        add_expense()   
    else:
        print("Returning to main menu...\n")
        main_menu()

### Prompts
print("Welcome to the Personal Expense Tracker!\n")

## Display available commands
main_menu()
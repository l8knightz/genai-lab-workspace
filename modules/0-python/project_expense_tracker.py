# Project - Personal Expense Tracker
# This script allows users to track their personal expenses by adding, viewing, and storing expenses.
# Developed by: Travis B.
# Date: 2025-07-27
import datetime
import csv
# Global Variables
expenses = [] # List to store expenses
CATEGORY_MAP = {
    "1": "Rent/Mortgage",
    "2": "Food",
    "3": "Travel",
    "4": "Utilities",
    "5": "Entertainment"
}

## Functions

# Main Menu Function 
def main_menu():
    print("Available commands:")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Create a Budget")
    print("4. Load/Save Expenses")
    print("5. Exit")

    input_command = input("Enter command (1-5): ").strip()
    if input_command == "1":
        add_expense()
    elif input_command == "2":
        display_expenses()
    elif input_command == "3":
        create_budget()
    elif input_command == "4":
        load_save_expenses()
    elif input_command == "5":
        print("Exiting the Expense Tracker. Goodbye!")
    else:
        print("Invalid command. Please enter a number between 1 and 5.")

# Prompt for Date Function (make it easier to use dates in expenses)
def prompt_for_date():
    """Keep asking until the user enters a valid YYYY-MM-DD (or MM-DD) date."""
    today = datetime.date.today()
    year = today.year

    while True:
        # Show the year so they can just type MM-DD - annoying to always type the year
        prompt = (
            f"Enter the date of expense (YYYY-MM-DD) "
            f"or just MM-DD for {year} [default today]: "
        )
        entry = input(prompt).strip()

        # Default to today if they hit Enter
        if entry == "":
            return today

        # If they entered MM-DD, prepend current year
        if len(entry) == 5 and entry.count("-") == 1:
            entry = f"{year}-{entry}"

        # Now try parsing
        try:
            return datetime.datetime.strptime(entry, "%Y-%m-%d").date()
        except ValueError:
            print("  Invalid date. Please use YYYY-MM-DD or MM-DD (e.g. 07-28).")

# Display the expenses 
def display_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nRecorded Expenses:")
    for idx, expense in enumerate(expenses, start=1):
        # convert the category to a readable format
        cat_label = CATEGORY_MAP.get(expense['category'], "Unknown")
        print(f"{idx}. Date: {expense['date']}, Category: {cat_label}, "
              f"Description: {expense['description']}, Amount: ${expense['amount']:.2f}")
    print()

# Add Expenses
def add_expense():
    expense_date = prompt_for_date()

    while True:
        print("Select the correct category:")
        for num, name in CATEGORY_MAP.items():
            print(f"  {num}. {name}")
        choice = input("Enter category number: ").strip()
        if choice in CATEGORY_MAP:
            category = choice
            break
        print("  → Invalid choice. Please enter one of:", ", ".join(CATEGORY_MAP.keys()))

    description = input("Enter a description: ")
    while True:
        amount_str = input("Enter the amount spent: ")
        try:
            amount = float(amount_str.replace(",", ""))  # Allows for commas in numbers
            break
        except ValueError:
            print("Invalid amount. Please enter a number without symbols except a decimal point.")
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

# Create a Budget Function
def create_budget():
    budget = float(input("Enter your monthly budget: "))
    total_expenses = sum(expense['amount'] for expense in expenses)
    remaining_budget = budget - total_expenses

    print(f"\nYour monthly budget is: ${budget:.2f}")
    print(f"Total expenses so far: ${total_expenses:.2f}")
    print(f"Remaining budget: ${remaining_budget:.2f}\n")

    if remaining_budget < 0:
        print("Warning: You have exceeded your budget!\n")
    else:
        print("You are within your budget.\n")

    exit_or_main_menu()

# Ensure CSV file function
def ensure_csv(filename):
    if not filename.lower().endswith(".csv"):
        print("Error: file must end with “.csv”")
        return False
    return True

# Load/Save Expenses Function
def load_save_expenses():
    action = input("Would you like to (1) Load expenses or (2) Save expenses? Enter 1 or 2: ").strip()
    
    if action == "1":
        filename = input("Enter filename to load (must end with .csv): ").strip()
        if not ensure_csv(filename):
            return load_save_expenses()
        try:
            with open(filename, "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                loaded = []
                for row in reader:
                    # Validate that all columns exist
                    if not {"date","category","description","amount"} <= row.keys():
                        raise ValueError("CSV missing required columns")
                    # Parse date and amount
                    dt = datetime.datetime.strptime(row["date"], "%Y-%m-%d").date()
                    amt = float(row["amount"])
                    cat = row["category"]
                    if cat not in CATEGORY_MAP:
                        raise ValueError(f"Unknown category {cat}")
                    loaded.append({
                        "date": dt,
                        "category": cat,
                        "description": row["description"],
                        "amount": amt
                    })
            # Only overwrite if everything parsed
            global expenses
            expenses = loaded
            print(f"Expenses loaded from {filename} successfully.\n")
        except FileNotFoundError:
            print(f"File {filename} not found.\n")
        except Exception as e:
            print(f"Error loading CSV: {e}\n")
    elif action == "2":
        filename = input("Enter filename to save (must end with .csv): ").strip()
        if not ensure_csv(filename):
            return load_save_expenses()  # re-prompt
        try:
            with open(filename, "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile,
                    fieldnames=["date","category","description","amount"])
                writer.writeheader()
                for exp in expenses:
                    # store date as ISO string, category as number
                    writer.writerow({
                        "date": exp["date"].isoformat(),
                        "category": exp["category"],
                        "description": exp["description"],
                        "amount": f"{exp['amount']:.2f}"
                    })
            print(f"Expenses saved to {filename} successfully.\n")
        except Exception as e:
            print(f"Error saving CSV: {e}\n")
    else:
        print("Invalid option. Please enter 1 or 2.\n")

    exit_or_main_menu()

# Exit or Main Menu Function
def exit_or_main_menu():
    if input("Would you like to return to the main menu? (yes/no): ").strip().lower() == "yes":
        main_menu()
    else:
        print("Exiting the Expense Tracker. Goodbye!")


### Prompts
print("Welcome to the Personal Expense Tracker!\n")

## Display available commands
main_menu()
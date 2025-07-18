# Tip Calculator
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
percent = int(input("How much tip would you like to give; 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tip = (percent / 100 * bill + bill) / people

print(f"Each person needs to cough up ${tip:.2f}.")

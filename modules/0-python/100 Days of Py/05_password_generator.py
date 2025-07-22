# Simple python based password generator - 100 Days of Python
import random
letters = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
    "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]

print("Welcome to the Py Password Generator!")
print("You can create a password with letters, numbers, and symbols.")
num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like? "))
num_numbers = int(input("How many numbers would you like? "))

ran_letters = random.sample(letters, num_letters)
ran_symbols = random.sample(symbols, num_symbols)
ran_numbers = random.sample(numbers, num_numbers)

new_password = [*ran_letters, *ran_symbols, *ran_numbers]
random.shuffle(new_password)

print(f"Your new password: {''.join(new_password)}")

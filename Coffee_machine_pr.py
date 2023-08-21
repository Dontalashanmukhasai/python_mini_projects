from Coffee_machine_data import Menu
from Coffee_machine_data import resources
import os
def system():
    os.system(cls)

choose_coffee = input("What would you like to have? Type '(espresso/latte/cappuccino)': ")
def currency():
    print("Please insert the coins.")
    print(input("How many ₹1000:"))
    print(input("How many ₹500:"))
    print(input("How many ₹200:"))
    print(input("How many ₹100:"))

profit = 0
def report():
    print(f"Water : {resources['water']}")
    print(f"Milk : {resources['milk']}")
    print(f"Coffee : {resources['coffee']}")
    print(f"Amount : {profit}")



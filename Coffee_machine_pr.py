from Coffee_machine_data import Menu
from Coffee_machine_data import resources

def currency():
    print("Please insert coins.")
    total = int(input("how many ₹1000?: "))*1000
    total += int(input("how many ₹500?: ")) *500
    total += int(input("how many ₹200?: ")) *200
    total += int(input("how many ₹100?: ")) *100
    return total

profit = 0
def report():
    print(f"Water : {resources['water']}")
    print(f"Milk : {resources['milk']}")
    print(f"Coffee : {resources['coffee']}")
    print(f"Amount : {profit}")

def resources_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item] >resources[item]:
            print(f"we are sorry,there is no sufficient {item}")
            return False
    return True

def transcation_check(amount_received,drink_cost):
    if amount_received >= drink_cost:
        change = round(amount_received-drink_cost,2)
        print(f"Here is the change ₹{change}. ")
        return True
    else:
        print("Sorry amount is not sufficient! ")
        return False
    
def make_coffe(drink_name,ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {choose_coffee} coffe.")

machine_on = True
while machine_on:
    choose_coffee = input("What would you like to have? Type '(espresso/latte/cappuccino)': ")
    if choose_coffee == "off":
        machine_on = False
    elif choose_coffee == "report":
        report()
    else:
        coffee = Menu[choose_coffee]
        if resources_sufficient(coffee["ingredients"]):
            payment = currency()
            if transcation_check(payment,coffee["cost"]):
                make_coffe(choose_coffee,coffee["ingredients"])

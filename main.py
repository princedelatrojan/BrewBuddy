# Brew Buddy Coffee Machine Program
from art import logo
import sys

# Menu and Resource definitions
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

cash = 0

# Function to check if resources are sufficient
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources.get(item, 0) < order_ingredients[item]:
            print(f"Sorry, not enough {item}.")
            return False
    return True

# Function to process the payment
def process_payment(cost):
    print(f"Please pay Ksh {cost}")
    try:
        amount = int(input("How much would you like to pay? Ksh: "))
        if amount < cost:
            print("Sorry, that's not enough money. Transaction cancelled.")
            return 0
        elif amount > cost:
            change = amount - cost
            print(f"Here is your change: Ksh {change}")
        return cost
    except ValueError:
        print("Invalid input. Please enter a number.")
        return 0

# Function to deduct resources
def make_coffee(order_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {order_name}. Enjoy! ")

# Admin report view
def report():
    print("Resources available:")
    for item, value in resources.items():
        unit = "ml" if item != "coffee" else "g"
        print(f"{item.title()}: {value}{unit}")
    print(f"Money: Ksh {cash}")

# Main program loop
coffee_on = True
print(logo)

while coffee_on:
    choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        print("\nMachine powering down. Goodbye!")
        coffee_on = False
    elif choice == "report":
        report()
    elif choice in MENU:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_payment(drink["cost"])
            if payment:
                cash += payment
                make_coffee(choice, drink["ingredients"])
    else:
        print("Invalid selection. Please choose from the menu or type 'report' or 'off'.")

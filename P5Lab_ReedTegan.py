# Tegan Reed
# 11/30/2025
# P5LAB
# generating a total owed ammount of dollars, quarters, dimes, nickels and pennies.

import random

def dispense_change(change):
    """
    Takes the amount of change owed (float) and prints the number of:
    dollars, quarters, dimes, nickels, and pennies required to make that change.
    Does not return anything.
    """

    
    cents = round(change * 100)

    
    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

 
    print(f"Dollars: {dollars}")
    print(f"Quarters: {quarters}")
    print(f"Dimes: {dimes}")
    print(f"Nickels: {nickels}")
    print(f"Pennies: {pennies}")


def main():
    
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${total_owed}")

    
    cash = float(input("How much cash will you put into the self-checkout? "))

    
    change = round(cash - total_owed, 2)

 
    print(f"Change owed: ${change}")

    
    dispense_change(change)



if __name__ == "__main__":
    main() 
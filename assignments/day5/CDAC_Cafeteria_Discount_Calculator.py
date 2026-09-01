"""
Assignment 1: CDAC Cafeteria Discount Calculator

Scenario
The CDAC Cafeteria needs a modular pricing function to calculate student bills. The cafeteria offers main combo meals, optional side-dishes, standard tax rates, promotional discounts, and delivery charges.

Problem Description
Write a function named calculate_cafeteria_bill(base_price, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0) that calculates the final bill.

base_price (float): The cost of the main combo meal.
*items (floats): A variable-length positional argument list representing prices of additional side items.
tax_rate (float): The tax percentage (default 0.05 for 5% tax). This must be a keyword-only parameter.
discount (float): A percentage value (e.g., 10.0 represents a 10% discount, default 0.0) applied directly to the subtotal before taxes.
delivery_fee (float): A flat shipping surcharge added to the final total after taxes (default 0.0).

Calculation Rules:

Sum the base_price and all side item prices (*items) to compute the raw subtotal.

Deduct the discount from the raw subtotal to compute the discounted subtotal: 

Discounted Subtotal = Raw Subtotal x (1 - discount/100)

Compute the tax value by multiplying the discounted subtotal by tax_rate.
Add the tax and delivery_fee to the discounted subtotal to get the final bill.
Return the final total rounded to 2 decimal places.
"""


def calculate_cafeteria_bill(base_price, *items, tax_rate=0.05, discount=0.0, delivery_fee=0.0) -> float:
    '''
    Function: calculates the bill and returns the bill.
    Returns -> Float Value
    '''
    sub_total = base_price + sum(items)
    dis_sub_total = sub_total * (1-(discount/100))
    tax = dis_sub_total * tax_rate
    total = dis_sub_total + tax + delivery_fee
    return f'{total:.2f}'

def main():
    '''
    Main Function of the code.
    '''
    print(calculate_cafeteria_bill(100.0))
    print(calculate_cafeteria_bill(100.0, 20.0, 30.0, tax_rate=0.08, discount=10.0, delivery_fee=15.0))

if __name__ == ("__main__"):
    main()
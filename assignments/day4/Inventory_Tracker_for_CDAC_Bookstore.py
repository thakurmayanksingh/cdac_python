"""
Assignment 1: Inventory Tracker for CDAC Bookstore
Scenario
The CDAC Bookstore needs a backend helper module to manage books and their quantities. 
The inventory is stored in a Python dictionary where keys are book titles (strings) and values are quantities in stock (non-negative integers).

Problem Description
Write a function manage_bookstore_inventory(inventory, action, book_title, quantity=0) that handles inventory operations safely.

The action parameter can be one of three options: "add", "sell", or "lookup".
Add Action ("add"):
Add the specified quantity to the existing stock of book_title.
If the book is not in the inventory dictionary, add it as a new key with quantity as the value.


Sell Action ("sell"):
Decrease the stock of book_title by the specified quantity.
If the book is not found in the inventory, print a message: Error: Book '<book_title>' not found in inventory. and make no changes. (Do not let the program crash with a KeyError).
If the requested quantity to sell exceeds the stock available, print: Error: Insufficient stock for '<book_title>'. Available: <current_stock>. and make no changes.
If the stock reaches exactly 0 after a successful sale, remove the book key from the inventory entirely.


Lookup Action ("lookup"):
Look up the stock quantity of book_title and return it.
Use safe dictionary retrieval; if the book does not exist, return 0 without throwing a KeyError.
The function must return the updated/current inventory dictionary.

Example Walkthrough:
# Initial Inventory
inventory = {"Python Basics": 10, "Learning AI": 5}

# 1. Add Stock
inventory = manage_bookstore_inventory(inventory, "add", "Python Basics", 5)
# Result: {"Python Basics": 15, "Learning AI": 5}

# 2. Sell Stock Safely (Missing Book)
inventory = manage_bookstore_inventory(inventory, "sell", "Data Science 101", 1)
# Console output: Error: Book 'Data Science 101' not found in inventory.

# 3. Sell Stock (Insufficient)
inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 10)
# Console output: Error: Insufficient stock for 'Learning AI'. Available: 5.

# 4. Sell Stock (Exactly Zero Stock)
inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 5)
# Result: {"Python Basics": 15}
"""

def line():
    print("-"*30)

def menu():
    print("*** MAIN MENU ***")
    print("=================")
    print("0. Exit")
    print("1. Add Stock")
    print("2. Sell Stock")
    print("3. View Stock")
    print("4. View all Stock")

    choice = int(input('Enter your choice: '))

    if choice < 0 or choice > 4:
        choice = -1

    return choice

inventory = {"Python Basics": 10, "Learning AI": 5,"Alchemist":18, "Ikigai":7}

def add_stock():
    
    title = input("Enter the Book title: ")
    while True:
        quant = int(input("Enter the Quantity of the book to add (Non-Negative): "))
        if quant > 0:
            break
        print("Please enter a valid positive number!")

    if title in inventory:
        inventory[title] += quant
    else:
        inventory[title] = 1

    print("Book is added successfully")
    

def del_stock():
    while True:
        title = input("Enter the title of the book you want to sell: ")
        if title not in inventory:
            print(f"{title} is not in inventory.\nEnter a valid title!")
            continue
        break
    while True:
        quant = int(input("Enter the Quantity of the book to add (Non-Negative): "))
        if quant > 0:
            break
        print("Please enter a valid positive number!")
    if title in inventory and inventory[title] >= quant:
        inventory[title] -= quant
        if inventory[title] == 0:
            del inventory[title]
        print(f"{title} is sold succesfully.\nRemaining quantity: {inventory[title]}")
    elif title in inventory and inventory[title] < quant:
        print(f"Error: Insufficient stock for '{title}'. Available: {inventory[title]}.")
    else:
        print(f"Error: Book '{title}' not found in inventory.")

def view_stock():
    title = input("Enter the title of the book you want to view: ")
    x = inventory.get(title, 0)
    print(f"{title}: {x}")
    
def view_all_stock():
    line()
    print(f"{"Title":<20} {"Quantity"}")
    line()
    for k, v in inventory.items():
        print(f"{k:<20}: {v:>5}")
    line()

def manage_book_store_inventory(inventory, action, book_title, quantity=0):
    ...

def main():
    while True:
        user_choice = menu()

        if user_choice == 0:
            break

        if user_choice == 1:
            add_stock()
        elif user_choice == 2:
            del_stock()
        elif user_choice == 3:
            view_stock()
        elif user_choice == 4:
            view_all_stock()
        else:
            print("Invalid choice! Please retry with valid value.")

        print()
    print("Bye!")

if __name__ == ("__main__"):
    main()

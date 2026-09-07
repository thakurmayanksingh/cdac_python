import csv

def line():
    print("-"*60)

p_id = 3
product_list = [
    {
        'ID': 1,
        'Name': 'Laptop',
        'Category': 'Electronics',
        'Price': 55000,
        'Quantity': 10
    },
    {
        'ID': 2,
        'Name': 'Smartphone',
        'Category': 'Electronics',
        'Price': 25000,
        'Quantity': 30
    },
    {
        'ID': 3,
        'Name': 'Chair',
        'Category': 'Furniture',
        'Price': 500,
        'Quantity': 3
    }
]

# Add product method
def add_product(name: str, category: str, price: float, quantity: int):
    global p_id, product_list
    mp = dict(ID=p_id+1, Name=name, Category=category, Price=price, Quantity = quantity)
    product_list.append(mp)
    p_id += 1
    return True

# view product
def view_product():
    line()
    print("VIEW PRODUCT")
    line()
    if len(product_list) > 1:
        print(f"{'ID':<4}{'Name':^15}{'Category':^15}{'Price':^15}{'Quantity':>10}")
        line()
        for d in product_list:
            print(f"{d['ID']:<4}{d['Name']:^15}{d['Category']:^15}{d['Price']:^15}{d['Quantity']:>10}")
        line()

    elif len(product_list) == 1:
        for d in product_list:
            print(f"ID -> {d['ID']}")
            print(f"Name -> {d['Name']}")
            print(f"Category -> {d['Category']}")
            print(f"Price -> {d['Price']}")
            print(f"Quantity -> {d['Quantity']}")
        line()

    else:
        print("Product List is empty!! Add a product first....")

# Search Product
def search_product() -> bool:
    choice = input("1 for search by ID and 2 for search by name: ")
    if choice.strip() == '1':
        try:
            search_id = int(input("Enter ID to search: "))
        except ValueError:
            print("Search ID must be an integer!!!")
        else:
            for data in product_list:
                if data.get('ID', 0) == search_id:
                    line()
                    print(data)
                    line()
                    return True
            return False

    elif choice.strip() == '2':
        search_name = input("Enter name to search: ")
        out = []
        for data in product_list:
            if data.get('Name', 0) == search_name:
                out.append(data)
        if out:
            line()
            print(out)
            line()
            return True
        else:
            return False

    else:
        line()
        print("Bad input! Returning to main menu!!!")
        return -1

# Update Product
def update_product():
    global p_id, product_list
    line()
    print("UPDATE PRODUCT")
    line()
    try:
        update_id = int(input("Enter ID to update: "))
    except ValueError:
        print("Value should be Integer!!!")
    else:
        for data in product_list:
            if data['ID'] == update_id:
                while True:
                    updated_name = input("Enter Product Name: ")
                    if updated_name:
                        break
                    print("Name cannot be empty!!")

                while True:
                    updated_category = input("Enter Product Category: ")
                    if updated_category:
                        break
                    print("Product category cannot be empty!!")

                while True:
                    try:
                        updated_price = float(input("Enter Product Price: "))
                        if updated_price > 0:
                            break
                        print("Price should be greater than 0.")
                    except ValueError:
                        print("Product price should be a nunber (integer/float)!!")

                while True:
                    try:
                        updated_quantity = int(input("Enter Product Quantity: "))
                        if updated_quantity >= 0:
                            break
                        print("Quantity cannot be less than 0.")
                    except ValueError:
                        print("Quantity should be a number (integer)")

                data['ID'] = update_id
                data['Name'] = updated_name
                data['Category'] = updated_category
                data['Price'] = updated_price
                data['Quantity'] = updated_quantity

                print("Data Updated Successfully!!!")
                break
        else:

            print("Product is not in the list!!!")

# Delete Product
def del_product():
    try:
        search_id = int(input("Enter ID to Delete: "))
    except ValueError:
        print("For Deletion, ID must be an integer!!!")
    else:
        for data in product_list:
            if data.get('ID', 0) == search_id:
                line()
                print(data)
                line()
                new_choice = input("Do you want to delete the product (y/n): ").strip()
                if new_choice.lower() == 'y':
                    product_list.remove(data)
                    return True
                else:
                    return False


# save to csv file
def save_to_csv(filename: str):
    line()
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as csv_file:
            fieldnames = ['ID', 'Name', 'Category', 'Price', 'Quantity']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for product in product_list:
                writer.writerow(product)
        print("Data saved successfully!!")
    except Exception as _:
        print("Error while saving the file!!")
    line()
    

# load the csv file
def load_csv(filename: str):
    global p_id, product_list
    try:
        with open(filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            temp_list = []
            for row in reader:
                mp = {
                    'ID': int(row['ID']),
                    'Name': row['Name'],
                    'Category': row['Category'],
                    'Price': float(row['Price']),
                    'Quantity': int(row['Quantity'])
                }
                temp_list.append(mp)
            p_id = 0
            for data in temp_list:
                if data['ID'] > p_id:
                    p_id = data['ID']

            # product_list.clear()
            # product_list.extend(temp_list)
            
            product_list = temp_list

        print("File Loaded Successfully!!!")

    except Exception as _:
        print("Error while loading the file!!")

def main():
    while True:
        print('******************** PRODUCT INVENTORY MANAGEMENT SYSTEM ********************')
        print('''Main Menu!!
1. Add Product
2. View All Products
3. Search Product
4. Update Product
5. Delete Product
6. Save to CSV
7. Load from CSV
8. Exit''')

        user_choice = input("Enter your choice -> ")
        if user_choice.strip() == '8':
            break

        elif user_choice == '1':
            while True:
                line()
                print("Add Product!")
                line()
                while True:
                    p_name = input("Enter Product Name: ")
                    if p_name:
                        break
                    print("Name cannot be empty!!")
                
                while True:
                    p_category = input("Enter Product Category: ")
                    if p_category:
                        break
                    print("Product category cannot be empty!!")

                while True:
                    try:
                        p_price = float(input("Enter Product Price: "))
                        if p_price > 0:
                            break
                        print("Price should be greater than 0.")
                    except ValueError:
                        print("Product price should be a nunber (integer/float)!!")

                while True:
                    try:
                        p_quantity = int(input("Enter Product Quantity: "))
                        if p_quantity >= 0:
                            break
                        print("Quantity cannot be less than 0.")
                    except ValueError:
                        print("Quantity should be a number (integer)")
                
                if add_product(p_name, p_category, p_price, p_quantity):
                    print("Product is added Successfully!!!")
                    line()
                    break

        elif user_choice == '2':
            view_product()

        elif user_choice == '3':
            if search_product() == -1:
                ...
            elif search_product():
                print("Product Found Successfully!!")
            else:
                print("No Product Found!!!")
                
        elif user_choice == '4':
            update_product()

        elif user_choice == '5':
            if del_product():
                print("Product Deleted Successfully!!")
            else:
                print("Product is not Deleted!!")

        elif user_choice == '6':
            filename = input("Enter Filename (No need to give extention): ")
            filename = filename+".csv"
            save_to_csv(filename)
        
        elif user_choice == '7':
            filename = input("Enter Filename to load (No need to give extention): ")
            filename = filename+".csv"
            load_csv(filename)
                

if __name__ == "__main__":  main()
import os, sys

def line():
    print("-"*70)

# ---------------------------------------------------------

book_id = 2
book_catalog = [
    {
        'id': 1,
        'title': "Python",
        'author': "Author",
        'genre': "genre",
        'price': 150.00,
        'copies': 5
    },
    {
        'id': 2,
        'title': "java",
        'author': "Author",
        'genre': "genre",
        'price': 1050.00,
        'copies': 7
    }
]

# ---------------------------------------------------------

def add_book_entry(catalog: list[dict], next_id: int) -> int:
    global book_catalog, book_id
    line()
    print("Enter book details below!")
    title = input("Enter book title: ")
    author_name = input("Enter Author Name: ")
    genre = input("Enter Genre (default None): ")
    try:
        price = float(input("Enter Price: "))
        stock = int(input("Enter Copies to add: "))
    except Exception as _:
        print("Invalid Input! Price and Copies should be only numbers.")
        choice = input("You want to retry? (y/n): ")
        if choice.lower().strip() == 'n':
            return
        elif choice.lower().strip() == 'y':
            return add_book_entry(catalog, next_id)
        else:
            print("Wrong input! Returning to main function!")
    else:
        book_mp = {
            'id': next_id,
            'title': title,
            'author': author_name,
            'genre': genre,
            'price': f"{price:.2f}",
            'copies': stock
        }

        book_id += 1
        book_catalog.append(book_mp)
        print("Book is Added Successfully!!")

# ---------------------------------------------------------

def render_catalog(catalog: list[dict]) -> None:
    if len(catalog) > 1:
        header = list(catalog[0].keys())
        line()
        print(f"{header[0]:<3} {header[1]:^10} {header[2]:^10} {header[3]:^10} {header[4]:^10} {header[5]:>10}")
        line()
        for data in catalog:
            print(f"{ data['id']:<3} {data['title']:^10} {data['author']:^10} {data['genre']:^10} {data['price']:^10} {data['copies']:>10}")
        line()

    elif len(catalog) < 1:
        print("No books in the Catalog! Try adding the book first!....")
    else:
        line()
        print(f"Id -> {catalog[0]['id']}")
        print(f"Title -> {catalog[0]['title']}")
        print(f"author -> {catalog[0]['author']}")
        print(f"genre -> {catalog[0]['genre']}")
        print(f"price -> {catalog[0]['price']:.2f}")
        print(f"copies -> {catalog[0]['copies']}")

# ---------------------------------------------------------

def query_books(catalog: list[dict], search_term: str, search_key) -> list[dict]:
    line()
    search_term = search_term.lower()
    if search_key == 'id':
        for dic in catalog:
            if str(dic['id']) == search_term:
                return [dic]
        return "Book is not Found!!!"

    elif search_key == 'title':
        for dic in catalog:
            if dic['title'].lower() == search_term:
                return [dic]
        return "Book is not Found!!!"

    elif search_key == 'author':
        ans = []
        for dic in catalog:
            if dic['author'].lower() == search_term:
                ans.append(dic)
        return ans if len(ans) > 0 else "Book is not Found!!!"

# ---------------------------------------------------------

def modify_book_details(catalog: list[dict], book_id: int) -> bool:
    for dic in catalog:
        if dic['id'] == book_id:
            try:
                new_price = float(input("Enter Price: "))
                new_stock = int(input("Enter Copies to add: "))
            except Exception as _:
                print("Invalid Input! Price and Copies should be only numbers.")
                choice = input("You want to retry? (y/n): ")
                if choice.lower().strip() == 'n':
                    return False
                elif choice.lower().strip() == 'y':
                    return modify_book_details(catalog, book_id)
                else:
                    print("Again a Wrong input! Returning to main function!")
            else:
                dic['price'] = f"{new_price:.2f}"
                dic['copies'] = new_stock
                return True
        
# ---------------------------------------------------------

def delete_book(catalog: list[dict], del_id: int) -> bool:
    for dic in catalog:
        if dic['id'] == del_id:
            line()
            print(dic)
            line()
            choice = input("Do you really want to delete the above book! (y/n): ")
            if choice == 'y':
                catalog.remove(dic)
                return True
            else:
                return False

# ---------------------------------------------------------

def sync_catalog_to_file(filepath: str, catalog: list[dict]) -> None:
    with open(filepath, mode='w', encoding='utf-8') as file:
        for book in catalog:
            record = f"{book['id']}|{book['title']}|{book['author']}|{book['genre']}|{book['price']}|{book['copies']}"
            file.write(record)
        print("File sync Successfully")

# ---------------------------------------------------------

def load_catalog_from_file(filepath: str) -> list[dict]:
    catalog = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        for line in file:
            out = line.strip().split("|")
            mp = {
                'id': out[0],
                'title': out[1],
                'author': out[2],
                'genre': out[3],
                'price': float(out[4]),
                'copies': int(out[5])    
            }
            catalog.append(mp)
    return catalog

# ---------------------------------------------------------

def main():
    global book_catalog, book_id
    line()
    print("********** LIBRARY BOOK MANAGEMENT SYSTEM **********")
    while True:
        line()

        print("Menu (1-8): ")
        user_choice = input('''1. Add Book
2. View Catalog
3. Search Books
4. Update Details
5. Delete Books
6. Save to File
7. Load from File
8. Exit\n-> ''')

# ---------------------------------------------------------

        if user_choice.strip() == '1':
            add_book_entry(book_catalog, book_id+1)

# ---------------------------------------------------------

        elif user_choice.strip() == '2':
            render_catalog(book_catalog)

# ---------------------------------------------------------

        elif user_choice.strip() == '3':
            line()
            while True:
                choice = input("Want to search by ID or Title or Author? (1 for id, 2 for title, 3 for author and 0 for main menu): ")
                
                if choice.strip() == '1':
                    try:
                        search_id = int(input("Enter ID to search: "))
                        print(query_books(book_catalog, str(search_id), 'id'))
                        break
                    except Exception as _:
                        print("Value much be an integer!")

                elif choice.strip() == '2':
                    search_title = input("Enter Title to search: ")
                    print(query_books(book_catalog, search_title, "title"))
                    break


                elif choice.strip() == '3':
                    search_author = input("Enter Author to search: ")
                    print(query_books(book_catalog, search_author, 'author'))

                elif choice.strip() == '0':
                    break

                else:
                    print("Enter a valud choice!")



# -------------------------------------------------
            

        elif user_choice.strip() == '4':
            line()
            print("Welcome to book modification!")
            while True:
                try:
                    inp = int(input("Enter the book id you want to modify (0 for main menu): "))
                    if inp<0:
                        print("Enter a valid Book ID! (Book ID should be greater than 0)")
                        print()
                    elif inp == 0:
                        break
                    else:
                        is_success = modify_book_details(book_catalog, inp)
                        if is_success:
                            print("Book details are updated Successfully!")
                            break
                        else:
                            print("Book details are not updated!\nTry again later...")
                            break

                except Exception as _:
                    line()
                    print("Book ID must be an integer!\nEnter Valid Value!!")
                    line()
            
    
# -------------------------------------------------

        elif user_choice.strip() == '5':
            line()
            print("Welcome to Delete Book Menu!")
            while True:
                try:
                    del_id = int(input("Enter a book ID to delete (0 for main menu): "))
                except Exception as _:
                    line()
                    print("Book ID must be an integer!\nEnter Valid Value!!")
                    line()
                else:
                    if del_id == 0:
                        print("Returning to main menu!")
                        break
                    is_deleted = delete_book(book_catalog, del_id)
                    if is_deleted:
                        print("Book is deleted successfully!!")
                        break
                    else:
                        print("Book is not deleted!! Returning to main menu!")
                        break

# -------------------------------------------------


        elif user_choice.strip() == '6':
            filepath = "books.txt"
            sync_catalog_to_file(filepath, book_catalog)


# -------------------------------------------------

        elif user_choice.strip() == '7':
            filepath = "books.txt"
            book_catalog = load_catalog_from_file(filepath)
            book_id = len(book_catalog)


# -------------------------------------------------

        elif user_choice.strip() == '8':
            line()
            print("Thank you for using!\nQuiting!!!")
            break

# -------------------------------------------------

        else:
            line()
            print("Invalid input!\n(Choose between value between 1-8)")
            line()


# -------------------------------------------------


if __name__ == "__main__":  main()
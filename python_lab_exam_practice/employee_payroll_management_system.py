import json, csv

# ----------------------------------------------------------------------------------------------------

def line():
    print("-"*70)

# ----------------------------------------------------------------------------------------------------

emp_id = 2
employees = [
    # {"id": 1, "name": "Ravi Kumar", "department": "Sales", "basic_salary": 30000, "allowances": 5000, "deductions": 2000, 'net_salary': 33000},
    # {"id": 2, "name": "Anita Rao", "department": "IT", "basic_salary": 45000, "allowances": 8000, "deductions": 3000, 'net_salary': 50000}
]

# ----------------------------------------------------------------------------------------------------

def add_employee(name: str, dept: str, basic_salary: float, allowances: float, deduction: float, net_salary: float) -> bool:
    global emp_id, employees

    mp = {
        'id': emp_id+1,
        'name': name,
        'department': dept,
        'basic_salary': basic_salary,
        'allowances': allowances,
        'deductions': deduction,
        'net_salary': net_salary
    }

    employees.append(mp)
    emp_id += 1
    return True

# ----------------------------------------------------------------------------------------------------

def view_employees(employees_list):
    if not employees_list:
        print("No employee data found!\nAdd an Employee data first!")
        return
    
    if len(employees_list) == 1:
        line()
        print("View Employee Data!!")
        line()
        e_id, name, dept, basic_salary, allowances, deduction, net_salary = employees_list[0].values()
        print(f"ID           : {e_id}")
        print(f"Name         : {name}")
        print(f"Department   : {dept}")
        print(f"Basic Salary : {basic_salary}")
        print(f"Allowances   : {allowances}")
        print(f"Deduction    : {deduction}")
        print(f"Net Salary   : {net_salary}")
        line()
    
    elif len(employees_list) > 1:
        line()
        print("View Employee's Data!!")
        line()
        print(f"{'ID':<5}{'Name':^20}{'Department':^15}{'Basic Salary':^15}{'Allowances':^15}{'Deduction':^15}{'Net Salary':^15}")
        for emp in employees_list:
            e_id, name, dept, basic_salary, allowances, deduction, net_salary = emp.values()
            print(f"{e_id:<5}{name:^20}{dept:^15}{basic_salary:^15}{allowances:^15}{deduction:^15}{net_salary:^15}")
        line()
    
# ----------------------------------------------------------------------------------------------------

def search_employee(search_term: str):
    if search_term.isnumeric():
        print("SEARCHING EMPLOYEE BY ID.....")
        for emp in employees:
            if int(emp['id'] )== int(search_term):
                print("EMPLOYEE MATCH FOUND.....")
                view_employees([emp])
                return True
    else:
        print("SEARCHING EMPLOYEES BY NAME.....")
        out = []
        for emp in employees:
            if search_term.lower() in emp['name'].lower():
                out.append(emp)
        view_employees(out)
        return True

    return False

# ----------------------------------------------------------------------------------------------------

def del_employee(del_id: int):
    global employees
    line()
    print('ENTERING REMOVE EMPLOYMENT MENU!!')
    line()
    for emp in employees:
        if int(emp['id']) == del_id:
            print("Employee Found!")
            view_employees([emp])
            final_choice = input("You sure want to delete this employee? (y/n): ").strip().lower()
            if final_choice == 'y':
                employees.remove(emp)
                line()
                print("EMPLOYEE REMOVED/DELETED SUCCESSFULLY!!!")
                return
            else:
                print("Employee is not Deleted!!\nGoing back to main menu!!!")
                return
    print("No Employee Found with this ID...\nGoing back to main menu!")
    
# ----------------------------------------------------------------------------------------------------

def update_employee(employees_list: list[dict], update_id: int):
    for emp in employees_list:
        if int(emp['id']) == update_id:
            print("EMPLOYEE MATCH FOUND.....")
            view_employees([emp])

            name = input(f"Enter updated name (Press Enter to keep {emp['name']}): ").strip()
            if name == '':
                name = emp['name']
            
            dept = input(f"Enter updated Department name (Press Enter to keep {emp['department']}): ").strip()
            if dept == '':
                dept = emp['department']

            while True:
                raw_sal = input(f"Enter updated basic salary (Press Enter to keep {emp['basic_salary']}): ").strip()
                if not raw_sal:
                    basic_salary = float(emp['basic_salary'])
                    break
                try:
                    basic_salary = float(raw_sal)
                    if basic_salary > 0:
                        break
                    print("Retry with valid value (Positive Number)!!")
                except ValueError:
                    print("Invalid input for salary!! Retry with a valid number!!")
            
            while True:
                raw_allow = input(f"Enter updated allowances (Press Enter to keep {emp['allowances']}): ").strip()
                if not raw_allow:
                    allowances = float(emp['allowances'])
                    break
                try:
                    allowances = float(raw_allow)
                    if allowances >= 0:
                        break
                    print("Retry with valid value (Positive Number or Zero)!!")
                except ValueError:
                    print("Invalid input for allowances!! Retry with a valid number!!")

            while True:
                raw_ded = input(f"Enter updated deduction amount (Press Enter to keep {emp['deductions']}): ").strip()
                if not raw_ded:
                    deduction = float(emp['deductions'])
                    if deduction < (basic_salary + allowances):
                        break
                    print("Previous deduction is now larger than new total salary! Please enter a new valid deduction.")
                    continue
                    
                try:
                    deduction = float(raw_ded)
                    if (deduction >= 0) and (deduction < (basic_salary + allowances)):
                        break
                    print("Retry with valid value (Positive Number, must be less than Basic + Allowances)!!")
                except ValueError:
                    print("Invalid input for deduction!! Retry with a valid number!!")

            net_salary = ((basic_salary+allowances) - deduction)
            line()
            print("Updating Values!!!!")

            emp['name'] = name
            emp['department'] = dept
            emp['basic_salary'] = basic_salary
            emp['allowances'] = allowances
            emp['deductions'] = deduction
            emp['net_salary'] = net_salary
            print("Values are Updated Successfully!!!")
            return

    print(f"No employee found with the ID: {update_id}")
            
# ----------------------------------------------------------------------------------------------------

def save_to_file(filename: str):
    with open(filename, mode='w', encoding='utf-8') as txt_file:
        for record in employees:
            e_id, name, dept, basic_salary, allowances, deduction, net_salary = record.values()
            txt_file.write(f"{e_id}|{name}|{dept}|{basic_salary}|{allowances}|{deduction}|{net_salary}\n")
    print("File Exported Successfully!!")

# ----------------------------------------------------------------------------------------------------

def load_from_file(filename: str) -> list[dict]:
    line()
    try:
        with open(filename, mode='r', encoding='utf-8') as txt_file:
            out = []
            for l in txt_file:
                line_list = l.strip().split("|")
                e_id, name, dept, basic_salary, allowances, deduction, net_salary = line_list
                mp = {
                    'id': int(e_id),
                    'name': name,
                    'department': dept,
                    'basic_salary': float(basic_salary),
                    'allowances': float(allowances),
                    'deductions': float(deduction),
                    'net_salary': float(net_salary)
                }
                out.append(mp)
            print("File Loaded Successfully!!!")
            return out
    except FileNotFoundError:
        print("No File Found with this name!!!\nFile not Loaded!!\nReturnning to main menu!!!")
        return []

# ----------------------------------------------------------------------------------------------------

def save_to_json(filename: str):
    with open(filename, mode='w', encoding='utf-8') as json_file:
        json.dump(employees, json_file,indent=4)
    print("File Exported Successfully!!")

# ----------------------------------------------------------------------------------------------------

def load_from_json(filename: str) -> list[dict]:
    line()
    try:
        with open(filename, mode='r', encoding='utf-8') as json_file:
            print("File Loaded Successfully!!!")
            return json.load(json_file)
    except FileNotFoundError:
        print("No File Found with this name!!!\nFile not Loaded!!\nReturnning to main menu!!!")
        return []

# ----------------------------------------------------------------------------------------------------

def save_to_csv(filename: str):
    with open(filename, mode='w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['id', 'name', 'department', 'basic_salary', "allowances", 'deductions', 'net_salary'], lineterminator="\n")
        writer.writeheader()
        writer.writerows(employees)
    print("File Exported Successfully!!")

# ----------------------------------------------------------------------------------------------------

def load_from_csv(filename: str) -> list[dict]:
    try:
        with open(filename, mode='r', encoding='utf-8') as csv_file:
            read = csv.DictReader(csv_file)
            out = []
            for row in read:
                row['id'] = int(row["id"])
                row['basic_salary'] = float(row['basic_salary'])
                row['allowances'] = float(row['allowances'])
                row['deductions'] = float(row['deductions'])
                row['net_salary'] = float(row['net_salary'])
                out.append(row)
            print("File Loaded Successfully!!!")
            return out
    except FileNotFoundError:
        print("No File Found with this name!!!\nFile not Loaded!!\nReturnning to main menu!!!")
        return []

# ----------------------------------------------------------------------------------------------------

def main():
    global employees, emp_id
    while True:
        line()
        print("****************** EMPLOYEE PAYROLL MANAGEMENT SYSTEM ******************")
        line()
        print('''0. Exit
1. Add Employee
2. View All Employee
3. Search Employee
4. Update Employee
5. Delete Employee
6. Export to Text File
7. Export to JSON File
8. Export to CSV File
9. Load File
''')

# ----------------------------------------------------------------------------------------------------

        user_choice = input("Enter your choice: ").strip()

# ----------------------------------------------------------------------------------------------------

        if user_choice == '0':
            print("Thank you for using! Quitting!!!")
            break

# ----------------------------------------------------------------------------------------------------

        elif user_choice == '1':
            line()
            print("Adding an Employee Record!")
            line()
            while True:
                name = input("Enter name: ").strip()
                if name:
                    break
                else:
                    print("Name cannot be empty! Re-enter with a valid name!!")

            while True:
                dept = input("Enter Department name: ").strip()
                if dept:
                    break
                else:
                    print("Department cannot be empty! Re-enter with a valid Department!!")

            while True:
                try:
                    basic_salary = float(input("Enter your basic salary: "))
                except Exception as e:
                    print(f"Invalid input for salary!! System says - '{e}'\nRetry with valid value (Positive Number)!!")
                else:
                    if basic_salary > 0:
                        break
                    else:
                        print("Retry with valid value (Positive Number)!!")
                        continue
            
            while True:
                try:
                    allowances = float(input("Enter your allowances: "))
                except Exception as e:
                    print(f"Invalid input for allowances!! System says - '{e}'\nRetry with valid value (Positive Number)!!")
                else:
                    if allowances >= 0:
                        break
                    else:
                        print("Retry with valid value (Positive Number)!!")
                        continue

            while True:
                try:
                    deduction = float(input("Enter your deduction amount: "))
                except Exception as e:
                    print(f"Invalid input for deduction!! System says - '{e}'\nRetry with valid value (Positive Number)!!")
                else:
                    if (deduction > 0) and (deduction < (basic_salary + allowances)):
                        break
                    else:
                        print("Retry with valid value (Positive Number)!!")
                        continue

            net_salary = ((basic_salary+allowances) - deduction)
            
            if add_employee(name, dept, basic_salary, allowances, deduction, net_salary):
                line()
                print("Employee Data Added Succesfully!!")
            else:
                print("Error while Adding Employee Data!\nRetry Again!!!")

# ----------------------------------------------------------------------------------------------------

        elif user_choice == '2':
            view_employees(employees)

# ----------------------------------------------------------------------------------------------------

        elif user_choice == '3':
            line()
            print("Search Employee (by ID/NAME)")
            search_term = input("Enter Employee Credentials to search (ID/NAME): ").strip()
            if not search_employee(search_term):
                print("No Employee record found!!!")

# ----------------------------------------------------------------------------------------------------

        elif user_choice == '4':
            line()
            print("Entering Update Employee Menu!!!")
            line()
            try:
                update_id = int(input("Enter Employee ID to Update: "))
            except Exception as e:
                print(f"ERROR!\nSYSTEM SAYS - {e}\nRETRY WITH A VALID ID (INTEGER ONLY)")
            else:
                update_employee(employees, update_id)

# ----------------------------------------------------------------------------------------------------

        elif user_choice == '5':
            try:
                del_id = int(input("Enter Employee ID to Delete: "))
            except Exception as e:
                print(f"ERROR!\nSYSTEM SAYS - {e}\nRETRY WITH A VALID ID (INTEGER ONLY)")
            else:
                del_employee(del_id)

# ----------------------------------------------------------------------------------------------------

        elif user_choice == '6':
            line()
            print("Entering Export to Text File Menu!!")
            line()
            filename = input("Enter name of the file you want to export to: ")
            if not filename.endswith(".txt"):
                filename += '.txt'
            save_to_file(filename)

# ----------------------------------------------------------------------------------------------------

        elif user_choice == '7':
            line()
            print("Entering Export to JSON File Menu!!")
            line()
            filename = input("Enter name of the file you want to export to: ")
            if not filename.endswith(".json"):
                filename += '.json'
            save_to_json(filename)

# ----------------------------------------------------------------------------------------------------

        elif user_choice == '8':
            line()
            print("Entering Export to CSV File Menu!!")
            line()
            filename = input("Enter name of the file you want to export to: ")
            if not filename.endswith(".csv"):
                filename += '.csv'
            save_to_csv(filename)

# ----------------------------------------------------------------------------------------------------

        elif user_choice == '9':
            line()
            print("Entering Load File Menu!!")
            line()
            filename = input("Enter name of the file you want to load: ")
            if filename.endswith(".txt"):
                employees = load_from_file(filename)
                if employees:
                    emp_id = len(employees)
            if filename.endswith(".json"):
                employees = load_from_json(filename)
                if employees:
                    emp_id = len(employees)
            if filename.endswith(".csv"):
                employees = load_from_csv(filename)
                if employees:
                    emp_id = len(employees)

# ----------------------------------------------------------------------------------------------------
        
        else:
            print("Invalid Input!! Values should be in range(0-9)")

# ----------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
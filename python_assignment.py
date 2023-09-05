print("Name: Medha Agarwal")
print("Roll No. E22CSEU0851\n\n")

class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

employees = [
    Employee("161E90", "Raman", 41, 56000),
    Employee("161F91", "Himadri", 38, 67500),
    Employee("161F99", "Jaya", 51, 82100),
    Employee("171E20", "Tejas", 30, 55000),
    Employee("171G30", "Ajay", 45, 44000)
]

def search_by_age():
    print()
    try:
        age_operator = input("Enter age operator (<, >, <=, >=): ")
        age_value = int(input("Enter age value: "))

        for employee in employees:
            if age_operator == '<' and employee.age < age_value:
                print_employee(employee)
            elif age_operator == '>' and employee.age > age_value:
                print_employee(employee)
            elif age_operator == '<=' and employee.age <= age_value:
                print_employee(employee)
            elif age_operator == '>=' and employee.age >= age_value:
                print_employee(employee)
    except ValueError:
        print("Invalid input. Age value must be an integer.")

def search_by_salary():
    print()
    try:
        salary_operator = input("Enter salary operator (<, >, <=, >=): ")
        salary_value = int(input("Enter salary value: "))

        for employee in employees:
            if salary_operator == '<' and employee.salary < salary_value:
                print_employee(employee)
            elif salary_operator == '>' and employee.salary > salary_value:
                print_employee(employee)
            elif salary_operator == '<=' and employee.salary <= salary_value:
                print_employee(employee)
            elif salary_operator == '>=' and employee.salary >= salary_value:
                print_employee(employee)
    except ValueError:
        print("Invalid input. Salary value must be an integer.")

def search_by_employee_id():
    print()
    emp_id = input("Enter Employee ID: ")
    for employee in employees:
        if emp_id == employee.emp_id:
            print_employee(employee)
            return
    print("Employee not found.")

def print_employee(employee):
    print()
    print(f"Employee ID: {employee.emp_id}")
    print(f"Name: {employee.name}")
    print(f"Age: {employee.age}")
    print(f"Salary: {employee.salary}")
    print()

while True:
    print("Menu:")
    print("1. Search by Age")
    print("2. Search by Salary")
    print("3. Search by Employee ID")
    print("4. Exit")
    print()
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        search_by_age()
    elif choice == '2':
        search_by_salary()
    elif choice == '3':
        search_by_employee_id()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please enter a valid option.")

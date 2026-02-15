employee={
   101:{'name':'fazeel','age':23,'department':'HR','salary':45000},
   102:{'name': 'Ravi', 'age': 30, 'department': 'Sales', 'salary': 40000},
   103:{'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000}
}
def add_employee():
    emp_id=int(input('enter employee id'))
    if emp_id in employee:
        print('employee alredy exist')
        return
    name=input('enter your name :')
    age=int(input('enter your age : ')) 
    department=input('enter your department: ')   
    salary=int(input('enter your salary: '))
    employee[emp_id]={
        'name':name,
        'age':age,
        'department':department,
        'salary':salary
    }
    print('employee details added successfully')
def view_employees():
    if not employee:
        print('employee not present in employee')
        return
    for emp_id,details in employee.items():
        print(f"{emp_id}\t{details['name']}\t{details['age']}\t{details['department']}\t{details['salary']}")
def search_employee():
    emp_id=int(input('enter employee id'))       
    if emp_id in employee:
        details=employee[emp_id]
        print(f"name of employee is :{details['name']}")
        print(f"age of employee is: {details['age']}")
        print(f"department of employee is: {details['department']}")
        print(f"salary  of employee is: {details['salary']}")
    else:
         print("Employee not found.") 
def main_menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search for Employee")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()              

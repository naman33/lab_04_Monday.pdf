class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def sort_and_print(self, key):
        if key == 1:  
            sorted_employees = sorted(self.employees, key=lambda x: x.age)
        elif key == 2:  
            sorted_employees = sorted(self.employees, key=lambda x: x.name)
        elif key == 3:  
            sorted_employees = sorted(self.employees, key=lambda x: x.salary)
        else:
            print("Invalid sorting option.")
            return

        for employee in sorted_employees:
            print(employee)


if __name__ == "__main__":
    emp_table = EmployeeTable()

    emp_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    sorting_key = int(input("Sort by (1. Age, 2. Name, 3. Salary): "))

    emp_table.sort_and_print(sorting_key)

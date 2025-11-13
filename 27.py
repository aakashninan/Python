"""Program to createa class Employee that keeps track of the total number of employees created (use class variable and static method) @AakashNinan IMCA Rollno:02.														 """
class Employee:
    total_employees = 0

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        Employee.total_employees += 1

    @staticmethod
    def get_total_employees():
        return Employee.total_employees

if __name__ == "__main__":
    emp1 = Employee("Alice", "E001")
    print(f"Employee created: {emp1.name}")
    print(f"Total employees so far: {Employee.get_total_employees()}")
    print("-" * 20)

    emp2 = Employee("Bob", "E002")
    print(f"Employee created: {emp2.name}")
    print(f"Total employees so far: {Employee.get_total_employees()}")
    print("-" * 20)

    emp3 = Employee("Charlie", "E003")
    print(f"Employee created: {emp3.name}")
    print(f"Total employees so far: {Employee.get_total_employees()}")
    print("-" * 20)

    print(f"Final count of employees: {Employee.total_employees}")
    print(f"Final count from static method: {Employee.get_total_employees()}")
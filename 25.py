""""Program to create a class Student with attributes name, roll number, and marks. Display the details of 3 students. @AakashNinan IMCA Rollno:02"""														
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}, Roll Number: {self.roll_number}, Marks: {self.marks}")


student1 = Student("Alice", "A101", 85.5)
student2 = Student("Bob", "B202", 92.0)
student3 = Student("Charlie", "C303", 78.9)

print("--- Student Details ---")

student1.display_details()
student2.display_details()
student3.display_details()
"""Program to Implement Student Records System using MVC Architecture@AakashNinan IMCA Rollno:02"""
class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks


class StudentView:
    def display(self, student):
        print(f"Roll: {student.roll}, Name: {student.name}, Marks: {student.marks}")


class StudentController:
    def __init__(self, student, view):
        self.student = student
        self.view = view

    def set_name(self, name):
        self.student.name = name

    def set_marks(self, marks):
        self.student.marks = marks

    def update_view(self):
        self.view.display(self.student)


s = Student(1, "Alice", 85)
v = StudentView()
c = StudentController(s, v)

c.update_view()
c.set_name("Alicia")
c.set_marks(90)
c.update_view()

"Write a program to create a dictionary of student names and marks, then print students who scored above 75.@AakashNinan IMCA Rollno:02"""
students = {"Alan": 82,"Thomas": 67,"Vivek": 90,"David": 74,"Shikha": 88
}
print("Students who scored above 75:")
for name, marks in students.items():
    if marks > 75:
        print(name, ":", marks)

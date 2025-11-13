"""Write a program to create a nested dictionary of student names and their subject marks, then display each student’s details.@AakashNinan IMCA Rollno:02"""
students = {"Alice": {"Math": 85, "Science": 92, "English": 78},"Bob": {"Math": 68, "Science": 74, "English": 80},"Charlie": {"Math": 90, "Science": 88, "English": 85}
}

for name, subjects in students.items():
    print(f"\nStudent: {name}")
    for subject, marks in subjects.items():
        print(f"  {subject}: {marks}")

"""Write a program to define a custom exception for invalid marks  and raise it if the input is invalid@Aakashninan IMCA Rollno:02"""
try:
    marks = float(input("Enter marks: "))
    if marks < 0 or marks > 100:
        raise Exception("Invalid marks: Marks should be between 0 and 100.")
    print("Marks are valid:", marks)
except Exception as e:
    print("Error:", e)

"""" Program to print a pyramid of numbers using loop @AakashNinan IMCA Rollno:02"""
rows = int(input("Enter the number of rows"))
for i in range(1, rows + 1):
    for space in range(rows - i):
        print(" ", end="")
    for num in range(1, i + 1):
        print(num, end="")
    for num in range(i - 1, 0, -1):
        print(num, end="")
    print()

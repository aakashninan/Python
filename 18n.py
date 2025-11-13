""""Program to write 5 lines to a file and append two line @Aakashninan IMCA Rollno:02"""
with open("my_file2.txt", "w") as file:
    file.write("This is line 1\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")
    file.write("This is line 4\n")
    file.write("This is line 5\n")

print("Before appending:")
with open("my_file2.txt", "r") as file:
    print(file.read())

with open("my_file2.txt", "a") as file:
    file.write("This is line 6 (appended)\n")
    file.write("This is line 7 (appended)\n")

print("After appending:")
with open("my_file2.txt", "r") as file:
    print(file.read())

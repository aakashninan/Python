
with open("my_file.txt", "w") as file:
    file.write("This is line 1\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")
    file.write("This is line 4\n")
    file.write("This is line 5\n")

with open("my_file.txt", "a") as file:
    file.write("This is line 6 (appended)\n")
    file.write("This is line 7 (appended)\n")

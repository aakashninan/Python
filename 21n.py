""""Program that handles multiple exceptions Zer Division,Value error and idex error @Aakashninan IMCA Rollno:02"""
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    lst = [10, 20, 30]
    index = int(input("Enter index to access from list: "))
    result = a / b
    print("Division result:", result)
    print("List element:", lst[index])
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input, enter numeric values only.")
except IndexError:
    print("Error: Index out of range.")

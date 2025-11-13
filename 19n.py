""""Program to handle Zero Division error while dividing two number@AakashninAN IMCARollno:02"""
try:
    a = float(input("Enter numerator: "))
    b = float(input("Enter denominator: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero.")

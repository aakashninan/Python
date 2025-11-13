""""Program to print the factorial of a number using recursion @Aakashnina IMCA Rollno:02"""
def fact(n):
    if(n==0):
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter a number "))
a=num
num=fact(num)
print("Factorial of",a,"is ",num)


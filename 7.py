"Program to check whether a number entered is prime or not @authorAakashninan IMCA Rollno:02"""


num = int(input("Enter a number: "))
half=((num/2)+1)
num2=int(half)

if num > 1:
    for i in range(2,num2+1):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

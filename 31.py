"""Program to Generate Fibonacci Sequence up to a Limit@AakashNinan IMCA Rollno:02"""
def fibonacci(limit):
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

n = int(input("Enter the limit: "))
for num in fibonacci(n):
    print(num, end=" ")

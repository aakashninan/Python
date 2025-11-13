"""Generator function that yields squares of numbers up to n.@AakashNinan IMCA Rollno:02"""
def generate_squares(n):
    for i in range(1, n + 1):
        yield i * i

n = int(input("Enter a number: "))
for square in generate_squares(n):
    print(square)

"""decorator that allows a function to be executed only a maximum of n times. After that, it should display 'Function call limit reached'.@AakashNinan IMCA Rollno:02"""
def limit_calls(n):
    def decorator(func):
        count = {"calls": 0}
        def wrapper(*args, **kwargs):
            if count["calls"] < n:
                count["calls"] += 1
                return func(*args, **kwargs)
            else:
                print("Function call limit reached")
        return wrapper
    return decorator

@limit_calls(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Aakash")
greet("Priya")
greet("John")
greet("Sara")

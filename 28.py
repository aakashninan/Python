"""Decorator that checks if the argument passed to a function is an integer.@AakashNinan IMCA Rollno:02"""
def check_integer(func):
    def wrapper(arg):
        if not isinstance(arg, int):
            raise TypeError(f"Argument must be an integer, got {type(arg).__name__} instead.")
        return func(arg)
    return wrapper


@check_integer
def square(n):
    return n * n



print(square(5))   
print(square("5")) 

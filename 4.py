import cmath
""""Program to find the roots of a quadratic equation"""
print("The quadratic expression is in the Ax^2 +Bx+C")
a=float(input("Enter the coefficient of a"))
b=float(input("Enter the coefficient of b"))
c=float(input("Enter the coefficient of c"))
d = (b**2) - (4*a*c)
root1=(-b+(cmath.sqrt(d)))/(2*a)
root2=(-b-(cmath.sqrt(d)))/(2*a)

print("The two roots are ",root1," ",root2)
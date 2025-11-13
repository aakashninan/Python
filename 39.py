"""Program to Add Fractions Using Operator Overloading@AakashNinan IMCA Rollno:02"""
import math

class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __add__(self, other):
        num = self.num * other.den + other.num * self.den
        den = self.den * other.den
        g = math.gcd(num, den)
        return Fraction(num // g, den // g)

    def __str__(self):
        return f"{self.num}/{self.den}"

f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
print(f1, "+", f2, "=", f1 + f2)

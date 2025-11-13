"""Program to create two matrices and perform addition, subtraction, multiplication, and transpose using NumPy.@AakashNinan IMCA Rollno:02"""												
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

print("Matrix A:\n", a)
print("Matrix B:\n", b)

print("Addition:\n", a + b)
print("Subtraction:\n", a - b)
print("Multiplication:\n", a * b)
print("Transpose of A:\n", a.T)
print("Transpose of B:\n", b.T)

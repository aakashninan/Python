"""Program to create a NumPy array with 10 random integers and find their mean and standard deviation. @AakashNinan IMCA Rollno:02"""												
import numpy as np

arr = np.random.randint(1, 101, size=10)
print("Array:", arr)
mean_val = np.mean(arr)
std_dev = np.std(arr)
print("Mean:", mean_val)
print("Standard Deviation:", std_dev)

"""Program to Compare Sequential and Multithreaded File Reading@AakashNinan IMCA Rollno:02"""
import threading, time

def read_file(name):
    with open(name, "r") as f:
        f.read()

f1, f2 = "sample.txt", "myfile.txt"

t = time.time()
read_file(f1); read_file(f2)
print("Sequential:", time.time() - t, "s")

t = time.time()
t1 = threading.Thread(target=read_file, args=(f1,))
t2 = threading.Thread(target=read_file, args=(f2,))
t1.start(); t2.start(); t1.join(); t2.join()
print("Multithreaded:", time.time() - t, "s")

"""Program to Compare Counting with and without Threads@AakashNinan IMCA Rollno:02"""
import threading, time

def count(n):
    while n: n -= 1

N = 50_000_000

t = time.time()
count(N)
print("Single-threaded:", time.time() - t, "s")

t = time.time()
a = threading.Thread(target=count, args=(N//2,))
b = threading.Thread(target=count, args=(N//2,))
a.start(); b.start(); a.join(); b.join()
print("Multi-threaded:", time.time() - t, "s")

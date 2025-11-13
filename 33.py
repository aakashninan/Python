"""Program to Temporarily Change Working Directory Using Context Manager@AakashNinan IMCA Rollno:02"""
import os

class ChangeDir:
    def __init__(self, path):
        self.path = path
        self.saved = None

    def __enter__(self):
        self.saved = os.getcwd()
        os.chdir(self.path)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.saved)


path = input("Enter directory path: ")
with ChangeDir(path):
    print("Inside block:", os.getcwd())

print("After block:", os.getcwd())

"""Program to Read File Using Context Manager@AakashNinan IMCA Rollno:02"""
class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

filename = input("Enter file name: ")
with FileManager(filename) as f:
    print(f.read())

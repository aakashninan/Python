"""Program to Implement a Singleton Printer Class@AakashNinan IMCA Rollno:02"""
class Printer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def print_document(self, text):
        print("Printing:", text)


p1 = Printer()
p2 = Printer()

p1.print_document("Report")
p2.print_document("Invoice")

print("Are both objects same?", p1 is p2)

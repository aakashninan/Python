"""Program to Design a Report System Using OOP@AakashNinan IMCA Rollno:02"""
class ReportData:
    def __init__(self):
        self.data = []

    def add_record(self, record):
        self.data.append(record)

    def get_data(self):
        return self.data


class ReportPrinter:
    def print_report(self, data):
        print("Report:")
        for d in data:
            print("-", d)


class ReportSystem:
    def __init__(self):
        self.storage = ReportData()
        self.printer = ReportPrinter()

    def add_record(self, record):
        self.storage.add_record(record)

    def generate_report(self):
        data = self.storage.get_data()
        self.printer.print_report(data)


system = ReportSystem()
system.add_record("Sales increased by 10%")
system.add_record("New customers: 50")
system.add_record("Expenses reduced by 5%")
system.generate_report()

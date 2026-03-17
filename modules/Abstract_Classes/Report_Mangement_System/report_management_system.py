from abc import ABC, abstractmethod

# Interface 1
class Printable(ABC):
    @abstractmethod
    def print_details(self):
        pass


# Interface 2
class Savable(ABC):
    @abstractmethod
    def save(self):
        pass


# Interface 3
class Exportable(ABC):
    @abstractmethod
    def export(self, format):
        pass


# Concrete class
class Report(Printable, Savable, Exportable):

    def __init__(self, title, content):
        self.title = title
        self.content = content

    def print_details(self):
        print(f"\nReport Title: {self.title}")
        print(f"Content: {self.content}")

    def save(self):
        print(f"Report '{self.title}' saved successfully")

    def export(self, format):
        print(f"Report '{self.title}' exported as {format}")


# Main Program
reports = []

n = int(input("Enter number of reports: "))

for i in range(n):
    print(f"\nEnter details for Report {i+1}")
    title = input("Enter title: ")
    content = input("Enter content: ")

    r = Report(title, content)
    reports.append(r)


# Processing all reports
for r in reports:
    r.print_details()
    r.save()
    r.export("PDF")
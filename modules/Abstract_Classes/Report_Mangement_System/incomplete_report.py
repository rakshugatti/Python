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


# Incomplete class (missing save method)
class IncompleteReport(Printable, Savable):

    def print_details(self):
        print("Only print implemented")


# Trying to create object
obj = IncompleteReport()
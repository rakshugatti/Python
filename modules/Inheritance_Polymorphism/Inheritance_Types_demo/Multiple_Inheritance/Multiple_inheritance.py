# Multiple Inheritance
# Person->Worker->Manager
class Person:

    def show_person(self):
        print("Person information")


class Worker:

    def show_worker(self):
        print("Worker information")


class Manager(Person, Worker):

    def manage(self):
        print("Manager manages the team")


m = Manager()

m.show_person()
m.show_worker()
m.manage()

# MRO demonstration
print("MRO of Manager:", Manager.mro())
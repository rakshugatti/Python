import csv

phone_book = {}

def add_contact():
    name = input("Enter name: ")
    number = input("Enter phone number: ")
    phone_book[name] = number
    print("Contact added successfully.")

def search_contact():
    name = input("Enter name to search: ")
    if name in phone_book:
        print("Phone Number:", phone_book[name])
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in phone_book:
        del phone_book[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter name to update: ")
    if name in phone_book:
        number = input("Enter new phone number: ")
        phone_book[name] = number
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def display_contacts():
    if not phone_book:
        print("Phone book is empty.")
    else:
        print("\nContacts (Sorted by Name)")
        for name in sorted(phone_book):
            print(name, ":", phone_book[name])

def export_to_csv():
    with open("contacts.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone Number"])
        for name, number in phone_book.items():
            writer.writerow([name, number])
    print("Contacts exported to contacts.csv")

while True:
    print("\n---- PHONE BOOK MENU ----")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Update Number")
    print("5. Display All Contacts")
    print("6. Export Contacts to CSV")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        export_to_csv()
    elif choice == "7":
        print("Exiting Phone Book...")
        break
    else:
        print("Invalid choice. Try again.")
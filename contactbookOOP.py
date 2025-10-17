
class Contact:
    def __init__(contact, name, number):
        contact.name = name
        contact.number = number
    
    def display(contact):
        print(f"{contact.name}: {contact.number}")

class ContactBook:
    def __init__(contact):
        contact.contacts = []

        try:
            with open("contactlist.txt", "r") as file:
                for line in file:
                    name, number = line.strip().split(", ")
                    contact.contacts.append(Contact(name, number))
        except FileNotFoundError:
            contact.contacts = []

    def add_cont(contact):
        new_contactname = input("Enter your contact name: ")
        new_contactnum = input("Enter your contact number: ")
        new_contact = Contact(new_contactname, new_contactnum)
        contact.contacts.append(new_contact)
        print(f"{new_contactname} has been added to your contact book.\n")

    def remove_cont(contact):
        print(contact)
        rem_action = input("Enter the contact name to be removed: ")
        for c in contact.contacts:
            if c.name == rem_action:
                contact.contacts.remove(c)
                print(f"{rem_action} has been removed from your contact book.\n")
                return
        print(f"{rem_action} not found in your contact book.\n")
    
    def search_cont(contact, name):
        for c in contact.contacts:
            if c.name == name:
                c.display()
                return
        print("Contact not found.\n")
    
    def view_cont(contact):
        print("\n--- Contact List ---")
        if not contact.contacts:
            print("No contacts available.")
        for ce in contact.contacts:
            ce.display()
        print("--------------------")

    def save_cont(contact):
        with open("contactlist.txt", "w") as file:
            for item in contact.contacts:
                file.write(f"{item.name}, {item.number}\n")


book = ContactBook()

print("WELCOME TO USUAL CONTACT BOOK V2!!!")
while True:
    print("1. Add Contact\n2. Remove Contact\n3. Search Contact\n4. View All\n5. Exit")
    action = int(input("Choose your options (1-5): "))

    if action == 1:
        book.add_cont()
    elif action == 2:
        book.remove_cont()
    elif action == 3:
        name_to_search = input("Enter the contact name to search: ")
        book.search_cont(name_to_search)
    elif action == 4:
        book.view_cont()
    elif action == 5:
        book.save_cont()
        print("Goodbye!!")
        break
    else:
        print("Invalid Response!")
        continue


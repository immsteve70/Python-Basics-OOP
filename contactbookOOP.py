
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
                    contact.contacts.append(line.strip())
        except FileNotFoundError:
            contact.contacts = []

    def add_cont(contact):
        new_contactname = input("Enter your contact name: ")
        new_contactnum = input("Enter your contact number: ")
        new_cont
        print(f"{new_contactname} has been added to your contact book.\n")

    def remove_cont(contact):
        print(contact.contacts)
        rem_action = input("Enter the contact name to be removed: ")
        contact.contacts.remove(rem_action)
        print(f"{rem_action} has been removed from your contact book.\n")
    
    def search_cont(contact, name):
        for contact in contact.contacts:
            if contact.name == name:
                contact.display()
                return
            print("Contact not found.\n")
    
    def view_cont(contact):
        print("\n--- Contact List ---")
        for contact in contact.contacts:
            contact.display
        print("--------------------")

    def save_cont():
        with open("contactlist.txt", "w") as file:
            for item in contact.contacts:
                file.write(item + "\n")


book = ContactBook()

print("WELCOME TO USUAL CONTACT BOOK V2!!!")
while True:
    print("Choose your options:\n1. Add Contact\n2. Remove Contact\n3. Search Contact\n4. View All\n5. Exit")
    action = int(input("= "))

    if action == 1:
        book.add_cont()
    elif action == 2:
        book.remove_cont()
    elif action == 3:
        book.search_cont()
    elif action == 4:
        book.view_cont()
    elif action == 5:
        print("Goodbye!!")
        break
    else:
        print("Invalid Response!")
        continue


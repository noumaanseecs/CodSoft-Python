'''
This is a contact book created as a part of my internship with CodSoft

The class Contact utilises the constructor to create the contact and the str method is used to print out the added contacts name,phone,email and address
'''

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Phone: {self.phone}\n"
                f"Email: {self.email}\n"
                f"Address: {self.address}\n")

'''
The ContactBook is the heart of this code and includes all the functions of this contactbook.
its functions have following functionalities:

1. The contructor will store the contacts to a dictionary self.contacts.
2. The add_contacts will add the created contact to the dictionary.
3. veiw_contact will display the list of contacts stored in the dictionary.
4. search_contact will locate a contact and display its info.
5. update_contact will locate the contact to be updates and will allow to change its attributes(or even a single attribute).
6. delete_contact will remove contact from our list.

'''

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        self.contacts[contact.name] = contact
        print(f"Contact '{contact.name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        for contact in self.contacts.values():
            print(contact)
            print("-" * 20)

    def search_contact(self, name):
        contact = self.contacts.get(name)
        if contact:
            print(contact)
        else:
            print(f"Contact '{name}' not found.")

    def update_contact(self, name, phone=None, email=None, address=None):
        contact = self.contacts.get(name)
        if contact:
            if phone:
                contact.phone = phone
            if email:
                contact.email = email
            if address:
                contact.address = address
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if self.contacts.pop(name, None):
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' not found.")

'''
The main function provides the user interface , it will allow user to do his/her desired manupilation.
The interface uses a simple if else conditional structure
'''

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            name = input("Enter contact name to search: ")
            contact_book.search_contact(name)

        elif choice == '4':
            name = input("Enter contact name to update: ")
            phone = input("Enter new phone number (leave blank to keep current): ")
            email = input("Enter new email address (leave blank to keep current): ")
            address = input("Enter new address (leave blank to keep current): ")
            contact_book.update_contact(name, phone or None, email or None, address or None)

        elif choice == '5':
            name = input("Enter contact name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()


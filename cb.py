class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("Contact list is empty.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. Name: {contact.name}, Phone: {contact.phone_number}")

    def search_contact(self, query):
        found_contacts = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone_number:
                found_contacts.append(contact)
        return found_contacts

    def update_contact(self, old_name, new_contact):
        for contact in self.contacts:
            if contact.name == old_name:
                contact.name = new_contact.name
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def display_menu():
    print("\nContact Management System Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    contact_book = ContactBook()
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.")
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            found_contacts = contact_book.search_contact(query)
            if found_contacts:
                print("Search Results:")
                for contact in found_contacts:
                    print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
            else:
                print("No matching contacts found.")
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name: ")
            phone_number = input("Enter new phone number: ")
            email = input("Enter new email: ")
            address = input("Enter new address: ")
            new_contact = Contact(new_name, phone_number, email, address)
            contact_book.update_contact(name, new_contact)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()

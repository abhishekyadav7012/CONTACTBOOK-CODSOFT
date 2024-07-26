class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, index, new_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = new_contact
            print(f"Contact {new_contact.name} updated successfully!")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            deleted_contact = self.contacts.pop(index)
            print(f"Contact {deleted_contact.name} deleted successfully!")
        else:
            print("Invalid contact index.")

def get_contact_details():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    return Contact(name, phone, email, address)

def main():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            contact = get_contact_details()
            contact_book.add_contact(contact)

        elif choice == '2':
            contact_book.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(query)
            if results:
                print("\nSearch Results:")
                for i, contact in enumerate(results, 1):
                    print(f"{i}. {contact.name} - {contact.phone}")
            else:
                print("No matching contacts found.")

        elif choice == '4':
            contact_book.view_contacts()
            index = int(input("Enter the number of the contact to update: ")) - 1
            new_contact = get_contact_details()
            contact_book.update_contact(index, new_contact)

        elif choice == '5':
            contact_book.view_contacts()
            index = int(input("Enter the number of the contact to delete: ")) - 1
            contact_book.delete_contact(index)

        elif choice == '6':
            print("Thank you for using the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
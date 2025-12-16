import csv
from tabulate import tabulate

FILE = "contact.csv"

def load_contacts():
    try:
        with open(FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        with open(FILE, mode='w', newline='') as file:
            fieldnames = ['name', 'phone']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
        return []

"""Save contacts to a CSV file."""
def save_contacts(contacts):
    with open(FILE, mode='w', newline='') as file:
        fieldnames = ['name', 'phone']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)
    print("\nContacts saved successfully.")


"""Add a new contact to the CSV file."""
def add_contact(name, phone):
    contacts = load_contacts()
    contacts.append({'name': name, 'phone': phone})
    save_contacts(contacts)
    print(f"Contact added successfully: Name: {name}, Phone: {phone}")


"""View all contacts from the CSV file."""
def view_contacts():
    contacts = load_contacts()

    if not contacts:
        print("No contacts found.")
        return

    # Prepare data for tabulate
    table = [[c['name'], c['phone']] for c in contacts]
    headers = ['Name', 'Phone']

    # Display the table
    print(tabulate(table, headers=headers, tablefmt='grid'))


"""Delete a contact by name from the CSV file."""
def delete_contact(name):
    contacts = load_contacts()

    updated_contacts = [c for c in contacts if c['name'] != name]
    if len(updated_contacts) == len(contacts):
        print(f"No contact found with name: {name}")
        return

    save_contacts(updated_contacts)
    print(f"Contact deleted successfully: Name: {name}")


"""Search for a contact by phone number."""
def search_contact():
    phone = input("Enter phone number to search: ")
    contacts = load_contacts()

    found_contacts = [c for c in contacts if c['phone'] == phone]
    if not found_contacts:
        print("Invalid contact. No contact found with the given phone number.")
    else:
        # Prepare data for tabulate
        table = [[c['name'], c['phone']] for c in found_contacts]
        headers = ['Name', 'Phone']

        # Display the table
        print(tabulate(table, headers=headers, tablefmt='grid'))

def main():
    while True:
        print("\n=*=*=*=*=*=*=*=*=*=")
        print("EZ Contact Manager")
        print("=*=*=*=*=*=*=*=*=*=\n")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            add_contact(name, phone)
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            name = input("Enter contact name to delete: ")
            delete_contact(name)
        elif choice == '4':
            search_contact()
        elif choice == '5':
            print("\nExiting... Thanks for using EZ Contact Manager\n")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

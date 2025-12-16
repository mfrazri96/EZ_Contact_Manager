

# EZ Contact Manager

#### Video Demo URL: (https://youtu.be/3wh6-gJxO_g)

#### Description

EZ Contact Manager is a simple command-line tool for managing a list of contacts. This tool allows users to seamlessly add, view, delete, and search for contacts, all stored in a CSV file. It serves as a practical example of file handling and user interaction in Python, providing a robust and user-friendly solution for managing contact information.


## Modules and Functions Used

### Module Imports

- **`csv`**:
  - The `csv` module is used for reading from and writing to CSV files. It allows for easy handling of CSV data with functionalities to read and write dictionaries where each row is a dictionary with column names as keys.

- **`tabulate`**:
  - The `tabulate` module is used for creating well-formatted tables in text output. It helps in displaying the contacts in a readable and organized table format, making it easier to view the data.

### Functions Used

- **`load_contacts()`**:
  - Loads contacts from the CSV file. If the file does not exist, it creates the file with headers (`name` and `phone`). It handles the `FileNotFoundError` exception to ensure the file is created if it is missing, then reads the contacts into a list of dictionaries.

- **`save_contacts(contacts)`**:
  - Saves the list of contacts to the CSV file. It writes the contacts to the file with headers and ensures that the data is up-to-date. This function also prints a confirmation message upon successful saving.

- **`add_contact(name, phone)`**:
  - Adds a new contact to the list and saves it to the CSV file. It first loads the existing contacts, appends the new contact, and then saves the updated list. It also prints a success message with the contact details.

- **`view_contacts()`**:
  - Displays all contacts in a tabular format using the `tabulate` module. If no contacts are found, it prints a message indicating that the contact list is empty.

- **`delete_contact(name)`**:
  - Deletes a contact by name from the CSV file. It updates the contact list by removing the specified contact and saves the changes. If no contact is found with the given name, it prints a message indicating this.

- **`search_contact()`**:
  - Searches for a contact by phone number. It prompts the user for a phone number and searches the contacts list for matches. If a contact is found, it displays it in a table; otherwise, it prints a message indicating no contact was found.

## Try and Except Error Handling

- **`FileNotFoundError`**:
  - In the `load_contacts()` function, a `try` block is used to attempt reading from the CSV file. If the file is not found, a `FileNotFoundError` is caught, and the file is created with the necessary headers. This ensures that the program can continue to function even if the file initially does not exist.

## Additional Information

- **Data Storage**:
  - Contacts are stored in a CSV file named `contact.csv`. This file is created in the specified path if it does not already exist.

- **User Interaction**:
  - The program operates in a loop, continuously displaying a menu until the user chooses to exit. It prompts the user for input and performs actions based on the selected option.

- **Future Enhancements**:
  - Future improvements could include adding error handling for invalid inputs, implementing contact updates, and enhancing the user interface.

Feel free to contribute to the project or open issues if you encounter any problems or have suggestions for improvements!

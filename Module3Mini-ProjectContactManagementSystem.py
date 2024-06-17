# Module 3: Mini-Project | Contact Management System
# Introduction
# Welcome to the Contact Management System project! In this project, you will apply your Python programming skills to create a functional command-line-based application that simplifies the management of your contacts. The Contact Management System will empower you to add, edit, delete, and search for contacts with ease, all while reinforcing your understanding of Python dictionaries, file handling, user interaction, and error handling.
# Project Requirements
# Your task is to develop a Contact Management System with the following features:

# 1. User Interface (UI):
# Create a user-friendly command-line interface (CLI) for the Contact Management System.
# Display a welcoming message and provide a menu with the following options:


# Welcome to use the Contact Management System
# Menu:
# Add a new contact
# Edit an existing contact
# Delete a contact
# Search for a contact
# Display all contacts
# Export contacts to a text file  
# Import contacts from a text file
# Quit 

# 2. Contact Data Storage:
# Use nested dictionaries as the main data structure for storing contact information.
# Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
# Store contact details within the inner dictionary, including:
# Name
# Phone number
# Email address
# Additional information (e.g., address, notes).

# 3. Menu Actions:
# Implement the following actions in response to menu selections:
# Adding a new contact with all relevant details.
# Editing an existing contact's information (name, phone number, email, etc.).
# Deleting a contact by searching for their unique identifier.
# Searching for a contact by their unique identifier and displaying their details.
# Displaying a list of all contacts with their unique identifiers.
# Exporting contacts to a text file in a structured format.
# Importing contacts from a text file and adding them to the system.

# 4. User Interaction:
# Utilize input() to enable users to select menu options and provide contact details.
# Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.

# 5. Error Handling:
# Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.

# 6. GitHub Repository:
# Create a GitHub repository for your project.
# Commit your code to the repository regularly.
# Create a clean and interactive README.md file in your GitHub repository.
# Include clear instructions on how to run the application and explanations of its features.
# Provide examples and screenshots, if possible, to enhance user understanding.
# Include a link to your GitHub repository in your project documentation.

# 7. Optional Bonus Points
# Contact Categories (Bonus): Implement the ability to categorize contacts into groups (e.g., friends, family, work). Each contact can belong to one or more categories.
# Contact Search (Bonus): Enhance the contact search functionality to allow users to search for contacts by name, phone number, email address, or additional information.
# Contact Sorting (Bonus): Implement sorting options to display contacts alphabetically by name or based on other criteria.
# Backup and Restore (Bonus): Add features to create automatic backups of contact data and the ability to restore data from a backup file.
# Custom Contact Fields (Bonus): Allow users to define custom fields for contacts (e.g., birthdays, anniversaries) and store this information.

# Project Submission
# Upon completion, submit your project, including all source code files and the README.md file in your GitHub repository, to your instructor or designated platform.
# Project Tips
# Begin by designing a simple, intuitive user interface that aligns with the provided menu options.
# Test your code iteratively as you implement each feature to identify and address any potential bugs or issues.
# Collaborate with fellow learners, seek assistance, and remember that learning is a collaborative effort.
# By successfully completing this project, you will not only enhance your Python programming skills but also have a practical Contact Management System to streamline your contact management tasks. Get ready to create a valuable tool for yourself and others!

# Module 3: Mini-Project | Contact Management System



#=======================================================

import re 
import os
contacts = {}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# Create the User Interface (UI):
def menu():
    clear()
    print('''
    Welcome to use the Contact Management System
          
    1. Add a new contact
    2. Edit an existing contact
    3. Delete a contact
    4. Search for a contact
    5. Display all contacts
    6. Export contacts to a text file  
    7. Import contacts from a text file
    8. Quit 
          ''')


def validate_name(name):
    return re.match(r'[A-Za-z]+([A-Za-z]|\s|\d)+$', name) is not None

def validate_phone(phone_number):
    return re.match(r'^(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}$', phone_number) is not None


def validate_email(email):
    return re.match(r'[\w.-]+@[\w-]+\.[a-z]{2,3}', email) is not None


def add_contacts():
    while True:
        print("\nEnter a new contact (or enter 'done' to finish):")
        name = input("Name: ")
        if name.lower() == 'done':
            break
        while not validate_name(name):
            print("Invalid name format. Please enter a valid name.")
            name = input("Name: ")

        phone_number = input("Phone number: ")
        while not validate_phone(phone_number):
            print("Invalid phone number. Please enter a valid phone number.")
            phone_number = input("Phone number: ")

        email = input("Email: ")
        while not validate_email(email):           
            print("Invalid email address. Please enter a valid email address.")
            email = input("Email: ")
        for key, value in contacts.items():
            if value['email'] == email:
                input("This email already exists. Press enter to continue...")
                return
        address = input("Address (optional): ")
        
        contacts[email] = {
            'name': name,
            'phone_number': phone_number,
            'email': email,
            'address': address if address else None
        }
    print("Add contact successful...")
    export_contacts()


def update_contact():
        email = input("Enter the email of the contact to edit: ")
        if email in contacts:
            print("\nEnter new details (or press Enter to keep current value):")
            name = input(f"Name ({contacts[email]['name']}): ")
            phone_number = input(f"Phone Number ({contacts[email]['phone_number']}): ")
            new_email = input(f"Email ({email}): ")
            address = input(f"Address ({contacts[email]['address']}): ")

            if name:
                if validate_name(name):
                    contacts[email]['name'] = name
                else:
                    print("Invalid name. Name not updated.")
            if phone_number:
                if validate_phone(phone_number):
                    contacts[email]['phone_number'] = phone_number
                else:
                    print("Invalid phone number. Phone number not updated.")
            if address:
                contacts[email]['address'] = address

            if new_email and new_email != email:
                if validate_email(new_email):
                    contacts[new_email] = contacts.pop(email)
                    contacts[new_email]['email'] = new_email
                    print("Email updated successfully.")
                else:
                    print("Invalid email address. Email not updated.")
            else:
                input("Contact updated successfully. Press enter to continue")
                export_contacts()
        else:
            input("Contact not found. Press Enter to back to main menu")
        
def delete_contact():
    email = input("Enter the email of the contact to delete: ")
    while not validate_email(email):
        print("Invalid email address. Please enter a valid email address.")
        email = input("Enter the email of the contact to delete: ")

    if email in contacts:
        del contacts[email]
        print(f"Contact {email} deleted successfully.")
        export_contacts()
    else:
        print("Contact not found.")

def search_contact():
    email = input("Enter the email of the contact to search for: ")

    if email in contacts:
        print(f"Name: {contacts[email]['name']}")
        print(f"Phone number: {contacts[email]['phone_number']}")
        print(f"Email: {contacts[email]['email']}")
        print(f"Address: {contacts[email]['address']}")
        input("Press Enter to back to main menu...")
    else:
        input("Contact not found. Press Enter key to main menu")

def display_all_contacts():
    if contacts:
        for email, info in contacts.items():
            print(f"Name: {info['name']}")
            print(f"Phone number: {info['phone_number']}")
            print(f"Email: {email}")
            print(f"Address: {info['address']}")
            print()
        input("Click Enter key to back to main menu... ")
    else:
        input("No contacts available.")

def export_contacts():
    with open("contacts.txt", "w") as file:
        for email, info in contacts.items():
            file.write(f"{info['name']}-:-{info['phone_number']}-:-{email}-:-{info['address']}\n")
    input("Press Enter to continue...")

def import_contacts():
    global contacts
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone_number, email, address = line.strip().split('-:-')
                contacts[email] = {
                    'name': name,
                    'phone_number': phone_number,
                    'email': email,
                    'address': address if address != 'None' else None
                }
        input("Contacts imported from contacts.txt OK. Press enter to continue...")
    except FileNotFoundError:
        print("contacts.txt file not found.")
        input("Click Enter key to back to main menu... ")

def import_contacts_main():
    global contacts
    try:
        with open("contacts.txt", "r") as file:
            for line in file:
                name, phone_number, email, address = line.strip().split('-:-')
                contacts[email] = {
                    'name': name,
                    'phone_number': phone_number,
                    'email': email,
                    'address': address if address != 'None' else None
                }
        # input("Contacts imported from contacts.txt. Press enter to continue...")
    except FileNotFoundError:
        print("contacts.txt file not found.")
        input("Click Enter key to back to main menu... ")
def main():
    global contacts
    if os.path.exists("contacts.txt"):
        import_contacts_main()

    while True:
        menu()
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contacts()
        elif choice == "2":
            update_contact()
        elif choice == "3":
            delete_contact()
        elif choice == "4":
            search_contact()
        elif choice == "5":
            display_all_contacts()
        elif choice == "6":
            if contacts:
                export_contacts()
            else:
                print("No contacts to export.")
                input("Click Enter key back to main menu... ")
        elif choice == "7":
            import_contacts()
        elif choice == "8":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



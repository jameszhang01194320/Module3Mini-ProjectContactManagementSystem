# Module3Mini-ProjectContactManagementSystem
This project is a comprehensive use the knowage of the last 3 weeks.
we use file handling, regex, dictionary,tuple list 

Steps:

1. Create the main() method as the entry of the project, and create the interface menu according to the requirements of the project.
The menu includes
# Add new contact
# Edit existing contact
# Delete contact
# Search contacts
# Show all contacts
# Export contacts to text file  
# Import contacts from text file
# Exit 

2. Create a method to add a new contact, the contact consists of
# Name
# Phone number
# Email address
# Other information (e.g., address, notes).
Use regex to check input bytes
Since emails are IDs, if the email entered already exists in the contact dictionary, the user will be alerted to use another email.

3. Add update to existing contact's information (name, phone number, email, etc.).
Since we are using email as the ID, the ID is an external key and can't be changed but can be deleted, in order to update the email we have to copy the old email to the new one, with a different key, change the internal email and then delete the old email.

4. Delete a contact by searching the contact's unique identifier email.

5. searches for a contact by its unique identifier email and displays its details.

6. displays a list of all contacts and their unique identifiers.

7. exports contacts to a text file in a structured format.

8. imports contacts from a text file and adds them to the system.


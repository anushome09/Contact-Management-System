# Testing the crud function
from utils.crud import add_contact, get_contacts, update_contact, delete_contact

# Add Contacts 
add_contact(name="John Doe", phone="1234567890", email="john@example.com", category="Friend")
add_contact(name="Jane Doe", phone="9876543210", email="jane@example.com", category="Work")

# Get Contacts
contacts = get_contacts()
for contact in contacts:
    print(contact["id"], contact["name"], contact["phone"], contact["email"], contact["category"])


# Update a contact
update_contact(1, name="John Smith", category="Family")


# Delete a contact
delete_contact(2)
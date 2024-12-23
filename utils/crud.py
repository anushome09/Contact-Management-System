import pyodbc
from database.setup import  connection

# Add a new contact
def add_contact(name, phone, email=None, category='Uncategorized'):
    query = """
               INSERT INTO Contact (name, phone, email, category)
               VALUES (?, ?, ?, ?)
            """
    
    try: 
        # Prepare the values to be insert
        values = (name, phone, email, category)
        
        # Execute the query
        with connection.cursor as cursor:
            cursor.execute(query, values)
            connection.commit()
            
        print("Contact added successfully!")
    
    except pyodbc.Error as error:
        print("Error adding contact: ", error)
    
# Get all contact
def get_contacts():
    query = "SELECT * FROM Contact"
    
    try:
        # Execute the query
        with connection.cursor as cursor:
            cursor.excute(query)
            contacts = cursor.fetchall()
            
        # Convert the result into list of dictionary
        contact_list = []
        for row in contacts:
            contact_dict = {
                'id': row[0],
                'name': row[1],
                'phone': row[2],
                'email': row[3],
                'category': row[4]
            }
            contact_list.append(contact_dict)
        
        return contact_list
    
    except pyodbc.Error as error:
        print("Error fetching contacts: ", error)
        return []
            

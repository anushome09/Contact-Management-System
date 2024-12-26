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
        with connection.cursor() as cursor:
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
        with connection.cursor() as cursor:
            cursor.execute(query)
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
            
# Update a contact
def update_contact(contact_id, **kwargs):
    if not kwargs:
        print("No updates provided.")
        return
    set_clause = ", ".join([f"{key} = ?" for key in kwargs.keys()])
    values = list(kwargs.values())
    
    values.append(contact_id)
    
    sql_query = f"""
        UPDATE Contact
        SET {set_clause}
        WHERE id = ?;
    """
    
    try: 
        with connection.cursor() as cursor:
            cursor.execute(sql_query, values)
            connection.commit()
        print("Contact updated successfully!")
    except pyodbc.Error as error:
        print("Error updating contact: ", error)

# Delete a contact
def delete_contact(contact_id):
    sql_query = """
        DELETE FROM Contact
        WHERE id = ?;
    """
    
    try:
        # Execute the query
        with connection.cursor() as cursor:
            cursor.execute(sql_query, (contact_id))
            connection.commit()
        print("Contact deleted Successfully!")
    except pyodbc.Error as error:
        print("Error deleting contact: ", error)
        
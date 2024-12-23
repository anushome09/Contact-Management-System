import pyodbc

'''
# List all the available driver
drivers = pyodbc.drivers()
print("Available ODBC Drivers: ")
for driver in drivers:
    print(drivers)
'''
# Connection string
connection = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=(localdb)\\MSSQLLocalDB;"
    "Database=ContactManagement;"
    "Trusted_Connection=yes;"
)

# cursor = connection.cursor()

'''
# Test the connection
cursor.execute("SELECT 1")
print("Connection")
'''

'''
# Inserting values into the database
cursor.execute("""
               INSERT INTO Contact (name, phone, email, category)
               VALUES (?, ?, ?, ?)
               """, ("John Doe", "1234567890", "john@example.com", "Friend")) 
connection.commit()

# Fetching the data
cursor.execute("SELECT * FROM Contact")
for row in cursor.fetchall():
    print(row)
'''

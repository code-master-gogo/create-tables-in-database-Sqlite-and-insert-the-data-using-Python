import sqlite3

connection= sqlite3.connect('sqlite.db') 

cursor = connection.cursor()

sql ='''CREATE TABLE if not Exists Employee_data(
   Employee CHAR(20),
   Department CHAR(20),
   Project CHAR(20)
)'''

cursor.execute(sql)
print("Table created successfully........")

emp = 'Anubhav'
dept = 'Engineering'
proj = 'Automation'

INSERT_QUERY = f"INSERT INTO Employee_data VALUES ('{emp}','{dept}','{proj}')"

cursor.execute(INSERT_QUERY)

for row in cursor.execute('SELECT * FROM Employee_data'):
    print(row)

connection.commit()

connection.close()
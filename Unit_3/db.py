import sqlite3

db = sqlite3.connect('example.db')

cursor = db.cursor()

# cursor.execute("""CREATE TABLE Persons (
#                 PersonID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL ,
#                 name varchar (255),
#                 Adress varchar (255),
#                 'Group' int)
#             """)

# data record
# cursor.execute("INSERT INTO Persons VALUES(1, 'Oleg' ,'Pushkina-1' ,3) ")

# some data record
# cursor.execute("INSERT INTO Persons VALUES(2, 'Oleg' ,'Pushkina-1' ,3),(3, 'Alexei' ,'Kopishe-124' ,3) ")

# write information from table
cursor.execute("SELECT * FROM Persons")
print(cursor.fetchall())

# update information from table
cursor.execute("UPDATE Persons SET Adress='Brest' WHERE PersonID=3")







db.commit()

db.close()

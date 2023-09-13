import sqlite3


# db = sqlite3.connect('example.db')
#
# cursor = db.cursor()


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
# cursor.execute("SELECT * FROM Persons")
# print(cursor.fetchall())
# 
# # update information from table
# cursor.execute("UPDATE Persons SET Adress='Brest' WHERE PersonID=3")

def record(Person: int, name: str, adress: str, group: int):
    db = sqlite3.connect('example.db')
    cursor = db.cursor()
    data = (Person, name, adress, group)
    cursor.execute("INSERT INTO Persons(PersonID, name, Adress, 'Group') VALUES(?, ?, ?, ?);", data)
    db.commit()
    db.close()

def record_(name: str, adress: str, group: int):
    db = sqlite3.connect('example.db')
    cursor = db.cursor()
    data = (name, adress, group)
    cursor.execute("INSERT INTO Persons(name, Adress, 'Group') VALUES(?, ?, ?);", data)
    db.commit()
    db.close()


def delete(name: str):
    db = sqlite3.connect('example.db')
    cursor = db.cursor()
    cursor.execute("""DELETE from Persons where name = ?""", (name,))
    db.commit()
    db.close()

def search(name: str):
    db = sqlite3.connect('example.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Persons where name == ?", (name,))
    result = cursor.fetchone()
    db.commit()
    db.close()
    return (result)

# record(4, 'Irena', 'city',3)
# record_('Irena', 'city',3)
# delete('Irena')
# print(search('Alexei'))
#
# db.commit()
#
# db.close()

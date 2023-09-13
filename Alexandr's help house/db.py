import sqlite3
import datetime

def record(name: str, characteristics: str, amount: int, item_size=5):
    db = sqlite3.connect('donation.db')
    cursor = db.cursor()
    time = datetime.datetime.now()
    data = (name, characteristics, item_size, amount, time)
    cursor.execute("INSERT INTO Donation(name, characteristics, item_size, amount, date) VALUES(?, ?, ?, ?, ?);", data)
    db.commit()
    db.close()

def delete(name: str):
    db = sqlite3.connect('donation.db')
    cursor = db.cursor()
    cursor.execute("""DELETE from Donation where name = ?""", (name,))
    db.commit()
    db.close()

def search(name: str):
    db = sqlite3.connect('donation.db')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Donation where name == ?", (name,))
    result = cursor.fetchone()
    db.commit()
    db.close()
    return result
# record(4, 'Irena', 'city',3)
# record_('Irena', 'city',3)
# delete('Irena')
# print(search('Alexei'))
#
# db.commit()
#
# db.close()

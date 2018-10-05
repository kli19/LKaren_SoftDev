import sqlite3

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) 
c = db.cursor()

command = "SELECT peeps.id FROM peeps;"

c.execute(command)

id_list = c.fetchall()

for row in id_list:
    
    

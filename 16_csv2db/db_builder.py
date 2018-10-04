#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="database.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

command = "CREATE TABLE courses (code TEXT, mark INT, id INT)"          #build SQL stmt, save as string
c.execute(command)    #run SQL statement

with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['code'], row['mark'], row['id'])
        code = row['code']
        mark = row['mark']
        course_id = row['id']
        command = 'INSERT INTO courses VALUES ('
        command += '"' + code + '", '
        command += mark + ', '
        command += course_id + ')'
        #build SQL stmt, save as string
        c.execute(command)    #run SQL statement

command = "CREATE TABLE peeps (name TEXT, age INT, id INT)"          #build SQL stmt, save as string
c.execute(command)    #run SQL statement
with open('peeps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['age'], row['id'])
        name = row['name']
        age = row['age']
        peep_id = row['id']
        command = 'INSERT INTO courses VALUES ('
        command += '"' + name + '", '
        command += age + ', '
        command += peep_id + ')'
        #build SQL stmt, save as string
        c.execute(command)    #run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database

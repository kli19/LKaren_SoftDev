# trackStars -- Alex Liu, William Lu
# SoftDev1 pd7
# K16 -- No Trouble
# 2018-10-05 F

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

def csvToDB(fileName, types):
    DB_FILE="discobandit.db"

    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops

    #==========================================================
    #INSERT YOUR POPULATE CODE IN THIS ZONE

    file = open("raw/" + fileName, "rU")
    reader = csv.DictReader(file)

    #for row in reader:
    #    print(row['code'], row['mark'], row['id'])

    tableName = fileName[: fileName.find('.')]

    command = 'CREATE TABLE ' + tableName + ' ('
    i = 0
    for col in reader.fieldnames:
        # print(col)
        command += col + ' ' + types[i] + ', '#build SQL stmt, save as string
        i += 1

    command = command[: command.rfind(',')]
    command += ');'

    #print(command)

    c.execute(command)    #run SQL statement

    for row in reader:
        # print(row)
        command = 'INSERT INTO ' + tableName + ' VALUES ('
        i = 0

        for col in row:
            if types[i] == 'TEXT':
                command += '"' + row[col] + '", '
            else:
                command += row[col] + ', '
        command = command[: command.rfind(',')]
        command += ');'
        #print(command)
        c.execute(command)
        i += 1

    db.commit() #save changes

    db.close()  #close database

csvToDB("courses.csv", ['TEXT', 'INTEGER', 'INTEGER'])
#csvToDB("occupations.csv", ['TEXT', 'REAL'])
csvToDB("peeps.csv", ['TEXT', 'INTEGER', 'INTEGER'])

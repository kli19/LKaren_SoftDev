# Liliu and Stitch -- Alex Liu, Karen Li
# SoftDev1 pd7
# K17 -- AVERAGE
# 2018-10-05 F

import sqlite3

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE)
c = db.cursor()

avg_list = []
id_list = []
#avg of current student
avg = 0
#global variable for number of courses and sum
cor = 0
sum = 0

def avg_find(x):
    grades = "SELECT courses.mark FROM courses WHERE " + str(x) + "= courses.id;"
    c.execute(grades)

    #gets all the courses for the durrent "x" id
    mark_list = c.fetchall()
    #makes a list of avgs for each student
    markTuples = ()
    for row in mark_list:
        markTuples += row
        #print (row)

        #adds the tuples in the list for each student
    global cor
    global sum
    sum = 0
    cor = 0
    for num in markTuples:
        sum += num
        cor += 1
        #print (sum)
    return (sum / cor)

#looks for each course based on id
for x in range(1,11):

    avg = avg_find(x)

    #finds name of student with specfic id
    students = "SELECT peeps.name FROM peeps WHERE " + str(x) + "= peeps.id;"
    c.execute(students)

    student = c.fetchall()

    ids = "SELECT peeps.id FROM peeps WHERE " + str(x) + "= peeps.id;"
    c.execute(ids)

    id = c.fetchall()

    #prints sum of grades
    print (str(student[0][0]) + " with id " + str(id[0][0]) + " total : " + str(sum) )\
    #prints num of courses
    print (str(student[0][0]) + " with id " + str(id[0][0]) + " total : " + str(cor) )


    #prints avg
    print (str(student[0][0]) + " with id " + str(id[0][0]) + " avg : " + str(avg) + "\n" )
    avg_list.append(avg)
    id_list.append(id[0][0])

# ==============================Creating New Table==============================

command = "CREATE TABLE peeps_avg ( ID INTEGER, AVERAGE FLOAT )"
c.execute(command)

for x in range(0,10):
    command = "INSERT INTO peeps_avg VALUES (?,?)"
    #print(command)
    c.execute(command, (str(id_list[x]), str(avg_list[x])))

# ==============================Creating New Row==============================

def row_Add(code, mark, id):
    command = "INSERT INTO courses VALUES " + "(" + '"' + code + '"' + ", " + str(mark) + ", " + str(id) + ");"
    c.execute(command)
    #command = "INSERT INTO courses VALUES (?,?,?);"
    #c.execute(command, code, str(mark), str(id))

row_Add("hello" ,78, 1000)

#==============================Creating Update==============================

def updating(id, new):
    #gets old average
    old = avg_find(id);

    #adds new average to old average
    command = "UPDATE peeps_avg SET AVERAGE = " + str((sum + new) / (cor + 1)) + " " + "WHERE ID = " + str(id) + ";"
    print(command)
    c.execute(command)

#updating(9, 57)

db.commit() #save changes

db.close()  #close database

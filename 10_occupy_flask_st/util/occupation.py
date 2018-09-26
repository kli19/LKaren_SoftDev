# OccupationalHazard: Karen Li, Ahnaf Hasan
# SoftDev1 pd07
# K #10: Jinja Tuning 
# 2018 - 09 - 24

import csv, random



weightedOccupationList = []

occupationDic = {}



def fillList():

    #reads csv file

    csvFileObject = open( './data/occupations.csv', 'r')

    dictionaryReader = csv.DictReader( csvFileObject)

    

    #looks at each row except for the last

    for row in dictionaryReader:

        if (row['Job Class'] != 'Total'):

			# fills occupationDic with job keys linked with percentage values

            occupationDic[row['Job Class']] = row['Percentage']
			
			#fills occupationList with occupations with frequency dependent on percentage

            i = 0

            while i < (float(row['Percentage'])*10):

                weightedOccupationList.append(row['Job Class'])

                i+=1



#returns a randomly selected occupation from the weighted occupationList

fillList();

def randomOccupation():

    return random.choice(weightedOccupationList)




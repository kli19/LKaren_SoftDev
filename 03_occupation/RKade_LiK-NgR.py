# RKade: Karen Li, Rachel Ng
# SoftDev1 pd06
# K #06: StI/O: Divine your Destiny!
# 2018 - 09 - 13

import csv, random

occupationList = []

def fillList():
	csvFileObject = open( 'occupations.csv', 'rb')
	dictionaryReader = csv.DictReader( csvFileObject)
	for row in dictionaryReader:
		if (row['Job Class'] != 'Total'):
			i = 0
			while i < (float(row['Percentage'])*10):
				occupationList.append(row['Job Class'])
				i+=1

def randomOccupation():
	return random.choice(occupationList)
				
fillList()
print(randomOccupation())

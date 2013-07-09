import csv;

dataFile = csv.reader(open('cities.txt','r'),delimiter = ',');
fileToWrite = csv.writer(open('sortedCities.txt','w+'),delimiter = ',');


cityArray = []

def sort_by_city(inner):
	return inner[1];

for row in dataFile:
	cityArray.append(row)


cityArray.sort(key=sort_by_city)

for row in cityArray:
	fileToWrite.writerow(row)
	print row




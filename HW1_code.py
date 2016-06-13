import csv # needed for csv file
import urllib.request
import io

tup1=();
url1="https://raw.githubusercontent.com/cnwneal/Hw1-Digging-into-Data-/master/Grocery_Stores_-_2013.csv"
url2="https://raw.githubusercontent.com/cnwneal/Hw1-Digging-into-Data-/master/Affordable_Rental_Housing_Developments.csv"
url3="https://raw.githubusercontent.com/cnwneal/Hw1-Digging-into-Data-/master/Problem_Landlord_List.csv"
url4="https://raw.githubusercontent.com/cnwneal/Hw1-Digging-into-Data-/master/Public_Health_Statistics-_Selected_underlying_causes_of_death_in_Chicago__2006___2010.csv"

response1 = urllib.request.urlopen(url1)
response2 = urllib.request.urlopen(url2)
response3 = urllib.request.urlopen(url3)
response4 = urllib.request.urlopen(url4)

datareader = csv.reader(io.TextIOWrapper(response1))#.read().decode('utf-8'))
for row in datareader:
       tup1+ row
       print(tup1)
       print("    ")
datareader2 = csv.reader(io.TextIOWrapper(response2))#.read().decode('utf-8'))
for row in datareader2:
	print(row)
	print("    ")
datareader3 = csv.reader(io.TextIOWrapper(response3))#.read().decode('utf-8'))
for row in datareader3:
	print(row)
	print("   ")
datareader4 = csv.reader(io.TextIOWrapper(response4))#.read().decode('utf-8'))
for row in datareader4:
	print(row)
	print("    ")






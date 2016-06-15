import csv # needed for csv file
import urllib.request
import io

list=[];
list1=[0]*100;
counter=0;
i = 0;
list2=[100]
list3=[100]
#list4=[100]

url1="https://raw.githubusercontent.com/cnwneal/Hw1-Digging-into-Data-/master/Grocery_Stores_-_2013.csv"
url2="https://raw.githubusercontent.com/cnwneal/Hw1-Digging-into-Data-/master/Affordable_Rental_Housing_Developments.csv"
url3="https://raw.githubusercontent.com/cnwneal/Hw1-Digging-into-Data-/master/Problem_Landlord_List.csv"
#url4="https://raw.githubusercontent.com/cnwneal/Hw1-Digging-into-Data-/master/Public_Health_Statistics-_Selected_underlying_causes_of_death_in_Chicago__2006___2010.csv"

response1 = urllib.request.urlopen(url1)
response2 = urllib.request.urlopen(url2)
response3 = urllib.request.urlopen(url3)
#response4 = urllib.request.urlopen(url4)

datareader = csv.reader(io.TextIOWrapper(response1))#.read().decode('utf-8'))
print ("This is the number of liquor stores per neighborhood ")
print("                                     ")
for row in datareader:
       if ("Liquor" in row[0] or "LIQUOR" in row[0] or "liquor" in row[0]):
              list.append(row[7] and row [8])
              for i in row[8]:
                     counter=counter+1
                     list1[int(row[8])]= list1[int(row[8])]+1
#print(list1[38])
#while  i< len(list1):
       #if list1[i]>0:
             #print(list1[i])
       #i=i+1
print(list)
print("There were a total of: ", counter,  " liquor stores in Cook County neighborhoods in 2013")
print("                                     ")             
datareader2 = csv.reader(io.TextIOWrapper(response2))#.read().decode('utf-8'))
print("Affordable housing and the number of self described liqoure stores in the neighborhood where it is located based on 2013 data ")
print("                                     ")
for row in datareader2:
       if ( row[1]=='' or row[1]=="Community Area Number"):
              continue 
       elif (int (row[1])>=1 or int (row[1])==0):
              list2.append((row[3], list1[int(row[1])]))
              print(row[3], list1[int(row[1])])
print("                                     ")              
datareader3 = csv.reader(io.TextIOWrapper(response3))#.read().decode('utf-8'))
print("Problem landlords and the number of self described liqoure stores in the neighborhood they are is located based on 2013 data ")
print("                                     ")
for row in datareader3:
       if( row[4]=='' or row[4]=="COMMUNITY AREA NUMBER"):
              continue
       elif (int (row[4])>=1 or int (row[4])==0):
              list3.append((row[2], row[3], list1[int(row[4])]))
              print(row[2], row[3], list1[int(row[4])])



#print(list2, end=' ')	





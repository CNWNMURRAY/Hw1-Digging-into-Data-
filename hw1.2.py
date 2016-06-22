import csv # needed for csv file
import urllib.request
import io
import unittest

list=[];
list_all=[];
list1=[0]*100;
list5=[0]*100;
counter=0;
counter_two=0;
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
print("                                     ")
for row in datareader:
       if ("Liquor" in row[0] or "LIQUOR" in row[0] or "liquor" in row[0]): #row 0 is the name of the store
              list.append(row [8])#row 8 is the community number
              #for i in row[8]: 
              counter=counter+1
              list1[int(row[8])]= list1[int(row[8])]+1
# grabs all stores
       if( row[7]=="COMMUNITY AREA NAME"):
              continue
       list_all.append(row[7]and row [8])
       #for i in row[8]:
       counter_two=counter_two+1
       list5[int(row[8])]= list5[int(row[8])]+1
#print(list1[38])
#while  i< len(list1):
       #if list1[i]>0:
             #print(list1[i])
       #i=i+1
#while i<100:
      # print(list1[i])
       #i=i+1
#i=0;
#while i<100:
      # print(list5[i])
      # i=i+1
#i=0;
print(" The number of liquors stores in Community Area per store in the Community Area")
print ("Rogers Park", list1[1],"Englewood",list1[39])
print("Rogers Park", list5[1], "Englewood",list5[39])
print ("                                                ")
Avg1=(counter/counter_two)*100
print("Shows the total percentage of liquor stores compared to non liquor stores and the percent of liquor stores per community area ",  Avg1)

i=0;
while i<80:
       if list5[i]>0:
              addin=list1[i];
              addin_two=list5[i];
              Avg2=(addin/addin_two)*100
              print(Avg2)
       i=i+1
i=0;

print(list)
print("There were a total of: ", counter,  " liquor stores in Cook County neighborhoods in 2013")
print(list_all)
print("There were a total of: ", counter_two,  "stores in Cook County neighborhoods in 2013")
print("                                     ")
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



class TestData(unittest.TestCase):

    def test_first_average(self):
        self.assertEqual(list1[1], 13)

    def test_average(self):
        self.assertTrue(list5[39],4)
       

 




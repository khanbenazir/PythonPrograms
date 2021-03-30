# Reading a csv file from system, adding it to a list with each row as a tuple
# and doing some calculations on it

import csv

myList = []
total = 0
f = open("C:/Users/benuk/Desktop/blocks.txt", "r")        #reading the .txt file
reader = csv.reader(f)
next(reader)    # to skip the first line containing field name
for row in reader:
    tup1 = tuple(row)
    total = float(tup1[1])*float(tup1[2])    # we have to convert the values from str to float
    myList.append(tup1)

print(myList,'/n')
print(total)

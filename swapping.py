# sorting without using in-built function
myList = [8, 10, 4, 6, 2]
swap = True
while swap:
    swap = False
    for i in range(len(myList)-1):
        if myList[i] > myList[i+1]:
            swap = True
            myList[i], myList[i+1] = myList[i+1], myList[i]
print("Sorted List: ", myList)

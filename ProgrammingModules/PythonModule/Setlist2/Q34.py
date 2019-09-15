list1 = [1,4,5,6,8,21,57,97]
list2 = [5,65,34,12,87,89,5,9]
list3 = [4,2,6,8,6,5,44,32]

maxList = []
minList = []
def createMaxMinList():
    list1.sort()
    list2.sort()
    list3.sort()
    maxList.extend(list1[len(list1)-(len(list1)+2):])
    maxList.extend(list2[len(list2)-(len(list2)+2):])
    maxList.extend(list3[len(list3)-(len(list3)+2):])

    minList.extend(list1[0:2])
    minList.extend(list2[0:2])
    minList.extend(list3[0:2])

createMaxMinList()
print("MAX LIST:")
x = 0
for val in maxList:
    x += val
    print(val)
x /= len(maxList)
print("The average value of the max list is: " + str(x)+"\n")

print("MIN LIST:")
y = 0
for val in minList:
    y += val
    print(val)
y /= len(minList)
print("The average value of the minList is: " + str(y))
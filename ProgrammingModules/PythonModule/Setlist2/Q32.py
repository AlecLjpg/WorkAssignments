list1 = ['Boston', 'New York', 'Burlington', 'Hartford', 'Albany']
list2 = ['Atlanta', 'Charlotte', 'Birmingham','Nashville', 'Charleston']
list3 = ['Dallas', 'Houston','El Paso','Arlington','Fort Worth']

def printCityLength(x):
    for val in x:
        print("City:" + val + "\t Length:" + str(len(val)))
print("List 1")
printCityLength(list1)
print("\nList 2")
printCityLength(list2)
print("\nList 3")
printCityLength(list3)

def maxMin(x):
    y = sorted(x,key=len)
    print("Max: " + y[-1])
    print("Min: " + y[0])

print("\nList1")
maxMin(list1)
print("\nList2")
maxMin(list2)
print("\nList3")
maxMin(list3)

def listCompare():
    x = sorted(list1,key=len)
    y = sorted(list2,key=len)
    z = sorted(list3,key=len)
   
    if x[-1] > y[-1]and [x-1] > z[-1]:
        print("The max of all three lists is: " + x[-1])
    elif y[-1] > x[-1] and y[-1] > z[-1]:
        print("The max of all three lists is: " + y[-1])
    elif z[-1] > x[-1] and z[-1] > y[-1]:
        print("The max of all three lists is: " + z[-1])
    if x[0] < y[0] and x[0] < z[0]:
        print("The min of all three lists is: " + x[0])
    elif y[0] < x[0] and y[0] < z[0]:
        print("The min of all three lists is: " + y[0])
    elif z[0] < x[0] and z[0] < y[0]:
        print("The min of all three lists is: " + z[0])

listCompare()

def deleteFirstLast(x):
    x.pop(0)
    x.pop(-1)

    for val in x:
        print(val)
print("List 1, first and last elements removed:")
deleteFirstLast(list1)
print("List 2, first and last elements removed:")
deleteFirstLast(list2)
print("List 3, first and last elements removed:")
deleteFirstLast(list3)
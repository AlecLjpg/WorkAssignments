list1 = ['Boston', 'New York', 'Burlington', 'Hartford', 'Albany']
newList = list1

def alterList(x):
    x.append("Detroit")
    x.insert(4,"Indianapolis")
    x = sorted(x, key=len)
    print("Sorted list:")
    for val in x:
        print(val)
    x = x[:len(x)-3]
    print("List with last three elements deleted:")
    for val in x:
        print(val)
alterList(newList)
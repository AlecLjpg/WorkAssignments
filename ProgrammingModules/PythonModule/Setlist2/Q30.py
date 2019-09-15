y = int(input("Enter the number of integers you will enter: "))
x = []
def enterNumber(y):
    for i in range(y):
       z =  int(input("Enter a number: "))
       x.append(z)

enterNumber(y)
placeholder = 0
def sort(x):
    for val in x:
        for i in range(len(x)-1):
            if x[i] > x[i+1]:
                continue
            elif x[i]<x[i+1]:
                placeholder = x[i+1]
                x[i+1] = x[i]
                x[i] = placeholder
sort(x)
print("Sorted list: " + str(x))
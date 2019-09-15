x = [1,7,3,4]
y = [20,5,1,10]
largest = 0

for i in range(len(x)):
    if x[i] > largest:
        largest = x[i]
print("Largest number: " + str(largest)) 

x.extend(y)

for z in range(len(x)):
    if x[z] > largest:
        largest = x[z]
print("Largest number (after extension) : " + str(largest))

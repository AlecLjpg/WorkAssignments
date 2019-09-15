low = []
av = []
high = []


x = [int(y) for y in input("Enter 10 numbers to be processed: ").split()]

avg = (sum(x)/len(x))
print("The average of all numbers entered is: " + str(avg))

for y in x:
    if y > avg: high.append(y)
    elif y == avg: av.append(y)
    elif y < avg: low.append(y)

print(str(len(high)) + " numbers are above the average.")
print(str(len(av)) + " numbers are the average.")
print(str(len(low)) + " numbers are below the average.")
x = [1,2,3,4,5,6,7,8,9,10]
y = ["John","Joe","James","Alex","Tom","Paul","Rick","Steve","Sam","Stacy"]

for i in range(len(y)):
    print(y[i])

for i in range(len(x)):
    print("Name: " + str(x[i]) + " Index: " + str(i))

print(x[4:9])
print(x[3:])

z = int(input("Enter a number for list to be repeated: "))

print(x*z + y*z)

u = x+y
print(u)

for i in range(len(x)):
    print("ID: " + str(x[i]) + " Name: " + y[i])


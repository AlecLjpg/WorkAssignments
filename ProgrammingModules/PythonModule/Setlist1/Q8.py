x = (1,2,3,4,5,6,7,8,9,10)
y = (20,30,40,50,60,70,80,90,100)
for i in range(len(x)):
    print (x[i])

print("Sliced tuple: " + str(x[0:len(x):2]))
print("Repeated tuple: " + str(x*10))
z = x+y
print("Concatenated tuples: " + str(z))

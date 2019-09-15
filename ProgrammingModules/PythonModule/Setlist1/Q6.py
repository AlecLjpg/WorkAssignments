x = input("Enter a string to be maniuplated: ")
y = list(x)
i = 0

while i <len(y):
    print (y[i])
    i += 1
print("Sliced string: " + x[0:len(x):2])
print(x*100)
z = input("Enter a second string to be concatenated: ")
print(x+" "+z)

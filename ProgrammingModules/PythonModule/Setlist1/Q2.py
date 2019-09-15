
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

def largest(x,y,z):
    if x>y and x>z:  
        print(str(x) + " is the largest number")
    elif y>x and y>z: 
        print(str(y) + " is the largest number")
    elif z>x and z>y:
        print(str(z) + " is the largest number")

largest(x,y,z)
    

x = int(input("Enter a number to find out if it is prime: "))

def primeFunc(x):
    if x==2:
        return True
    if x%2 == 0 or x<=1:
        return False
    squareRoot = int(x**0.5) + 1

    for i in range(3,squareRoot,2):
        if x%i == 0:
            return False
    return True

if primeFunc(x) == False:
    print("The number is not prime")
elif primeFunc(x) == True:
    print("The number is prime")
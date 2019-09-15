x = int(input("Enter a number to find out if its odd or even: "))

remainder = x%2

def oddOrEven(remainder):
    if remainder == 0:
        print("The number is even")
    if remainder != 0:
        print("The number is odd")

oddOrEven(remainder)
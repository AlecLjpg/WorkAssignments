import math
import random

x = float(input("Enter a float for it to be rounded: "))
print(str(x) + " rounded returns: " + str(round(x)))

y = float(input("Enter a number to find its square root: "))
print("The square root of " + str(y) + " is: " + str(math.sqrt(y)))

print("Random number between 0-1: " + str(random.randint(0,1)))
print("Random number between 10-500: " + str(random.uniform(10,500)) )
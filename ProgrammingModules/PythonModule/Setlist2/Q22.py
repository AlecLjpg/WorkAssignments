import math

x = float(input("Enter x value for trig functions: "))
y = float(input("Enter y value for trig functions: "))

print("Arc Cosine of x:" + str(math.acos(x)))
print("Arc Sine of x: " + str(math.asin(x)))
print("Arc Tan of x: " + str(math.atan(x)))
print("Tan of y/x: " + str(math.atan2(y,x)))
print("Cosinse of x: " + str(math.cos(x)))
print("Euclidean norm of x,y: " + str(math.hypot(x,y)))
print("Sine of x: " + str(math.sin(x)))
print("Tan of x: " + str(math.tan(x)))
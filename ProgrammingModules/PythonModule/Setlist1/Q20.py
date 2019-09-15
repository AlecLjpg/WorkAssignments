x = int(input("Enter a number for the max of a Fibonacci series: "))

y = []

def fibonacci(x):
    for i in range(x):
        if i == 0 or i == 1: y.append(i)
        if i > 1: y.append(y[i-1] + y[i-2])

fibonacci(x)
print("Fibonacci Sequence: ")
for i in range(len(y)):
    print("Index: " + str(i) + " | " + str(y[i]))
y = ["John","Tom","Joe","Rick","Paul"]
x = input("Enter a name to see if it exists in the list: ")
z = True

if x in y:
        print(x + " exists in the list!")

if x not in y:
    print(x + " does not exist in the list")

for i in range(len(y)):
    if x == y[i]:
        z = False
        print(x + " exists in the list!")
if z == True:
    print(x + " does not exist in the list.")

print(y[::-1])
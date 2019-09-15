x = input("Enter a string to check the number of vowels are included: ")
xList = list(x)
aCount = 0
eCount = 0
iCount = 0
oCount = 0
uCount = 0
totalCount = 0


for val in xList:
    if val == 'a' or val == 'A': 
        aCount+=1
        totalCount+=1
    if val == 'e' or val =='E':
        eCount+=1
        totalCount+=1
    if val == 'i' or val == 'I':
        iCount+=1
        totalCount+=1
    if val == 'o' or val == 'O':
        iCount+=1
        totalCount+=1
    if val == 'u' or val == 'U':
        uCount+=1
        totalCount+=1

print("Total number:" + str(totalCount))
print("A: " + str(aCount))
print("E: " + str(eCount))
print("I: " + str(iCount))
print("O: " + str(oCount))
print("U: " + str(uCount))



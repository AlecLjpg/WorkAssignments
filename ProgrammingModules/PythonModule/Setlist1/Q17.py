x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
y = int(input("Enter a number of elements to compare to find the smallest/largest numbers: "))

z = x[0:y]

print("The maximum of the list is: " + str(max(z)))
print("The minimum of the list is :" + str(min(z)))

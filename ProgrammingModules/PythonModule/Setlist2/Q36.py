tup1 = ("A","B","C","D")
tup2 = ("E","F","G","H")

print("Comparison of tup1 and tup2:")
if tup1 > tup2:
    print("Tup1 is greater than tup2")
elif tup2 > tup1:
    print("Tup2 is greater than tup1")

print("Length of tup1:" + str(len(tup1)))
print("Length of tup2: " + str(len(tup2)))

print("Max of tup1: " + max(tup1))
print("Max of tup2: " + max(tup2))

print("Min of tup1: " + min(tup1))
print("Min of tup2: " + min(tup2))

list1 = list(tup1)
list2 = list(tup2)

print("Conversion of list1 and list2 into tuples:")
print("List1: " + str(tuple(list1)))
print("List2: " + str(tuple(list2)))
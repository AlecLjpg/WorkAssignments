dict1 = {"Animal Type":"Dog", "Color":"Brown", "Age":4}
dict2 = {"Name":"Alec","Eye Color":"Blue","Age":23}
dict3 = {"Make":"Nissan","Model":"Frontier","Year":2016}

if cmp(dict1,dict2) == 1 and (dict1,dict3) == 1:
    print("Dict1 is the greatest")
elif cmp(dict2,dict1) == 1 and cmp(dict2,dict1) == 1:
    print("Dict2 is the greatest")
elif cmp(dict3,dict1) == 1 and cmp(dict3,dict2) == 1:
    print("Dict3 is the greatest")

print("Adding new elements to dict1 and dict2: ")
dict1.update({"Favorite Toy":"Squeaky Toy"})
dict2.update({"Height":"5 11"})
print(dict1)
print(dict2)

print("The lengths of dict1,dict2, and dict3:")
print(len(dict1))
print(len(dict2))
print(len(dict3))


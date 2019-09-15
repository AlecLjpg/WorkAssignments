tup1 = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
tup2 = ('January','February','March','April','May','June','July','August','September','October','November','December')
tup3 = tup1 + tup2
print(tup3)

tup1x = (1,3,4,5)
tup2x = (1,5,9,7)
tup3x = (3,6,7,4)

if (tup1x>tup2x and tup1x>tup3x):
    print("Tuple 1 is the greatest")
elif(tup2x>tup1x and tup2x>tup3x):
    print("Tuple 2 is the greatest")
elif(tup3x>tup1x and tup3x>tup2x):
    print("Tuple 3 is the greatest")

tup1x = list(tup1x)
tup1x.insert(8,7)
tup1x = tuple(tup1x)
print("Tup1 with new elements added through typecasting:")
for val in tup1x:
    print(val)

print("Skipping odd numbers:")
for i in range(101): 
    if i%2 == 0:
        print(i)

print("Skipping odd numbers, break at 50:")
for i in range(101):
    if i%2 == 0:
        print(i)
    if i == 50:
        break

print("Skipping odd numbers, continue at 10,20,30,40, and 50:")
for i in range(101):
    if i%2 == 0:
        if i == 10 or i== 20 or i == 30 or i == 40 or i == 50:
            continue
        else :print(i)

print("Skipping odd numbers, break at 90: ")
for i in range(101):
    if i%2 == 0:
        print(i)
    if i == 90:
        break

print("Skipping odd numbers, continue at 60,70,80, and 90: ")
for i in range(101):
    if i%2 == 0:
        if i == 60 or i == 70 or i == 80 or i ==90:
            continue
        else: print(i)
   
    

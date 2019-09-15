x = input("Enter a string to see if it is a palindrom: ")

def palindromeCheck(x):
    if str(x) == str(x)[::-1]:
        print(x + " is a palindrome")
    else: print(x + " is not a palindrome")

palindromeCheck(x)
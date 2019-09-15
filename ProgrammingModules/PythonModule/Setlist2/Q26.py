import base64
x = input("Enter a word to be encoded and decoded: ")

y = base64.b64encode(x.encode('utf-8',errors='strict'))

print("Encoded String: ", y)

z = base64.b64decode(y.decode('utf-8',errors='strict'))

print("Decoded string: ", z)
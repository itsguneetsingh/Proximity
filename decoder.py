import base64

a = input("Enter whatever you want to: ")
try:
    text = base64.b64decode(a)
except:
    print("Nothing")

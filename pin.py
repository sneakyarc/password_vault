import passman as p
import hashlib
import os
if not os.path.exists("pin.key"):
    print('\nGenerate a pin first')
    pin=(input("Enter 4 digit pin : "))
    if len(pin)!=4 or not pin.isdigit():
        print("\nEnter 4 digits")
        exit()
    confirm=input("confirm your pin : ")
    if confirm != pin:
        print("Passsword do not match")
        exit()
    hashed=hashlib.sha256(pin.encode()).hexdigest()
    with open("pin.key","w") as f:
        f.write(hashed)
    p.mainfun()   
else :
    pin=input("enter your pin - ")
    if len(pin)!=4 or not pin.isdigit():
        print("\nPlease enter 4 digits ")
        exit()
    hashedinput=hashlib.sha256(pin.encode()).hexdigest()
    with open("pin.key","r") as f:
        savedpin=f.read()
        if hashedinput != savedpin:
            print("--Wrong pin --")
            exit()
        print("\nAccess granted.....opening your vault")
        p.mainfun()




    


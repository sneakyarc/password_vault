from cryptography.fernet import Fernet
def generate():
    key = Fernet.generate_key()
    with open("key.key","wb") as f:
        f.write(key)
def load():
    with open("key.key","rb") as f:
        return f.read()
def encr(password):
    key=load()
    f=Fernet(key)
    return f.encrypt(password.encode()).decode()
import json
import os
def save(acc,user,password):
    encrypted=encr(password)
    if os.path.exists("vault.json"):
        with open("vault.json","r") as f:
            data =json.load(f)
    else:
        data={}
    new_entry={"user":user,"password":encrypted}
    if acc in data:
        data[acc].append(new_entry)
    else:
        data[acc]=[new_entry]
    with open("vault.json","w") as f:
        data=json.dump(data,f,indent=4)

   
def decr(encrpass):
    key=load()
    f=Fernet(key)
    return f.decrypt(encrpass.encode()).decode()
def getpass(acc):
    try:

        with open("vault.json","r") as f:
            data=json.load(f)
            if acc in data:
                length=len(data[acc])
                print(length,"accounts found :")
                for i in range(len(data[acc])) :
                    username=data[acc][i]["user"]
                    print(i+1,username)
                choice=int(input("enter choice : "))
                if 1<= choice <=len(data[acc]):
                    selected=data[acc][choice-1]
                    decrypted=decr(selected["password"])
                    print(f"Username :",selected["user"])
                    print(f"Password:",decrypted)
                else:
                    print("Invalid choice")
                



                    
            else:
                return "Account not found"
    except FileNotFoundError:
        return "No passwords saved yet, :)"
if not os.path.exists("key.key"):
    print("First time setup, generating key......",end='')
    generate()
    print("...key created")
def mainfun():
    while True:
        print("="*30)
        print("\nPassword vault")
        print("="*30)


        print("1. Save new password")
        print("2. Get saved password")
        print("3. List all saved passwords")
        print("4. Exit")
        choice=input("Enter choice :")
        if choice =="1":
            acc=input("account name :")
            user=input("Username :")
            pwd=input("password: ")
            save(acc,user,pwd)
            print("saved succesfully")
        elif choice=="2":
            acc=input("enter account name :")
            result=getpass(acc)
            print("your password :",result)
        elif choice=="4":
            print("goodbye")
            break
        elif choice=="3":
            try:
                with open("vault.json","r") as f:
                    data=json.load(f)
                    if data:
                        for i,j in data.items():
                            print(f"  > {i} ({j['user']})")
                    else:
                        print("No files saved yet")
            except FileNotFoundError:
                print("No files saved yet")
        else:
            print("invalid")
if __name__=="__main__":
    print("X-- ACCESS DENIED --X")



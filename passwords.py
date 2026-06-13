#creating a dictionary
import random
import string
dictionary={}
while True:
    print("1. Insert")
    print("2. Display all names")
    print("3. Display all passwords")
    print("4. Get passwords")
    print("5. Delete")
    print("6. Create randomn names and passwords")
    print("7. Exit")
    option=input("enter your choice ")
    if option=="1":
        name=input("enter the name ")
        password=input("enter the password ")
        dictionary[name]=password
        print("you have added a name to the dictionary")
    elif option=="2":
        print(dictionary.keys())
    elif option=="3":
        print(dictionary.values())
    elif option=="4":
        name=input("enter the name ")
        print(dictionary[name])
    elif option=="5":
        delete=input("what name do you want to delete? ")
        del dictionary[delete]
    elif option=="6":
        names = ["Ariana","Letsy","Oren","Nancy","Timmy","Greg"]
        passwords = ["hello123","letsy@wesome","54O","Yess67","timtim98","#sooocuteee"]
        import random
        g6=random.choice(names)
        print(g6)
        h5=random.choice(passwords)
        print(h5)
    elif option=="7":
        print("We will exit now")
        break
        
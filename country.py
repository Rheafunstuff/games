#creating a dictionary
dictionary={}
while True:
    print("1. Insert")
    print("2. Display all countries")
    print("3. Display all capitals")
    print("4. Get capitals")
    print("5. Delete")
    print("6. Exit")
    option=input("enter your choice ")
    if option=="1":
        country=input("enter the country ")
        capital=input("enter the capital ")
        dictionary[country]=capital
        print("you have added the country to the dictionary")
    elif option=="2":
        print(dictionary.keys())
    elif option=="3":
        print(dictionary.values())
    elif option=="4":
        country=input("enter the country name ")
        print(dictionary[country])
    elif option=="5":
        delete=input("what country do you want to delete? ")
        del dictionary[delete]
    elif option=="6":
        print("We will exit now")
        break



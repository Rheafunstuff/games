dictionary={"age":10,"name":"Rhea","country":"England"}
print(dictionary)
#display all the keys
print(dictionary.keys())
#display all the values
print(dictionary.values())
#accessing the values in the dictionary
print(dictionary["country"])
#check if the key exists in the dictionary or not
if "age" in dictionary:
    print(dictionary["age"])
else:
    print("The key doesn't exist")
#add new key value pair to the dictionary
dictionary["continent"]="Europe"
print(dictionary)
#update a value in the dictionary
dictionary["name"]="Rayna"
print(dictionary)
#how to delete anything from the dictionary
del(dictionary["age"])
print(dictionary)
#store a list as a value in the dictionary
dictionary["marks"]=[5,10,15,20]
print(dictionary)
#access a value in the list stored in the dictionary
print(dictionary["marks"][1])
#create nested dictionary-it means dictionary inside another dictionary
classroom={
    "Tokyo":{
        "Age":21,"Country":"Russia"
    },
    "Chocolate":{
        "Age":45, "Country":"France"
    }
}
print(classroom.keys())
print(classroom.values())
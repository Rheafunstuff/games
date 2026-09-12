#Lists always use square brackets that look like []

#An example of a list named fruits is:
fruits=["Apples", "Strawberries", "Bananas", "Melon", "Pommegranite"]
print(fruits)

#An example of a list where only a few numbers are printed is:
numbers=[3, 5, 7, 9 , 11]
print(numbers[0], numbers[2], numbers[4])

#An example of when an element from the list has been updated
colours=["pink", "blue", "green", "purple", "white"]
print(colours)
colours[1]="black"
print(colours)

#An example of adding an element to a list
subjects=["maths", "english", "chemistry", "physics"]
print(subjects)
subjects.append("computer science")
print(subjects)

#An example of inserting an element to a list at a specifice place
numbers_2=[0, 50, 150, 200, 250]
numbers_2.insert(2, 100)
print(numbers_2)

#An example of removing an element from a list
animals=["tiger", "cheetah", "monkey", "lion", "hyena"]
print(animals)
animals.remove("lion")
print(animals)

#An example of removing an element using pop
numbers_3=[6, 7, 8, 9, 10, 13]
print(numbers_3)
#deleting the last item from the list
value_deleted = numbers_3.pop()
print(f"{value_deleted} is deleted from this list")

#deleting items from specific positions/index
variable = numbers_3.pop(3)
print(f"{variable} is deleted from this list")
print(numbers_3)

#An example of using the function len on a list
students=["Jack", "Jones", "Emily", "Tayla", "Nora", "Joushua"]
print(students)
print(len(students))

#An example of creating a list and asking the user to check whether an element is in the list or not
sports=["gymnastics", "tennis", "swimming", "football", "netball"]
print(sports)
operation = input("Write down a sport and we will tell you whether it is in the list or not ")
if operation in sports:
    print("That is a sport in our list!")
else:
    print("Sorry, that is not in our list")

#An example of an element's index being told to the user
numbers_5=[2, 4, 6, 8, 10, 12]
print(numbers_5)
print(f"The index of 10 in the list is {numbers_5.index(10)} ")
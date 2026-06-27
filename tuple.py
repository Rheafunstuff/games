#we cannot add, update or delete anything in a tuple, the circle brackets are optional in a tuple
tuple=("a", "c", "f", "k", "g", "h", "n", "y", "z")
print(tuple)
tuple="j", "l", "v", "s", "a", "b", "u"
print(tuple)
#creating a nested tuple
tuple=6, 7, 25, 26, 78,(45, 23, 90)
print(tuple)
#accessing a tuple
print(tuple[5][1])
print(tuple[3])
#slicing of tuples
tuple= 3, 4 , 5, 6 , 7 , 8, 9, 10
print(tuple[1:4])
print(tuple[-3:])
print(tuple[-4:-1])
print(tuple[0:3])
print(tuple[:])
tuple= 5, 67, 90,[49, 12, 83]
print(tuple)
#tuple[1]=4 it throws an error because you cannot update an element
tuple[3][2]=33
print(tuple)
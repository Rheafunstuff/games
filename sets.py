list=[2,4,5,7,2,6,5]
print(list)
sets=set(list)
print(sets)
#sets are nonindexible
#print(sets[1]) it throws an error
#check if element exists in the set
if 9 in sets:
    print("yes")
else:
    print("no")
#add an element to the set
set1=set([])
set1.add(3)
set1.add(7)
set1.add(2)
set1.add(7)
print(set1)
#remove a element from the set
set1.remove(3)
print(set1)
#set operations
s1={1,4,7,3}
s2={2,4,8,9}
#union meansn combining the sets together
print(s1.union(s2))
#intersection means the common element of both the sets
print(s1.intersection(s2))
#difference of sets means the element that is present in the first set and not in the second
print(s1.difference(s2))
#symmetric difference means combining the two sets without the common element
print (s1.symmetric_difference(s2))
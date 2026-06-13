#count the occurence of vowels in the string entered by the user
#method one, approach one
operation=input("enter a word ")
vowels={"a":0, "e":0, "i":0, "o":0, "u":0}
for i in operation:
    if i in vowels:
        vowels[i]+=1
print(vowels)
#method two, approach two
operation=input("enter a word ")
vowellist=["a", "e", "i", "o", "u"]
vowels={}
for i in operation:
    if i in vowellist:
        if i in vowels:
            vowels[i]+=1
        else:
            vowels[i]=1
print(vowels)
#count the occurence of each alphabet in the string
operation=input("enter a word ")
count={}
for i in operation:
    if i.isalpha():
        if i in count:
            count[i]+=1
        else:
            count[i]=1
print(count)
word = "Tbilisi"  

if word[0].isupper():
    print(word.upper())
else:
    print(word.lower())


    
    name = input("Enter your name: ")

result = ""

for i in name:
    if i.isupper():
        result = name.lower()
        break
    else:
        result = name.capitalize()
print(result)



animals = ["Lion","Tiger","Elephant"]
 

for i in animals:
    if (len(i) < 5) and (i == i.capitalize()):
        print(i[0:3])
        
    else:
        print("This word is so long")


new_list = [True,"Luka",5,0.8,"Nika"]


for i in new_list:
    if type(i) == str:
        print(i.upper()[-3:])



names = ["nika", "luka", "saba", "ana"]

for i in names:
    print(i.upper())

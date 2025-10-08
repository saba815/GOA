names = ["giorgi","saba",5,10,5.5,6.6,True,False]

strings = []

numbers = []

floats = []

bools = []

for i in names:
    if type(i) == str:
        strings.append(i)
    elif type(i) == int:
        numbers.append(i)
    elif type(i) == float:
        floats.append(i)
    elif type(i) == bool:
        bools.append(i)


print(strings)

print(numbers)

print(floats)

print(bools)
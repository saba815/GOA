numbers = [3, 5, 10, 12, 15, 18, 20, 30, 33, 45]

result = [num for num in numbers if num % 3 == 0 and num % 5 == 0]

print(result)

names = ["Nika", "Saba", "Ana", "Giorgi", "Luka", "Nino"]


even_names = [name for name in names if len(name) % 2 == 0]

print(even_names)


#list comprehension არის სპეციალური რაღაც ფიტონში რითაც ვწერთ მოკლედ და სწრაფად
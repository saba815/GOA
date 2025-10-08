number = int(input("შეიყვანეთ რიცხვი: "))

if number % 2 == 0:
    print("even")
else:
    print("odd")


my_name = "saba"   # აქ შეგიძლია ჩაწერო შენი სახელი
user_name = input("შეიყვანეთ თქვენი სახელი: ")

if user_name == my_name:
    print("Hello")
else:
    print("Bye")

    num = int(input("შეიყვანეთ რიცხვი: "))

if num > 90:
    print("A")
elif num > 70:  
    print("B")
elif num > 50:   
    print("C")
else:
    print("D")


i = 1
while i <= 100:
    if i % 2 == 0:
        print(i, "ლუწია")
    else:
        print(i, "კენტია")
    i += 1




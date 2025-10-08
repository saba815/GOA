pin = "1234"


user_input = input("შეიყვანეთ პინ კოდი: ")


while user_input != pin:
    print("პინ კოდი არასწორია, სცადეთ თავიდან!")
    user_input = input("შეიყვანეთ პინ კოდი: ")

print("პინ კოდი სწორია ✅")

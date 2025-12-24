users = []

username = input("შეიყვანეთ username: ")
password = input("შეიყვანეთ password: ")

count = 0

for user in users:
    if user["username"] == username:
        count = count + 1

if count == 1:
    print("ეს Username უკვე დაკავებულია!")
else:
    new_user = {
        "username": username,
        "password": password
    }

    users.append(new_user)
    print("მომხმარებელი დაემატა!")
    print(users)

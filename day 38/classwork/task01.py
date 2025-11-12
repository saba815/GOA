about_me = {
    "name": "saba",
    "age": 10,
    "city": "tbilisi"
}

name = about_me["name"]

print("my name is:", name)

about_me["age"] = 11

print(about_me)

about_me.pop("city")

print(about_me)

for key,value in about_me.items():
    print(key,value)
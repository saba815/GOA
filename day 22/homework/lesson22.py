word = input("enter a word: ")

print(word.lower())      
print(word.upper())      
print(word.capitalize()) 

sentence1 = input("enter first sentence: ")
sentence2 = input("enter second sentence: ")
sentence3 = input("enter the third sentence: ")

print(sentence1.lower())      
print(sentence2.upper())      
print(sentence3.capitalize()) 

my_name = "saba"  
user_name = input("enter your name: ")

if my_name.lower() == user_name.lower():
    print("Our names are similar!")
else:
    print("We have different names")

    sentence = "heLLo everYone, WELcome To Goa!"
formatted_sentence = sentence.capitalize()
print(formatted_sentence)




# .lower() — აქცევს ყველა ასოს პატარა ფორმატში
# მაგალითი:
# print("HELLO".lower()) → "hello"

# .upper() — აქცევს ყველა ასოს დიდ ფორმატში
# მაგალითი:
# print("hello".upper()) → "HELLO"

# .capitalize() — აქცევს მხოლოდ პირველ ასოს დიდად, დანარჩენს კი პატარად
# მაგალითი:
# print("hELLO".capitalize()) → "Hello"

# .find() — აბრუნებს იმ ადგილს, სადაც პირველად იპოვა მითითებული ნაწილი
# მაგალითი:
# print("hello".find("e")) → 1

# .count() — ითვლის რამდენჯერ გვხვდება მოცემული ნაწილი
# მაგალითი:
# print("banana".count("a")) → 3





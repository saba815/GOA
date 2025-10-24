def remove_first_last(text):
    return text[1:-1]

print(remove_first_last("hello"))  
print(remove_first_last("python"))

def check_list_length(lst):
    if len(lst) > 4:
        return "სია ძალიან დიდია"
    else:
        return lst


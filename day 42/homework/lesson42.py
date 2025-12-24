data = []


def register():
    username = input("Enter your username: ")
    

    password = input("Create a new password: ")


    current_user = {
        "name": username,
        "password": password
    }


    if len(data) == 0:
        print("Registration successful!")
        data.append(current_user)

  
    else:
        for i in data:
           
            if i["name"] == current_user["name"]:
                print("Username already exists!")
                
               
                username = input("Enter another username: ")
                current_user["name"] = username
                
                data.append(current_user)
                print("Registration successful!")
                break
            else:
                
                print("Registration successful!")
                data.append(current_user)
                break


def login():
   
    username = input("Enter your username: ")
    
   
    password = input("Enter your password: ")

    
    for i in data:
       
        if i["name"] == username and i["password"] == password:
            print("Login successful!")
            return

    
    print("Incorrect username or password!")



register()

login()

print(data)

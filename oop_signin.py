import json

class user:
    def __init__(self):
        print("1. Sign up")
        print("2. Sign up")
        ch = int(input("Enter an option"))
        if ch == 1:
            self.Register_User()
            print("Signup successful !!")
        else:
            self.authentication()

    def Register_User(self):
        self.user_name = input("Enter your new username")
        self.password = input("Enter your new password")
        self.mobile_num = input("Enter your new mobile_number")
        print("To signup")
        print("--"*25)
        signup_dict = {
            "username" : self.user_name,
            "password" : self.password,
            "mobile_number" : self.mobile_num
        }
        try:
            with open("database.json","r") as f:
                data = json.load(f)
                data_list = data["student"]
        except FileNotFoundError:
            data={}
            data_list = []

        data_list.append(signup_dict)
        data.update({"student" : data_list})

        with open("database.json",'w') as f:
            json.dump(data,f)
            print("Sign up successful")


    def authentication(self):
        user_name = input("Enter your username")
        password = input("Enter your password")
        
        with open("database.json",'r') as f:
            data = json.load(f)
    
        data_list = data["student"]
        
        for i in data_list:
            if (i["username"] == user_name):
                if (i["password"] == password):
                    self.user_name = user_name
                    self.password = password
                    self.mobile_num = i["mobile_number"]
                    
                    print("Logged in successfully")

                    self.welcome_user(user_name)
                    return
                
                print("Incorrect Password")
                return

        print("No such username\n")

    def welcome_user(self,username):
        print("Hello ", username)
        print("your mobile_num is ", self.mobile_num)

        print("1. Enter note")
        print("2. Display note")
        print("3. Exit")

        ch = int(input("enter a choice:"))
        if ch == 1:
            self.word = input("Enter your note")
        elif ch == 2:
            print(self.word)
        else:
            exit()

while True:
    print("\n\n", "--"*25, "\n\n")
    user1 = user()
    ch = input(("Do you want to continue(Y/N)"))
    if ch.lower() != 'y':
        break
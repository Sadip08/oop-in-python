class user:
    def __init__(self):
        print("1. Sign up")
        print("2. Sign up")
        ch = int(input("Enter an option"))
        if ch == 1:
            [self.user_name,self.password,self.mobile_num] = self.Register_User()
        else:
            self.authentication()

    def Register_User(self):
        user_name = input("Enter your new username")
        password = input("Enter your new password")
        mobile_num = input("Enter your new mobile_number")
        return [user_name,password, mobile_num]
    
    def authentication(self):
        user_name = input("Enter your username")
        password = input("Enter your password")
        if user_name == self.user_name and password == self.password:
            self.welcome_user(user_name)

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

user1 = user()
user2 = user()
    
    
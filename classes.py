class Employee:
    def __init__(self, first,last,pay):         #constructor(self, object/s)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@gmail.com"

    def fullname(self):
        print(self.email)
        return '{} {}'.format(self.first, self.last)

emp1 = Employee('Sadip','Tamang',1000)
emp2 = Employee('Madan','Tamang',5000)

print(emp1.fullname())
print(Employee.fullname(emp2))


'''
Class :
    -> Collection of functions and variables, which can work independently on its own.
    -> Example in real world scenario is Animal, Vehicles

Object :
    -> Instance of a class (Has its own independent identity)
    -> Dog from Animal can be an object, Car in vehicles
    -> Each object has its own set of attributes
    -> Dog has 4 legs(Variables) and barks (Functions)


'''

class Calculator:

    def add_2_numbers(self,a,b):
        return a+b
    
    def subtract_2_numbers(self,a,b):
        return a-b
    
    def multiply_2_numbers(self,a,b):
        return a*b
    
    def divide_2_numbers(self,a,b):
        return a/b
    

s1 = Calculator()
print(s1.add_2_numbers(4,2))
print(s1.subtract_2_numbers(4,2))
print(s1.multiply_2_numbers(4,2))
print(s1.divide_2_numbers(4,2))

s2 = Calculator()
print(s2.add_2_numbers(6,3))
print(s2.subtract_2_numbers(6,3))
print(s2.multiply_2_numbers(6,3))
print(s2.divide_2_numbers(6,3))

'''
Constructor:
    -> Constructor is used during initialization, such that as soon as an object is created it jumps to the constructor part.
    -> Syntax :
        def __init__(self):
            Constructor code here

'''

'''
How does encapsulation and different instances work !!

'''
print("--"*25)

class Animal:
    def __init__(self,animal_name, animal_species, animal_dob):
        self.name = animal_name
        self.species = animal_species
        self.dob = animal_dob

species_1 = Animal('Rojo', 'Dog', "2015-3-3")
print(species_1.name, species_1.species, species_1.dob)


'''
Task 2:
WAP that uses OOP
has class user
when initialized it provides options:
    1. sign up
    2. Sign in

if 1 is pressed, it redirects to a method named Register_User
this method takes in username, password and mobile number

if 2 is pressed, t redirects to a method name euthentication
this method checks input username and password with self.username
and self.password
if match it redirects to another method named welcome_user

welcome user method greets them, displays username and displays
their mobile number

also this method gives 2 options.
1. enter note
2. Display note
3. exit

if 1 is pressed user can input a large note that is saved for that object

if 2 is pressed, all notes is displayed

if 3 is pressed terminate
'''
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
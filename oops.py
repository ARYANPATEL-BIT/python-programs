# class car:
#     color = "Red"
#     brand = "Toyota"

#     def drive(self):
#         print("the car is driving")

# myCar = car()
# print(myCar.color)
# print(myCar.brand)


# class Dog:

#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name
#     def bark(self):
#         print("wolf")

# dog1 = Dog('Labrador',"??")
# dog2 = Dog("pug", "!!")

# dog1.bark()
# dog2.bark()

# print(dog1.breed)
# print(dog1.name)
# print(dog2.name)
# print(dog2.breed)


# class Car:

#     def __init__ (self, brand):
#         self.brand = brand
#     def start(self):
#         print(f"${self.brand} Started ")

# car1 = Car("Dodge")
# car2 = Car("Chervolet")

# print(car1.brand)
# print(car2.brand)

# car1.start()
# car2.start()


# class Student:

#     def __init__ (self,name,grade,age):
#         self.name = name
#         self.grade = grade
#         self.age = age
    
#     def display_info(self):
#         print(f'''Student: {self.name} \nGrade: {self.grade}\nAge: {self.age}''')
    
#     def is_passing(self):
#         if self.grade >= 40:
#             print(f"{self.name} is Passing")
#         else:
#             print(f"{self.name} is Failing")

# student1 = Student("Aryan", 100, 20)
# student2 = Student("Someone", 100 , 18)
# student3 = Student("Caman", 39, 19)

# student1.display_info()
# student2.display_info()
# student3.display_info()

# student1.is_passing()
# student2.is_passing()
# student3.is_passing()



# class BankAccount:


#     def __init__ (self, owner, balance):
#         self.owner = owner
#         self.balance = balance
    
#     def deposit(self):
#         amount = int(input(f"Welcome {self.owner} Please Enter the amount to deposite: "))
#         self.balance += amount
#         print(f"${amount} successfully added \nTotal amount: ${self.balance}")
        
#     def withdraw(self):
#         while True:
#            amount = int(input(f"Welcome {self.owner} Please Enter the amount to Withdraw: "))

#            if amount > self.balance:
#                print(f"Insufficient Funds Please enter a Vaild Amount \nCurrent Balance {self.balance}")
#            else:
#                self.balance -= amount
#                print(f"${amount} Successfully withdrawed \nTotal Amount: ${self.balance}")
#                break
    
#     def display_balance(self):
#         print(f"Welcome {self.owner}  Current Balance: ${self.balance}")

# owner1 = BankAccount("Aryan", 10000)
# owner2 = BankAccount("Someone", 230984)

# owner1.deposit()
# owner1.withdraw()
# owner1.display_balance()

# owner2.deposit()
# owner2.withdraw()
# owner2.display_balance()


# class Student:
#     def __init__ (self, name, marks):
#         self.name = name
#         self.marks = marks
#     def display(self):

#         print(self.name)
#         print(self.marks)

#     def grade(self):
#         if self.marks >= 90:
#             print("Grade A")
#         elif self.marks >= 75:
#             print("Grade B")
#         else:
#             print("grade C")

# student1 = Student("aryan", 100)
# student2 = Student("unknown", 1000)
# student3 = Student("UNknown2",74)

# student1.display()
# student1.grade()
# student2.display()
# student2.grade()
# student3.display()
# student3.grade()


# class Empolyee:
#     company_name = "Mars"

#     def __init__ (self,name):
#         self.name = name
    
#     @classmethod
#     def change_company(cls,new_name):
#         cls.company_name = new_name
    
#     def show(self):
#         print(self.name,Empolyee.company_name)

# e1 = Empolyee("Pratham")
# e2 = Empolyee("Pushkar")

# e1.show()
# e2.show()

# Empolyee.change_company("Google")
# e1.show()
# e2.show()


# class Employee:

#     bonus = 1000

#     def __init__(self, name , salary):
#         self.name = name
#         self.salary = salary
    
#     def show_details(self):
#         total = self.salary + Employee.bonus
#         print(f"welcome {self.name} your salary is {total}")

#     @classmethod
#     def change_bonus(cls,new_bonus):
#         cls.bonus = new_bonus
    
# e1 = Employee("aryan", 100000)
# e2 = Employee("unknown" , 10000000)

# e1.show_details()
# e2.show_details()

# e1.change_bonus(1234)
# e1.show_details()

# e2.change_bonus(9876)
# e2.show_details()



# class Employee:
#     bonus = 1000
#     def __init__(self,working_hours):
#         self.working_hours = working_hours
    
#     @classmethod
#     def applicable(cls,new_bonus):
#         if(Employee.working_hours > 25):
#             cls.bonus = new_bonus
        
#     def show_details(self):
#         new = self.bonus
#         print(f"{new}")

# e1 = Employee(26)
# e2 = Employee(24)

# e1.applicable(1250)
# e2.applicable(1250)
# e1.show_details()
# e2.show_details()



# class Temp:

#     # def __init__ (self,temp):
#     #     self.temp = temp

#     @staticmethod
#     def Celcius_to_fahrenheit(celsius):
#         fahrenheit = (celsius * 9/5) + 32
#         return fahrenheit
    
#     @staticmethod
#     def fahrenheit_to_celsius(fahrrenheit):
#         celsius = (fahrrenheit-32)*5/9
#         return celsius

# print(Temp.Celcius_to_fahrenheit(0))
# print(Temp.fahrenheit_to_celsius(0))


# class Car:

#     total_cars = 10

#     def __init__ (self,model,mileage):
#         self.model = model
#         self.mileage = mileage
#         Car.total_cars += 1

#     @staticmethod
#     def is_mileage_good(mileage):
#         if(mileage > 15):
#             return True
#         else:
#             return False
        
#     @classmethod
#     def show_total(cls,new_cars):
#         cls.total_cars = new_cars

#     def details(self):
#         print(self.model , self.mileage, Car.total_cars)

# car1 = Car("Gt",10)
# car1.details()

# print(Car.is_mileage_good(car1.mileage))

# car1.show_total(15)
# car1.details()


# class MathOperation:
#     @staticmethod
#     def add(a,b):
#         return a+b
    
#     @staticmethod
#     def multiplication(a,b):
#         return a*b
    
# print(MathOperation.add(1,2))
# print(MathOperation.multiplication(2,3))


# class Person:

#     def __init__ (self,name):
#         self.name = name

#     def greet(self):
#         print(f"Welcome, {self.name}")

# p1 = Person("aryan")
# p1.greet()



# class MathUtils:

#     @staticmethod

#     def is_prime(n):
#         if n < 2:
#             return False
#         for i in range(2,int(n**0.5) +1):
#             if n % i == 0:
#                 return False
#         return True
    
# print(MathUtils.is_prime(10))
# print(MathUtils.is_prime(7))



# class Car:
#     wheels = 4
#     def __init__ (self,brand):
#         self.brand = brand

# c1 = Car("benz")
# c2 = Car("Dodge")

# print(c1.wheels)
# print(c2.wheels)

# Car.wheels = 6

# print(c1.wheels)
# print(c2.wheels)


# class student:
#     def __init__(self,name, age):
#         self.name = name
#         self.age = age

#     def info(self):
#         return f"{self.name} {self.age}"
# s1 = student("aryan",20)
# print(s1.info())


# class Student:

#     def __init__ (self,name,marks):
#         self.name = name
#         self.marks = marks

# class Topper(Student):
#     def show_marks(self):
#         print(self.name, self.marks)

# s1 = Topper("Aryan" , 100)

# s1.show_marks()


# class BankAccount:

#     def __init__(self,name,balance):
#         self.name = name
#         self.__balance = balance

#     def show_balance(self):
#         return f"{self.name}, {self.__balance}"

# c1 = BankAccount("Aryan",2039492)

# print(c1.show_balance())
# print(c1.name)
# print(c1.__balance)   ## will not work because of private attribute



# class Book:
#     def __init__(self,title,author):
#         self.title = title
#         self.author = author
    
#     def show_details(self):
#         print(f"Title: {self.title} , Author: {self.author}")

# a1 = Book("...","Aryan")
# a2 = Book("Unknow","Aryan")

# a1.show_details()
# a2.show_details()


# class Employee:

#     def __init__(self,name,salary):
#         self.name = name
#         self.__salary = salary

#     def manager(self):
#         return  f"Name: {self.name}, Salary: {self.__salary}"
    
# e1 = Employee("Aryan", 9358938)
# print(e1.name)
# print(e1)      ## will only show the name because the the salary attribute is private
# print(e1.manager())



# class locker:
#     def __init__(self):
#         self.__pin = 1234
    
#     def access(self):
#         got_Pin = int(input("Please enter the Pin: "))
#         if(got_Pin == self.__pin):
#             return "Access granted"
#         else:
#             return "Access Denied"
    
# user1 = locker()

# print(user1.access())
# print(user1.__pin)


# class Car:
#     def __init__(self):
#         self.__speed = 0
    
#     def acceleration(self,inc):
#         if (self.__speed + inc <=200):
#             self.__speed += inc
#         else :
#             self.__speed = 200
    
#     def brack(self,inc):
#         if(self.__speed - inc >= 0):
#             self.__speed -= inc
#         else:
#             self.__speed = 0
    
#     def get_speed(self):
#         print(f"current speed : {self.__speed}")


# s1 = Car()

# s1.acceleration(100)
# s1.get_speed()
# s1.brack(90)
# s1.get_speed()
# s1.acceleration(1000)
# s1.get_speed()
# s1.brack(93230)
# s1.get_speed()



# class ShoppingCart:

#     def __init__(self):
#         self.__total_amount = 0
    
#     def add(self,inc):
#         self.__total_amount += inc
    
#     def remove(self, out):
#         if(self.__total_amount - out >= 0):
#             self.__total_amount -= out
#         else:
#             print(f"current Amount {self.__total_amount} can not do in negative")
        
#     def display(self):
#         print(f"Your current ammount is {self.__total_amount}")


# p1 = ShoppingCart()

# p1.add(1990238)
# p1.display()
# p1.remove(29348)
# p1.display()
# p1.remove(9348503)
# p1.display()


# class fuelTank:
#     def __init__(self):
#         self.__fuel_level = 0

#     def add_fuel(self, add_fuel):
#         if(self.__fuel_level + add_fuel <= 50):
#             self.__fuel_level += add_fuel
#         elif (self.__fuel_level + add_fuel == 50):
#             self.__fuel_level = 50
#         else:
#             self.__fuel_level = 50
#             print("Your tank is full can not fill more than 50 Liters")

#     def use_fuel(self,del_fuel):
#         if(self.__fuel_level - del_fuel >= 0):
#             self.__fuel_level -= del_fuel
#         elif(self.__fuel_level - del_fuel == 0):
#             self.__fuel_level = 0
#         else:
#             self.__fuel_level = 0
#             print('Fuel Tank is empty please fill the fuel.')
    
#     def check_fuel(self):
#         print(f"Fuel Level is {self.__fuel_level}")

# f1 = fuelTank()

# f1.add_fuel(39)
# f1.check_fuel()
# f1.use_fuel(29)
# f1.check_fuel()
# f1.add_fuel(41)
# f1.check_fuel()
# f1.use_fuel(41)
# f1.check_fuel()
# f1.add_fuel(98453)
# f1.check_fuel()
# f1.use_fuel(89437)
# f1.check_fuel()



# class Wallet:
#     def __init__ (self):
#         self.__amount = 0
#         self.limit = 0

#     def add_money(self,add):
#         self.__amount += add
    
#     def spend_money(self,remove):
#         if remove > self.__amount:
#             print("❌ Insufficient Funds.")
#         elif remove > self.limit:
#             self.__amount -= self.limit
#             print(f"⚠️ Cannot spend more than daily limit")
#         else:
#             self.__amount -= remove
#             print(f"✅ Spent {remove}. Remaining balance: ₹{self.__amount}")

#     def set_limit(self,limit_value):
#         self.limit = limit_value
#         print(f"Your current limit is {self.limit}")

#     def show_wallet(self):
#         print(f"💰 Current balance: {self.__amount}")


# w1 = Wallet()
# w1.set_limit(10000)
# w1.add_money(10001)
# w1.show_wallet()
# w1.spend_money(1000)
# w1.show_wallet()
# w1.spend_money(8900)
# w1.show_wallet()


# class Wallet:
#     def __init__ (self,limit):
#         self.__amount = 0
#         self.limit = limit

#     def add_money(self,add):
#         self.__amount += add
    
#     def spend_money(self,remove):
#         if(self.__amount - remove < 0 ):
#             print("Insufficient Funds")
#         elif(self.__amount - remove  > 0 and remove <= self.limit):
#             self.__amount -= remove
#             self.limit -= remove
#         elif(self.__amount - remove >0 and remove > self.limit):
#             self.__amount -= self.limit
#             print("daily limit reached cannot remove more than")
    
#     def show_wallet(self):
#         print(f"your current balance : {self.__amount}. Remaining daily limit: {self.limit}")

# w1 = Wallet(10000)

# w1.add_money(10001)
# w1.show_wallet()
# w1.spend_money(1000)
# w1.show_wallet()
# w1.spend_money(8900)
# w1.show_wallet()
        


# class Vehical:
#     def __init__(self,brand):
#         self.brand = brand
#     def start(self):
#         print(self.brand)

# class Car(Vehical):
#     def drive(self):
#         print(self.brand)

# c =Car("bmw")
# c.drive()
# c.start()

# class Grandfather:
#     def house(self):
#         print("grandfather house")
# class Father(Grandfather):
#     def car(self):
#         print("father car")
# class Son(Father):
#     def bike(self):
#         print("son bike")

# s = Son()
# s.house()
# s.car()
# s.bike()


# class Mother:
#     def eye(self):
#         print("Mother")

# class Father:
#     def  face(self):
#         print("Father")

# class Child(Mother,Father):
#     def brain(self):
#         print("Child")

# c = Child()
# c.eye()
# c.face()
# c.brain()


# class Animal:
#     def eat(self):
#         print("all animal eats")
# class dog(Animal):
#     def speak(self):
#         print("barks")

# class Cat(Animal):
#     def speak(self):
#         print("meow")

# d =dog()
# c = Cat()
# d.speak()
# c.speak()



# class Book:
#     def __init__ (self,title,author):
#         self.title = title
#         self.author = author
# class EBook(Book):
#     def __init__(self, title, author,file_size):
#         super().__init__(title,author)
#         self.file_size = file_size

#     def display(self):
#         print(f"Author: {self.author} \nTitle: {self.title} \nfile size: {self.file_size}")
        
# ebook = EBook("Unknown","Aryan",75)
# ebook.display()



# class Commpany:
#     def __init__(self,company_name):
#         self.company_name = company_name

# class Employee(Commpany):
#     def __init__(self,company_name,employee_name):
#         super().__init__(company_name)
#         self.employee_name = employee_name

# class Developer(Employee):
#     def __init__(self,company_name,employee_name,tech_stack):
#         super().__init__(company_name,employee_name)
#         self.tech_stack = tech_stack
    
# class TeamLead(Developer):
#     def __init__(self,company_name,employee_name,tech_stack,team_size):
#         super().__init__(company_name,employee_name,tech_stack)
#         self.team_size = team_size


# class Info(TeamLead):
#     def display(self):
#         print(f"Employee: {self.employee_name} \nTech Stack: {self.tech_stack} \nCompany: {self.company_name} \nTeam Size: {self.team_size}")


# person = Info("Google","Aryan","Machine Learning",10)

# person.display()


# class Camera:
#     def __init__(self,take_photo):
#         self.take_photo = take_photo

# class Phone:
#     def __init__(self,make_call):
#         self.make_call = make_call

# class Smart_Phone(Camera,Phone):
#     def __init__(self,take_photo,make_call,browse_internet):
#         super().__init__(take_photo,make_call)
#         self.browse_internet = browse_internet

# class Display(Smart_Phone):
#     def display(self):
#         print(f"{self.take_photo},{self.make_call},{self.browse_internet}")

# phone = Display("photo took","made call","browsed internet")
# phone.display()


# class User:
#     def __init__(self,name,email):
#         self.name = name 
#         self.email = email

# class Student(User):
#     def __init__(self,name,email,course):
#         super().__init__(name,email)
#         self.course = course

# class PremiumStudent(Student):
#     def __init__(self,name,email,course,subscription_fee):
#         super().__init__(name,email,course)
#         self.subscription_fee = subscription_fee
    
#     def show_details(self):
#         print(self.name)
#         print(self.email)
#         print(self.course)
#         print(self.subscription_fee)


# student = PremiumStudent("aryan","@gmial","cs","ai")
# student.show_details()

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



# class Person:

#     def __init__ (self,name):
#         self.name = name

#     def greet(self):
#         print(f"Welcome, {self.name}")

# p1 = Person("aryan")
# p1.greet()



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




# class Student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score

#     def getName(self):
#         return self.name
    
#     def getScore(self):
#         return self.score

# try:
#     s1 = Student("aryan",99)

#     try:
#         if s1.getScore() <=0 or s1.getScore() >100:
#              raise ValueError("he score must be a positve number in range 1 - 100")
#         print(s1.getName())
#         print(s1.getScore())
#     except ValueError as error:
#         print(error)
#     except Exception as error:
#         print(error)
#         print("An unknown error occured")
# except Exception as outer_error:
#     print("Outer error: ", outer_error)
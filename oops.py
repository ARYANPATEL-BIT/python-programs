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
#     def applicable(cls,emp,new_bonus):
#         if emp.working_hours > 25:
#             cls.bonus = new_bonus
        
#     def show_details(self):
#         new = self.bonus
#         print(f"{new}")

# e1 = Employee(26)
# e2 = Employee(24)

# e1.applicable(e1,1250)
# e2.applicable(e2,1250)
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



# class MathUtils:

#     @staticmethod

#     def is_prime(n):
#         if n < 2:
#             return False
#         for i in range(2,int(n) +1):
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
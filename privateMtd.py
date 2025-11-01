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
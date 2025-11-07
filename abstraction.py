## hide personal details and show only essential details

## reduce Conplexity, security , improve maintainabilty , reusabilty, test ability

## abstract class => 

# from abc import ABC,abstractmethod

# class Shape(ABC):

#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return 3.14*self.radius*self.radius

# class Reactangle(Shape):
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length*self.width

# c = Circle(5)
# r = Reactangle(3,4)
# print(c.area())
# print(r.area())


# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass


# class Car(Vehicle):
#     def start_engine(self):
#         return "Car engine Started."

# class Bike(Vehicle):
#     def start_engine(self):
#         return "Bike engine started"

# c = Car()
# b = Bike()

# print(c.start_engine())
# print(b.start_engine())

# from abc import ABC , abstractmethod

# class Appliance(ABC):

#     @abstractmethod
#     def turn_on(self):
#         pass

#     @abstractmethod
#     def turn_off(self):
#         pass


# class WashingMachine(Appliance):
#     def turn_off(self):
#         return "washing machine turned off"
    
#     def turn_on(self):
#         return "washing machine turned on"
    

# class Refrigerator(Appliance):
#     def turn_off(self):
#         return "Refrigerator turned off"
    
#     def turn_on(self):
#         return "Refrigerator turned on"

# w = WashingMachine()
# r = Refrigerator()

# print(w.turn_off())
# print(w.turn_on())
# print(r.turn_on())
# print(r.turn_off())



# from abc import ABC,abstractmethod

# class Payment(ABC):
#     @abstractmethod
#     def make_payment(self):
#         pass

# class CreditCard(Payment):
#     def make_payment(self):
#         print("payment done via Creditcard")


# class PayPal(Payment):
#     def make_payment(self):
#         print("payment done via PayPal")

# class UPI(Payment):
#     def make_payment(self):
#         print("payment done via UPI")

# a = CreditCard()
# b = PayPal()
# c = UPI()

# a.make_payment()
# b.make_payment()
# c.make_payment()



from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self):
        pass

class CreditCard(Payment):
    def make_payment(self,amount):
        print("payment done via Creditcard",amount)


class PayPal(Payment):
    def make_payment(self,amount):
        print("payment done via PayPal",amount)

class UPI(Payment):
    def make_payment(self,amount):
        print("payment done via UPI",amount)


payment = [CreditCard(), PayPal(), UPI()]

for p in payment:
    p.make_payment(1900)



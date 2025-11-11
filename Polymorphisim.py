# duck typing
# method overriding
# method overloding
# operator overloding



# class Human:
#     def speak(self):
#         print("human can speak")

# class Robot:
#     def speak(self):
#         print("Robot can speak")

# class Dog:
#     def speak(self):
#         print("dog can bark")

# def call_to_speak(entity):
#     entity.speak()

# for creation in [Human(), Robot(), Dog()]:
#     call_to_speak(creation)

# print(Human().speak())



# class Animal:
#     def sound(self):
#         print("Geniric sound")

# class Dog(Animal):
#     def sound(slef):
#         print("Bark")

# class Cat(Animal):
#     def sound(self):
#         print("Meow")
        
# animal = [Dog(), Cat(), Animal()]

# for a in animal:
#     a.sound()


# class animal:
#     def sound(self):
#         print("sound1")

# class robot:
#     def sound(self):
#         print("sound2")

# class human:
#     def sound(self):
#         print("sound3")

# voice = [human(),robot(),animal()]

# for v in voice:
#     v.sound()


# class Math:
#     def add(self, a, b):
#         print(a+b)
#     def add(self, a,b,c):
#         print(a+b+c)
# obj = Math()
# obj.add(1,2,3)




# class Math:
#     def add(self,*args):
#         total = sum(args)
#         print(total)

# obj = Math()
# obj.add(1,2,3,4,5,4,3,2,1)


# print(5+6)
# print("5"+"6")
# print([1,2]+[3,4])


# ## duck method

# class Printer:
#     def work(self):
#         print("Printer is working")

# class Scanner:
#     def work(self):
#         print("Scanner is working")

# for device in [Printer(), Scanner()]:    ##1 way to do it
#     device.work()

# operate = [Printer(), Scanner()]       ##2nd way to do it

# for a in operate:
#     a.work()



# class CreditCard:
#     def make_payment(slef,amount):
#         print(amount)

# class PayPal:
#     def make_payment(self,amount):
#         print(amount)

# class UPI:
#     def make_payment(self,amount):
#         print(amount)

# def process_payment(payment_method,amount):
#     payment_method.make_payment(amount)

# for method in [CreditCard(),PayPal(),UPI()]:
#     process_payment(method,2834)



## over riding method

# class Shape:
#     def area(self):
#         print("area")

# class Circle(Shape):
#     def area(self):
#         print("PI * r **2")

# class Square(Shape):
#     def area(self):
#         print("side square")

# for shape in [Circle(),Square(),Shape()]:
#     shape.area()



# class vehicle:
#     def max_speed(self):
#         return 200
# class Bike(vehicle):
#     def max_speed(self):
#         return 180

# class Car(vehicle):
#     def max_speed(self):
#         return 150

# class Truck(vehicle):
#     def max_speed(self):
#         return 120

# def Show_Speed(vehicle):
#     print(vehicle.max_speed())

# for method in [Bike(),Car(),Truck(),vehicle()]:
#     Show_Speed(method)


# class Employe:
#     def info(self, *args):
#         print(args)

# details = Employe()
# details.info("Name: Aryan","Department: IT","Salary: Bhot Jada")


# class Employee:
#     def info(self, *args):
#         if len(args) == 1:
#             print(f"Name: {args[0]}")
#         elif len(args) == 2:
#             print(f"Name: {args[0]}, Department: {args[1]}")
#         elif len(args) == 3:
#             print(f"Name: {args[0]}, Department: {args[1]}, Salary: {args[2]}")
#         else:
#             print("Invalid Number of details provided")

# obj = Employee()
# obj.info("Aryan")
# obj.info("Aryan","Engineering")
# obj.info("Aryan", "Engineering",28934571)
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


#class MathUtils:

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


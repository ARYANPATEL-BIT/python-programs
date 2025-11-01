
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
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


## if you want to take an input inside a child class then we have to use super key word


# class Book:
#     def __init__ (self,title,author):
#         self.title = title
#         self.author = author
# class EBook(Book):
#     def __init__(self, title, author,file_size):
#         super().__init__(title,author)               ## if you want to take an input inside a child class then we have to use super key word
#         self.file_size = file_size

#     def display(self):
#         print(f"Author: {self.author} \nTitle: {self.title} \nfile size: {self.file_size}")
        
# ebook = EBook("Unknown","Aryan",75)
# ebook.display()




# class Commpany:
#     def __init__(self,company_name):
#         self.company_name = company_name

# class Employee(Commpany):
#     def __init__(self,company_name,employee_name):             ## if you want to take an input inside a child class then we have to use super key word
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


# c.speak()


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


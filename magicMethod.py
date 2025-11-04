# class Student:
#     def __init__(self,marks):
#         self.marks = marks
    
#     def __add__(self,other):
#         return self.marks + other.marks
    
#     def __gt__(self,other):
#         return self.marks > other.marks
    
# s1 = Student(90)
# s2 = Student(89)
# print(s1 + s2)
# print(s1 > s2)



# class Distance:
#     def __init__(self,kilometers,meters):
#         self.kilometers = kilometers
#         self.meters = meters

    
#     def __add__(self,other):
#         total_m = self.meters + other.meters
#         total_km = self.kilometers + other.kilometers + total_m // 1000
#         total_m = total_m % 1000
#         return Distance(total_km, total_m)
    
#     def __str__(self):
#         return f"{self.kilometers} km {self.meters} m"

# d1 = Distance(123,123)
# d2 = Distance(371,238)
# d3 = d1 + d2
# print(d3)



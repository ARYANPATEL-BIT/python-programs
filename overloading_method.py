# class Vector:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def __add__(self,other):
#         return Vector(self.x + other.x , self.y + other.y)
    
#     def __sub__(self,other):
#         return Vector(self.x - other.x , self.y - other.y)
    
#     def __mul__(self,other):
#         return Vector(self.x * other.x , self.y * other.y)
    
#     def __str__(self):
#         return(f"{self.x}, {self.y}")



# v1 = Vector(5,10)
# v2 = Vector(15,20)

# print("Addition:" ,v1 + v2)
# print("Subtraction:" ,v1 - v2)
# print("Multiplication:" ,v1 * v2)



class Distance:
    def __init__(self,km,m):
        self.km = km
        self.m = m
    
    def __add__(self,other):
        total_m = self.m + other.m
        total_km = self.km + other.km + total_m // 1000
        total_m = total_m % 1000
        return Distance(total_km , total_m)
    
    def display(self):
        print(f"Distance: {self.km} km and {self.m} m")


d1 = Distance(10, 1024)
d2 = Distance(7, 2048)

d3 = d1 + d2

d3.display()
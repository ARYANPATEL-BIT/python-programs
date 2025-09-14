num = int(input("Enter the number: "))
total = 0

while num > 0:
    a = num % 10
    total = 10*total+a
    num = num // 10
print(total)

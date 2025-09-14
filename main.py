# reversing an number
# num = int(input("Enter the number: "))
# total = 0

# while num > 0:
#     a = num % 10
#     total = 10*total+a
#     num = num // 10
# print(total)

#fibonacci series
# num = int(input("Enter an number"))
# a,b = 0,1
# for i in range(num):
#     print(a)
#     c =a+b
#     a=b
#     b=c

#reversing an number using for loop
# num = int(input("Enter an number: "))
# rev =""
# for i in str(num):
#     rev = i + rev 
# print(int(rev))

#palindrom number
# num = int(input("Enter an number: "))
# total = 0
# final = num
# while num > 0:
#     a = num % 10
#     total = total * 10 + a
#     num = num // 10

# if total == final:
#     print("The number is palindrom.")
# else:
#     print("The number is not palindrom.")

#count digit in a number
# num = int(input("Enter an number"))
# total = 0
# while num > 0 :
#     a = num % 10
#     total +=1
#     num = num // 10
# print(total)

#sum of the digits
# num = int(input("Enter an number:"))
# total = 0

# while num > 0:
#     a = num % 10
#     total += a
#     num = num // 10

# print(total)

#armstrong number
# num = int(input("Enter an number: "))
# a = len(str(num))
# n = num
# total = 0

# while num > 0:
#     b = num % 10
#     total = total + b**a
#     num = num // 10

# if total == n:
#     print("It's an Armstrong number")
# else:
#     print("It's not an Armstrong number")

#taking number until user enters zero and then printing the sum
# total = 0
# while True:
#     num = int(input("Enter an number: "))
    
#     if num == 0:
#         break
#     total += num


# print("the sum is", total)

#largest digit in an number
# num = int(input("Enter an number: "))
# total = 0

# while num > 0:
#     a = num % 10
#     if a > total:
#         total = a
#     num = num // 10
# print(total)

#vowel in an sentence
s = input("Enter an sentence: ")
vol = "aeiouAEIOU"
total = 0

for i in s:
    if i in vol:
        total += 1

print(total)
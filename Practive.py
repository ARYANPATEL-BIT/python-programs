# for i in range(1,6):
#     for j in range(1, i+1):
#         print("*",end=" ")
#     print()


# str1 = "Aryan Patel"
# for i in str1:
#     print(i)


# n =5
# num = 1
# for i in range(1,n+1):
#     num *= i
# print(num)


# n = 10
# a, b = 0 ,1 
# for i in range(n):
#     print(a,end=" ")
#     a,b = b, a+b

# n = 1234
# rev = 0
# while n > 0:
#     a = n % 10
#     rev = rev * 10 + a
#     n = n // 10
# print(rev)


# n = 122
# t = n
# rev = 0
# while n > 0:
#     a = n % 10
#     rev = rev * 10 + a
#     n = n // 10

# if rev ==  t:
#     print("is palindrome")
# else:
#     print("Not a palindrome")


# name = "Aryan Patel"
# count = 0
# for i in name:
#     if i == "a" or i == "A":
#         count += 1

# print(count)

# total = 0

# while True:

#     num = int(input())

#     if num == 0:
#         break

#     total += num

# print(total)


for num in range(2,101):
    is_prime = True

    for i in range(2,num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)
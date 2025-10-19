# i = 1
# while i <= 5:
#     print(i)
#     i +=1


# p = ""
# while p != "python":
#     p = input("enter the password: ")
# print("Exess Granted!")


# count = 0
# while count < 5:
#     count +=1
#     print("python")
# print(f"the loop has finised , count: {count}")


# for i in range(1,10):
#     if i == 5:
#         break
#     print(i)


# for i in range(1,10):
#     if i == 5:
#         continue
# #     print(i)


# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()    


# number = int(input("enter the number: "))
# for i in range(1, number + 1):
#     count = number - i
#     print(" " * count + "* " * i)

# sum of n natural number
# n = int(input("Enter an number"))
# sum = 0
# for i in range(1,n+1):
#     sum +=i
# print(sum)

# number = int(input("Enter an number: "))
# factorial = 1
# for i in range(1,number+1):
#     factorial *= i
# print(factorial)


# fabonacci = int(input("Enter an number: "))
# a,b =0,1
# for i in range(fabonacci):
#     print(a, end=" ")
#     a,b = b,a+b


# num = int(input("Enter an number:"))
# rev = 0
# while num > 0:
#     a = num % 10
#     rev = rev * 10 + a
#     num = num // 10
# print(rev)


# num = int(input("Enter an number:"))
# rev = 0
# num1 = num
# while num > 0:
#     a = num % 10
#     rev = rev * 10 + a
#     num = num // 10
# if num1 == rev:
#     print("is palindrom")
# else:
#     print("not an palindrom")


# num = int(input("Enter an number:"))
# count = 0
# while num > 0:
#     num = num // 10
#     count += 1
# print(count)


# num = int(input("Enter an number: "))
# sum = 0
# while num > 0:
#     a = num % 10
#     sum += a
#     num = num // 10
# print(sum)


# num = int(input("Enter an number: "))
# digits = len(str(num))
# count = 0
# num1 = num

# while num > 0:
#     a = num % 10
#     count = count + a**digits
#     num = num // 10
# if num1 == count:
#     print("is armstrong")
# else:
#     print("not armstrong")



# num = int(input("enter a number: "))
# sum = 0 

# while True:
#     if num == 0:
#         break

#     sum += num
#     num = int(input("enter a number: "))
# print(sum)


# num = int(input("enter an number: "))
# max = 0

# while num > 0:
#     a = num % 10
#     if a > max:
#         max = a
#     num = num // 10

# print(max)
    

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(i,",", end= " ")


# n = int (input())
# sum = 0
# for i in range(1,2*n,2):
#     sum += i
# print(sum)


# n = int(input())

# if n < 2:
#     print("n is not an prime number: ")
# else:
#     for i in range(2,n):
#         if n % i == 0:
#             break
#     else:
#         print(n)


# for num in range(2,101):
#     prime = True

#     for i in range(2,num):
#         if num % i == 0:
#             prime = False
#             break
#     if prime:
#         print(num, end=" ")


# year = int(input("Enter an number: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("leap year")
# else:
#     print("not a leap year")


# for num in range(2,101):
#     is_prime = True

#     for i  in range (2,num):
#         if num % i == 0:
#             is_prime =False
#     if is_prime:
#         print(num,end=" ")


# import random

# choices = ["rock","paper","scissors"]

# while True:

#     user = input("Enter rock , paper , scissors or quit")

#     if user == "quit":
#         break

#     if user not in choices:

#         print("invalid input")

#         continue

#     computer = random.choice(choices)

#     print = ("computer chose:", computer)

#     if computer == user:
#         print("its a tie")
#     elif (computer == "rock" and user == "paper") or ( computer == "paper" and user == "scissors") or ( computer == "scissors" and user == "rock") :
#         print("You win")
#     else: 
#         print("You loss")


# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end= " ")
#     print()


# for i in range(1,6):
#     print("*"*5)
# print()

# import random

# secret = random.randint(1,20)
# while True:

#     user = int(input())

#     if user == secret:
#         print("correct")
#     elif user  > secret:
#         print("guessed too high")
#     else:
#         print("guessed too low!")


# import random

# max_choice = 3


# while True:
   
#    user = int(input("enter an number"))
#    dice = random.randint(1,6)
#    if user == dice:
#       print("you win")
#    elif user != dice:
#       max_choice-=1
#       print("Try again")
#    if max_choice == 0:
#       print("you lose")
#       break


# def count(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for ch in text:
#         if ch in vowels:
#             count +=1
#     print(count)

# count("Hello world")


# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print()


scores = {"Ravi": 85, "Priya": 92, "Aman": 78, "Sneha": 95}
sorted_scores = sorted(scores, key = scores.get)
sorted_values = {k : scores[k] for k in sorted_scores}
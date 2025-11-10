import math
# print(math.sqrt(25))
# print(math.floor(5.4))
# print(math.ceil(4.3))
# print(math.factorial(7))
# print(math.sin(45))

# radius = 7
# area = math.pow(radius,2) * 3.14159
# print(area)

# print(math.floor(8.7))
# print(math.ceil(8.7))



import random


# num = random.randint(1,90)
# print(num)

# names = ["Death", "Human", "Martian", "Alien", "Aryan"]
# random.shuffle(names)
# print(names)

# print(random.choice(names))


import datetime


# now = datetime.datetime.now()
# print(now)

# date = datetime.date.today()
# print(now.year)
# print(now.month)
# print(now.day)
# print(date)



import Currency_converter


# print(Currency_converter.usd_to_inr(100))

# print(Currency_converter.inr_to_usd(2309845790))



import scientific_calc 

# print(scientific_calc.factorial(10))
# print(scientific_calc.power(10,2))
# print(scientific_calc.sqrt(25))
# print(scientific_calc.sin(45))



import scientific_calc as sc

# print(sc.factorial(10))
# print(sc.power(10,2))
# print(sc.sqrt(25))
# print(sc.sin(45))


import random 

# question = ["a", "b" , "c" , "d" , "e"]

# ask = random.choice(question)

# if(ask == "a"):
#     print('''Are you a human?
#           a) yes
#           b) no
#           c) maybe
#           d) who knows''')
#     ans = input("Enter your Choice: ").strip().lower()
#     if ans == "a":
#         print("correct")


# elif(ask == "b"):
#     print('''Who are you??
#           a) Human
#           b) Soul
#           c) Nhi Bataung
#           d) who knows''')
#     ans = input("Enter your Choice: ").strip().lower()
#     if ans == "b":
#         print("correct")
    
    
# elif(ask == "c"):
#     print('''Are you a Alien?
#           a) yes
#           b) no
#           c) maybe
#           d) who knows''')
#     ans = input("Enter your Choice: ").strip.lower()
#     if ans == "b":
#         print("correct")
    
    
# elif(ask == "d"):
#     print('''Are you a human?
#           a) yes
#           b) no
#           c) maybe
#           d) who knows''')
#     ans = input("Enter your Choice: ").strip().lower()
#     if ans == "a":
#         print("correct")
    
    
# elif(ask == "e"):
#     print('''How are you?
#           a) Badiya
#           b) teriffic
#           c) Never been better
#           d) Great, What about you?''')
#     ans = input("Enter your Choice: ").strip().lower()
#     if ans == "d":
#         print("correct")
    

# import random

# question = ["a", "b", "c", "d", "e"]
# ask = random.choice(question)

# if ask == "a":
#     print('''Are you a human?
#     a) yes
#     b) no
#     c) maybe
#     d) who knows''')
#     ans = input("Enter your Choice: ").strip().lower()
#     if ans == "a":
#         print("correct")

# elif ask == "b":
#     print('''Who are you??
#     a) Human
#     b) Soul
#     c) Nhi Bataung
#     d) who knows''')
#     ans = input("Enter your Choice: ").strip().lower()
#     if ans == "b":
#         print("correct")

# elif ask == "c":
#     print('''Are you an Alien?
#     a) yes
#     b) no
#     c) maybe
#     d) who knows''')
#     ans = input("Enter your Choice: ").strip().lower()
#     if ans == "b":
#         print("correct")

# elif ask == "d":
#     print('''Are you a human?
#     a) yes
#     b) no
#     c) maybe
#     d) who knows''')
#     ans = input("Enter your Choice: ").strip().lower()
#     if ans == "a":
#         print("correct")

# elif ask == "e":
#     print('''How are you?
#     a) Badiya
#     b) terrific
#     c) Never been better
#     d) Great, What about you?''')
#     ans = input("Enter your Choice: ").strip().lower()
#     if ans == "d":
#         print("correct")


quiz = [ 
    {
        "question1": "What are you?",
        "options": {
            "a": "Human",
            "b": "Animal",
            "c": "soul",
            "d": "dont know"
        },
        "answer":"c"

}]



selected_questions = random.choice(quiz)
print(selected_questions)
for key,value in selected_questions["options"].items():
    print(f"{key}: {value}")
user_answer = input("enter your options:(a/b/c/d)").strip().lower()
if user_answer == selected_questions["answer"]:
    print("correct")
else:
    print("Wrong Answer")
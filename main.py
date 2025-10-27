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
# s = input("Enter an sentence: ")
# vol = "aeiouAEIOU"
# total = 0

# for i in s:
#     if i in vol:
#         total += 1

# print(total)

# num = int(input("enter"))
# for i in range(num+1):
#     print("*"*i)

# num = int(input("Enter an Number"))
# for i in range (num):
#     for j in range (num):
#         print("*"*i,j)


#split,strip,replace,etc

# sentence = "Python is fun to learn"
# word = sentence.split()
# print(word)

# sentence = "apple","banana","grapes","orange"
# word = sentence.split(",")
# print(word)

# sentence = "python is fun to learn"
# word = sentence.split(".",2)
# print(word)

# email = "user1234@gmail.com"
# domain = email.split("@")
# print(domain)

# date = "13-09-2025"
# part = date.split("-")
# print("day",part[0])
# print("month",part[1])
# print("year",part[2])

# s = " hello world "
# word = s.strip()
# print(word)

# s = "***amazing***"
# print(s.strip("*"))

# s = "xyxyhello worldxyxy"
# print(s.strip("xy"))

# s = "aabaaHelloaaaba"
# print(s.rstrip("ab"))

# s = "apple,banana,cherry"
# s1 =s.strip()
# s2 =s1.split(",")
# print(s2)

# s = "apple ,banana,cherry"
# print(s.strip().split(","))

# s = "python is programming language"
# word = s.find("programming")
# print(word)

# s ="python programming"
# index = s.find("java")
# print(index)

# s = "learn , learn , learn"
# result = s.replace("learn","orange",1)
# print(result)



# s = "ABCDC CDC"
# sub = "CDC"
# count = 0
# pos = s.find(sub)
# while pos != -1:
#     count +=1
#     pos = s.find(sub,pos+1)

# print(count)

# s = "order1234"
# for d in "0123456789":
#     s = s.replace(d,"#")
# print(s)

#string methods

#lists

# list = ["apple", "banana","cherry"]
# list[1]="grapes"
# print(list)

#to add something in the last in a list

# list=[1,2,3,4,5]
# list.append(6)
# print(list)

# to add something at an specific place

# list = [1,3,5,7,9]
# list.insert(3,1)
# print(list)

# list = [1,2,3,4,5,6,7]
# list.pop
# print(list)

# list=[1,2,3,4,5,6,7]
# list.remove(3)
# print(list)

# list1 = [1,2,3,4,5]
# list2 = [2,3,4,5,6]
# list1.extend(list2)
# print(list1)

# list.sort()





# cart = ["milk","bread","butter","eggs"]
# cart.extend({"jam","cheese"})
# cart.insert(0,"honey")
# cart.remove("bread")
# cart.pop
# cart.sort()
# cart.count("milk")
# print(cart)




# marks = [89,56,92,75,56,92,100,67]
# marks.sort()
# s =marks[-2]
# print(s)
#  marks.remove(0)
# marks.extend({85,90})
# marks.reverse()
# print(marks)




# playlist =["song1","song2","song3","song4"]
# playlist.insert(0,"intro_song")
# playlist2 = ["song5","song6","song7"]
# playlist.extend(playlist2)
# playlist.remove("song3")
# del playlist[2]
# playlist.reverse()
# playlist.index("song5")
# print(playlist)

# marks = [45,67,89,90,56,23]
# marks.sort()
# print(marks)
# (marks.sort(reverse=True))
# print(marks)




# marks = [45,67,89,90,56,23]
# marks.sort
# min = marks[0]
# max = marks[0]
# for i in marks:
#     if i > max:
#         i = max
#     if i < min:
#         i = min
# print(min,max)

# count = 0
# for i in marks:
#     count += i
# print(count)

# total = 0
# for m in marks:
#     if m > 50:
#         total +=m
# print(total)




# inventory = ["pen","notebook","eraser","pen","marker","notebook"]
# print(inventory.count("pen"))

# unique = []
# for i in inventory:
#     if i not in unique:
#         unique.append(i)
# print(unique)



# inventory = ["pen","notebook","eraser","pen","marker","notebook"]
# unique = []
# for i in inventory:
#     if i not in unique :
#         unique.append(i)
# print(inventory)

# inventory.sort()
# print(inventory)



# nums = [12,7,9,21,14,18,3,28]
# num = []
# for i in nums:
#     if i %2 ==0:
#         num.append(i)
# print(num)

# nums = [12,7,9,21,14,18,3,28]
# nums.sort()
# second = nums[-2]
# print(second)

# print(nums.reverse)

# nums =[12,7,9,21,14,18,3,28]
# num = []
# for i in nums:
#     if i not in num:
#         num.append(i)
# num.sort(reverse=True)
# second_largest = num[1]



# nums = [5,7,5,9,7,5,9,7,7]
# max = 0
# frequency = 0
# for i in nums:
#     count = nums.count(i)
#     if  count > max:
#         max = count
#         frequency = i
# print(max)
# print(i)



# squares =[i**2 for i in range(1,6)]
# print(squares)


# nums =[1,2,3,4,5,6,7,8,912,14,1,31,51,16]
# even=[]
# for i in nums:
#     if i % 2 == 0:
#         even.append(i)
# print(even)



# words =["apple","banana","cherry"]
# upper = [w.upper for w in words]
# print(upper)

# words = ["pythons" , "java","css"]
# f = []
# for w in words:
#     f.append(f[0])
# print(f)


# words = ["pythons" , "java","css"]
# f=[w[0] for w in words]
# print(f)


# t1 = (1,2,3)
# print(10 in t1)
# print(20 not in t1)

# t =(1,2,3,4,5,6)
# print(max(t))
# print(min(t))
# print(len(t))

# count , index

# t =(1,2,3,4,5,6)
# print(t.count(3))
# print(t.index(1))

# t = ("Aryan",20,"Math")
# name,age,subject = t
# print(name)
# print(age)
# print(subject)


# t1 = (10,20,30,40)
# a,b,*args = t1
# print(a)
# print(b)
# print(args)


# fruits = ("apple","banana","mango","grapes")
# if "apple" in fruits:
#     print("yes applw is present")
# else:
#     print("apple is not present")

# t = (4,6,2,6,7,4,9,2,6)
# duplicates = []
# for i in t:
#     if t.count(i)>1 and i not in duplicates:
#         duplicates.append(i)
# print(tuple(duplicates))


# t1 = (1,2,3,4,5,6)
# t2 = (4,5,6,7,8,9)
# intersect = []
# for i in t1 :
#     if i in t2 and i not in intersect:
#         intersect.append(i)
# print(intersect)


# t = (1,2,3,7,8,9,5,5)
# pairs=[]
# for i in range(len(t)):
#     for j in range(i+1,len(t)):
#         if t[i]+ t[j] == 10:
#           pairs.append((t[i],t[j]))
# print(pairs)

# d = {
#     101 : 20,
#     102 : 30,
#     103 : 40
# }
# print(d)


# students ={
#     "name" : "Aryan",
#     "age": "20",
#     "subject":"maths",
#     "marks":"100"
# }
# for k in students:
#     print(k)
# for v in students.values():
#     print(v)
# for i in students.items():
#     print(i)


# marks = {"ravi": 85 , "Aryan": 100 , "Aditya":100}
# print(marks["ravi"])
# print(marks["Aryan"])
# print(marks["Aditya"])

# student ={
#     "name":"ravi",
#     "marks":86
# }
# student["city"] = "delhi"
# student["marks"] = 90
# print(student)
# removed = student.pop("city")
# print(student)

# sentence = "apple banana apple orange banana apple".split()
# freq = {}

# for w in sentence:
#     freq[w] = freq.get(w, 0) + 1 

# for fruit, count in freq.items():
# #     print(fruit, count)

# students = {
#     "Ravi": {"math": 80, "science": 70, "english": 90},
#     "priya": {"math": 85, "science": 95, "english": 92},
#     "aman": {"math": 60, "science": 65, "english": 70}
# }

# total_marks = 0
# num_subject = 0
# for subjects in students.values():
#     for marks in subjects.values():
#         total_marks += marks
#         num_subject +=1
# average = total_marks/num_subject
# print(average)

#find total marks of each students

# for name,subjects in students.items():
#     total = 0
#     for marks in subjects.values():
#         total += marks
#     print(name,total)

#find average marks of each students

# for name,subjects in students.items():
#     total = 0
#     count = 0
#     for marks in subjects.values():
#         total+=marks
#         count +=1
#         average = total/count
#     print(name,average)


# max_marks = 0
# topper = ""
# for name,subjects in students.items():
#     total = sum(subjects.values())
#     if total > max_marks:
#         max_marks = total
#         topper = name
# print(topper,max_marks)


# min_marks = None
# opper = ""
# for name,subjects in students.items():
#     total = sum(subjects.values())
#     if total < max_marks:
#         min_marks = total
#         opper = name
# print(opper,min_marks)

####
# min_marks = 0
# lowest = ""
# for name,subjects in students.items():
#     total = sum(subjects.values())
#     if min_marks is None or total < min_marks:
#         min_marks = total
#         lowest = name
# print(lowest,min_marks)

# total_marks = 0
# for subjects in students.values():
#     for marks in subjects.values():
#         total_marks += marks
# print(total_marks)

# marks = 0
# names = ""
# for name,subjects in students.items():
#     total = sum(subjects.values())
#     if marks <= 70:
#         names = name
# print(names)

# d = {"a":1, "b":2, "c":1, "d":3}
# unique = {}
# for k,v in d.items():
#     if v not in unique.values():
#         unique[k] = v
# print(unique)


# set questions

# s = set("Hello")
# print(s)

# s = set([1,2,3,4])
# print(s)

# s = set((1,2,3,4,5))
# print(s)

# s = set(range(5))
# print(s)

# s = {"apple","mango","banana"}
# s.add("cherry")
# print(s)

# s = {1,2,3,4}
# s.update([4,5])
# print(s)

# s = {1,2,3,4,5,4,3,4,3,4,5}
# print(len(s))

# a = {1,2,3,4,5,6}
# b = {1,2,3,4,5,6,7,8,9}
# print(a.union(b))
# print(a|b)

# s1 = { 7,8,9}
# s2 = { 8,9,4}
# print(s1&s2)
# print(s1.intersection(s2))


# a = {1,2,3,4}
# b = {2,3,4,5,6}
# print(a-b)

# x = {1,2}
# y = {1,2,3}
# print(x.issubset(x))


# x = {1,2,6}
# y = {1,2,3}
# print(x.issuperset(y))

# x = {1,2,3}
# y = {4,5,6}
# print(x.isdisjoint(y))

# fruit = {"apple","banana","cherry"}
# print(fruit)

# list = [1,2,3,4,5,6,4,3,2]
# print(set(list))

# set = {"red","green"}
# set.add("blue")
# set.remove("red")
# print(set)

# a = {1,2,3}
# b = {3,4,5}
# print(a.union(b))
# print(a.intersection(b))
# print(a-b)
# print(a^b)

# a = {1,2}
# b = {1,2,3}
# print(a.issubset(b))
# print(b.issuperset(a))

# words = ["apple","grape","maple"]
# s1 = set(words[0])
# s2 = set(words[1])
# s3 = set(words[2])

# print(s1&s2&s3)


# words = ["apple","grape","maple"]
# common_char =set(words[0])
# for word in words[1:]:
#     common_char&= set(word)
# print(common_char)


# n = int(input("enter the number: "))
# for i in range (1,n+1):
#     for j in range (1, i+1):
#        print(j , end ="")
#     print()


# list1 = [1,2,3,4]
# list2 = [2,3,4,5]
# list3 = [3,4,6]

# a = set(list1)&set(list2)&set(list3)
# print(a)

# b = set(list1)|set(list2)|set(list3)
# print(b)

# remove the same frequency

###
# data =[(1,"a"),(2,"b"),(1,"c"),(3,"d"),(2,"e")]
# seen = set()
# list = []
# for i in data:
#     if i not in seen:
#         list.append(i)
#         seen.add(i[0])
# print(seen)



# data =[(1,"a"),(2,"b"),(1,"c"),(3,"d"),(2,"e")]
# freq ={}
# for i in data:
#     num = i[0]
#     if num in freq:
#         freq[num]+=1
#     else:
#         freq[num] = 1
# result = []
# for i in data:
#     num = i[0]
#     if freq[num] ==1:
#         result.append(i)
# print(result)


# words = ["apple","orange","grape"]
# vowels = set('aeiou')
# a =set()
# for i in words:
#     a.update(set(i)&vowels)
# print(a)
# print(len(a))


# words = ["education","sequoia","algorithims","beautiful"]
# vowels = set('aeiou')
# a = []
# for word in words:
#     if vowels.issubset(word):
#         a.append(word)
# print(a)


# def numbers(li):
#     num = []
#     for i in li:
#         if i %2 ==0:
#             num.append(i**2)
#     print(num)

# print(numbers([1,2,3,4,5,6,7,8,9,8,7,76,5,4,3,2,1]))

##########
# def multiplication(size):
#     num = []
#     for i in range(1,size+1):
#         row =[]
#         for j in range(1,size+1):


# def func(li1,li2):
#     list = []
#     for i in li1:
#         if i in li2:
#             list.append(i)
#         return list
# a = set {list}


# def group(words):
#     result={}
#     first = words[0].lower()
#     if first not in result:
#         result[first] = set()
#     result[first].add[words]
#     result


# file = open("sample.txt","r")
# content = file.read()
# print(content)
# file.close

# file = open("sample.txt","w")
# file.write("hello world")
# file.write("\nI am the Best!")


# file=open("sample.txt","a")
# file.write("\n I am the smartest")
# file.close

# file = open("sample.txt","r")
# print(file.read())


# readline()
# file = open("sample.txt","r")
# print(file.readline())
# print(file.readline())
# print(file.readline())


#readlines()
# file = open("sample.txt","r")
# print(file.readlines())

# writeline()

# file = open("sample.txt","w")
# file.write("i am the greatest")

# writelines()
# file =open("sample.txt","w")
# file.writelines(["I am the greatest\n","I will Win"])

# with open("sample.txt","r") as file:
#     content = file.read()
#     print(content)


# file = open("sample.txt","w")
# file.writelines(["Aryan\n","God\n","iathaar\n","aditya\n","ayaan\n"])

# file = open("sample.txt","r")
# a = file.readlines()
# file.close
# b = a.split()
# lines = 0
# letters = 0
# for i in b :
#     lines +=1
#     for j in i:
#         letters +=1
    
# print("total lines:",lines)
# print("total words:",letters)
    

# file = open("sample.txt","r")
# lines = file.readlines()
# file.close()
# num_lines = len(lines)
# num_words = sum(len(line.split()) for line in lines)
# print(num_lines)
# print(num_words)

# file = open("sample.txt","r")
# a = file.read()
# file.close
# words = a.split()
# word_freq ={}
# for i in words:
#     if i in word_freq:
#         word_freq[i] +=1
#     else:
#         word_freq[i] =1
# print(word_freq)
# print(i)



# def sign(num):
#     if num == 0:
#         print("0")
#     elif num > 0:
#         print("1") 
#     elif num < 0:
#         print("-1")




# t = (9,1,2,3,4,5,6,7,7,6,5,4,3,2,1)

# unique =[]
# for i in range(len(t)):
#     for j in range(i+1, len(t)):
#         if t[i] + t[j] == 10:
#             unique.append((t[i] , t[j] ))
# print(unique)


# exception handaling / Error Handaling

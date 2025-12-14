
# friends = ["Aryan\n","Krishna\n","Unknown\n","Known\n","Human\n"]

# with open("sample_file.txt","w") as file:
#     file.writelines(friends)
#     file.close()

# print("Friends saved in sample_file.txt")


# with open("sample_file.txt", "r") as file:
#     lines = file.readlines()
#     file.close()

# num_lines = len(lines)
# num_words = sum(len(line.split()) for line in lines)

# print("Number of Lines:",num_lines)
# print("Number of Words:",num_words)


# with open("sample_file.txt" , "r") as file:
#     text = file.read()
#     # file.close()

# words = text.split()

# word_freq = {}

# for word in words:
#     if word in word_freq:
#         word_freq[word] += 1
#     else:
#         word_freq[word] = 1

# for word , freq in word_freq.items():
#     print({f"{word}:{freq}"})


# with open("sample_file.txt" , "r" ) as file:
#     text = file.read()
#     file.close()

# words = text.split()
# word_freq = {}

# for word in words:
#     if word in word_freq:
#         word_freq[word] += 1
#     else:
#         word_freq[word] = 1

# for word , freq in word_freq.items():
#     print({f"{word}:{freq}"})



# with open("fruits.txt" ,"w") as file:
#     fruits = file.writelines(["Apple\n","Banana\n","Kiwi\n","Mango\n","cherry\n"])
#     file.close()

# with open("fruits.txt","r") as file:
#     lines = file.readlines()

# for line in lines :
#     fruit = line.strip()
#     if fruit.startswith("a") or fruit.startswith("A"):
#         print(fruit)


with open("Numbers.txt","w") as file:
    numbers = file.writelines(["1\n","2\n","3\n","4\n","5\n"])
    file.close()

with open("Numbers.txt","r") as file:
    numbers = file.readlines()
    file.close()

total = 0

for line in numbers:
    number = int(line.strip())

    total += number

print(total)
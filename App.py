from math import *

# name = "Amir"
# print(f"Hi {name}")
 
# print (name.index("i"))
# print (name.replace("m", "t"))

# print(type((name)))

# print (max(2,25,3,24,66,5))
# print (min(2,25,3,24,66,5))
# print (round(3.2))
# print (bin(334))
# print (sqrt(100))

# first_name = input ("Enter your name: ")
# age = int(input("Enter your age: "))
# print (type(age))
# print(f"Your name is {first_name} and Your age is {age}")




# Word replacement program 
# sentence = input ("Enter your sentence: ")
# print (f"Your sentence is: {sentence}")
# first_word = input ("Enter a word to replace: ")
# second_word = input ("Enter the word to replace with: ")

# print (sentence.replace (first_word, second_word))

# Lists 
# countries = ["UK", "Ghana", "Iran", "India"]
# stuff = ["UK", "Egypt"]
# numbers = [100,9,43,24,95,64,43,2]

# stuff.append("France")
# stuff.insert(1,"England")
# stuff.remove("UK")
# # stuff.clear()
# print (stuff.count("Egypt"))
# numbers.sort()
# print(numbers)
# numbers.reverse()
# print(numbers)
# numbers.pop()
# print(numbers)


# countries.extend(stuff)
 
# print(countries)



# # Tuples 


# three_numbers = (1,2,3)
# print(type(three_numbers))


# def greetings_function(name, age):
#     print(f"HI {name} you are {age}")


# greetings_function("Gholi", 26)



# def men_function(name, age):
#     print(f"HI {name} you are {age}")

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# men_function(name, age)


# number = int(input("Enter a Number: "))

# if number % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd number")

# Dictionaries
# print("Hi")
# my_dict = {
#     "name": "Gholi",
#     "age" : 26, 
#     "nationality" : "Iranian",
#     "friends" : ["Peter", "Gholi" ]
# }

# x = my_dict["name"]
# print(x)
# print(my_dict)

# while loop 
# i = 1
# m = 6
# while i <= 6 and m == 6:
#     print(i)
#     i +=1
    


# for loops 
# my_list = ["Ali", "Gholi", "Changiz"]
# dict = ["Ali", "Gholi", "Changiz"]


# for values in dict:
#     print(values)
    
    
# for x in range(4):
#     print(x)
# else:
#     print("Looping is finished")

# 2d list in python 

# my_list = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# for lists in my_list:
#     for row in lists:
#        print(row)




# num_1 = int(input("Enter the first number: "))
# num_2 =int( input("Enter the second number: "))
# operator = input("Enter operator")  

# if operator == "+":
#     print(num_1 + num_2)
    
# elif operator == "-":
#     print(num_1 - num_2)
    
# elif operator == "*":
#     print(num_1 * num_2)
    
# elif operator == "/":
#     print(abs(num_1 / num_2))
# else: 
#     print("Invalid operator")
    
# # Try except in python 
# try: 
#     x = int(input("input an integer :"))
#     print(x)
    
# except ValueError: 
#     print("HeHe That s wrong")

# else:
#     print("you did it")
    
# finally:
#     print("Try except finished")


file = open("countries.txt", "r")

print(file.read())

file.close()
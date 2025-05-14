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
countries = ["UK", "Ghana", "Iran", "India"]
stuff = ["UK", "Egypt"]
numbers = [100,9,43,24,95,64,43,2]

stuff.append("France")
stuff.insert(1,"England")
stuff.remove("UK")
# stuff.clear()
print (stuff.count("Egypt"))
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers.pop()
print(numbers)


countries.extend(stuff)
 
print(countries)



# Tuples 


# three_numbers = (1,2,3)
# print(type(three_numbers))


# def greetings_function(name, age):
#     print(f"HI {name} you are {age}")


# greetings_function("Gholi", 26)



def men_function(name, age):
    print(f"HI {name} you are {age}")

name = input("Enter your name: ")
age = input("Enter your age: ")
men_function(name, age)

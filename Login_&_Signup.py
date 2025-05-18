user_name = input("Enter your name: ")
password = input("Enter your password: ")

print("Your Account has been created successfully")
print("You can login now")

user_name_2 = input("Enter your name: ")
password_2 = input("Enter your password: ")

if user_name == user_name_2 and password == password_2:
    print("Logged in successfully")
else:
    print("Invalid Information")
"""
Day 2 - Input, Variables & Conditions

Today I learned:
- User input
- Type conversion
- Variable naming rules
- If / elif / else
- Logical operators
- Basic algorithms
"""

# num1 = int (input("Enter a number"))
# num2 = int (input("Enter another number"))

# #num1 = "111" -> 111
# #num2 = "222" -> 222

# result = num1 + num2

# # result = "111" + "222" = 111222 # string concatination

# #ask kilometer value from user and convert it to meters
# #1 kilometer = 1000 meters

# km_value = float(input("Enter distance in kilometers: "))

# m_value = km_value * 1000
# # print(km_vaue, "kilometers is equal to", m_value, "meters.")

# print(f"{km_value} kilometers is equal to {m_value} meters.")

# Rules for naming variables

#1[Strict]. variable name should not start with a number

# num1 = 90
# _1num = 100

# 2[Standard]. variable name should be meaningful
 
# english = 5
# math = 10

# a = 1
# b = 2

# 3[Standard]. variable name ,ust be single word, no space allowed, use snake_case or camelCase or PascalCase

# english_full_marks = 5 -> snake_case
# englishFullMaeks = 6 -> camelCase
# EnglishMarks = 7 -> PascalCase


# 4[Strict]. variable name should not be a keyword or built-in function name

# if = 10 # wrong

# determine if user is allowed to apply for citizenship or not 

##Algorithm
# step 1: what is your age? => 16
# step 2: check if user's is greater than or equal to 18 ?
# step 3: if yes, user is eligible to apply for citizenship card
# step 4: if no, user is currently not eligible to apply for citizenship card

#ex.com/admin/dashboard
# user_role = "admin"

# age = int(input("Enter your age (eg. 20): "))

# if age >= 18:
#     print("You are eligible to apply for citizenship card.")
#     print("Congratulations!")
# else:
#     print("You are currently not eligible to apply for citizenship card.")
#     print("Please try again after some time.")

# print("Thank you for using our service.")


# Calculate grade based on user entered marks

# Step1: Ask user obtained marks
# Step2: Check if marks >= 90, then grade = A+
# Step3: Check if marks >= 80, then grade = A
# Step4: Check if marks >= 70, then grade = B+
# Step5: Check if marks >= 60, then grade = B
# Step6: Check if marks >= 50, then grade = C+
# Step7: Check if marks >= 40, then grade = C
# Step8: Check if marks >= 30, then grade = D+
# Step9: Check if marks >= 20, then grade = D
# Step10: Check if marks >= 10, then grade = E
# Step11: Check if marks >= 0, then grade = NG

# marks = float(input("Enter your obtained marks (eg. 85): "))

# if marks > 100:
#     print("Invalid marks entered. Please enter a valid number between 0 and 100.")
# elif marks >= 90:
#     print("Your grade is: A+")
# elif marks >= 80:
#     print("Your grade is: A")
# elif marks >= 70:
#     print("Your grade is: B+")
# elif marks >= 60:
#     print("Your grade is: B")
# elif marks >= 50:
#     print("Your grade is: C+")
# elif marks >= 40:
#     print("Your grade is: C")
# elif marks >= 30:
#     print("Your grade is: D+")
# elif marks >= 20:
#     print("Your grade is: D")
# elif marks >= 10:
#     print("Your grade is: E")
# elif marks >= 0:
#     print("Your grade is: NG")
# else:
#     print("Invalid marks entered. Please enter a valid number between 0 and 100.")


## improved version of the above code

# marks = float(input("Enter your obtained marks (eg. 85): "))

# # if marks > 100 = invalid
# # if marks < 0 = invalid
# # or ->

# if marks > 100 or marks < 0:
#     print("Invalid marks entered. Please enter a valid number between 0 and 100.")
# elif marks >= 90:
#     print("Your grade is: A+")
# elif marks >= 80:
#     print("Your grade is: A")
# elif marks >= 70:
#     print("Your grade is: B+")
# elif marks >= 60:
#     print("Your grade is: B")
# elif marks >= 50:
#     print("Your grade is: C+")
# elif marks >= 40:
#     print("Your grade is: C")
# elif marks >= 30:
#     print("Your grade is: D+")
# elif marks >= 20:
#     print("Your grade is: D")
# elif marks >= 10:
#     print("Your grade is: E")
# elif marks >= 0:
#     print("Your grade is: NG")



# and .>

english = 42
math = 50
science = 30

# pass ?? english >= 40 , math >= 40

# if english >= 40 and math >= 40:
#     print("You have passed the exam.")

# # fail ?? english < 40 , math < 40 , science < 40

# if english < 40 or math < 40 or science < 40:
#     print("You have failed the exam.")



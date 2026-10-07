# Today's topic: Conditional Statements, Part 1 (if, else, elif)
# # what is a conditional statement 
# lets your program make a desion it checks 
# a condition and runs some code only id that conditions ind true

# if condition :
# runs only when the condition is true
#else:
# runs when the condition is false

# Indentation is how the python knows which lines are inside the if else has no cindition it catches everything the if didn't
'''
# Example
age=20
if age>=17.9:
    print("you can vote")
else:
    print("you canno't vote")

#
marks = int(input("Enter your marks: "))

if marks >= 75:
    print("Grade A")
elif marks >= 50:
    print("Grade B")
elif marks >= 35:
    print("Grade C")
else:
    print("Fail")

print("Done")

##  Practice

age=int(input("enter your age :"))
if age>=18:
    print("Adult")
else:
    print("Minor")
#######
# 2
number=int(input("enter a number : "))
if number>0 :
    print("Positive")
elif number <0 :
    print("Negative")
elif number == 0:
    print("Zero")
else:
    print("check your input ")

## 3
number=int(input("enter a number :"))
if number%2==0:
    print("Even")
else:
    print("Odd")
##
temperature=int(input("enter a number in temperature :"))
if temperature>35:
    print("Hot")
elif 20 <=temperature <= 30:
    print("warm")
elif 10 <=temperature <= 20:
    print("Cool")
elif temperature<10:
    print("cold")
## 5

score = int(input("Enter score: "))
#if score = 50: #here is = means assinging a value tovariable == to means comparing a value to another value
#print("Pass")  # here is an error print statement has some gap from stating line 
#else  #here is and missing :
#print("Fail")  # here is an error print statement has some gap from stating line 
# without bug 

score = int(input("Enter score: "))
if score == 50:
   
   print("Pass")
else:
    print("Fail")

##  end of the  day 
"""
What does an if statement do? Why do programs need it?
Why does Python need indentation? What happens if you forget it? (Try it and send me the error.)
What is the difference between several separate if statements and one if with elif? (Hint: think about what happens with marks = 90 in Example 2 if every line were a separate if.)
When does the else block run?
In Example 2, what would the output be if the user entered 35? And 34?
"""
# if statement can check the condition of the give problem is true of false python runs the code in indide the if loop block and line by line
# python use indentation to know which code belongs insoide th if block 
# if you forgot the indentation it gives IndentationError: expected an indented block after 'if' statement
# if can check the condtion and if it is false it goes to elif and print what we written in elif Here Python checks from top to bottom.
#The else block runs when none of the previous conditions are true.The else block runs when none of the previous conditions are true.
#Assuming Example 2 is the usual age/range example:
age = int(input("Enter your age: "))

if age >= 35:
    print("You can apply")
else:
    print("You cannot apply")
#If the user enters:35
#35 >= 35 True



#
#1. What does an if statement do?

#An if statement lets the program make a decision. It checks a condition, and if that condition is true, Python runs the code inside the if block.
age = 20

if age >= 18:
    print("Adult")
#Why does Python need indentation?

#Python uses indentation to know which code belongs to an if, elif, or else block.

#If I forget the indentation:
age = 20

if age >= 18:
#print("Adult") #IndentationError: expected an indented block after 'if' statement
#


    print("Adult")
#Separate if statements vs if + elif

#Several separate if statements are all checked independently.
marks = 90

if marks >= 50:
    print("Pass")

if marks >= 80:
    print("Very Good")

if marks >= 90:
    print("Excellent")
#I don't have the exact Example 2 code in your message, so I don't want to invent its output.
age = int(input("Enter your age: "))

if age >= 35:
    print("You can apply")
else:
    print("You cannot apply")

# Day 7 - If / Elif / Else Practice


# Exercise 1
# Ask for the user's age.
# Print Adult if age is 18 or more, otherwise Minor.

age = int(input("Enter your age: "))

if age >= 18:
    print("Adult")
else:
    print("Minor")


# Exercise 2
# Ask for a number.
# Positive if greater than 0
# Negative if less than 0
# Zero otherwise

number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Exercise 3
# Ask for a number.
# Print Even or Odd.

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Exercise 4
# Temperature:
# Above 35       -> Hot
# 20 to 35       -> Warm
# 10 to 19       -> Cool
# Below 10       -> Cold

temperature = int(input("Enter temperature in °C: "))

if temperature > 35:
    print("Hot")
elif 20 <= temperature <= 35:
    print("Warm")
elif 10 <= temperature <= 19:
    print("Cool")
else:
    print("Cold")
'''
#######
marks =int(input("enter a number : "))

if marks >= 50:
    print("Pass")

if marks >= 80:
    print("Very Good")

if marks >= 90:
    print("Excellent")
# it print according to the marks input u given for example id i entered 90 excellent and id u entered 78 id pass and id 89 very good
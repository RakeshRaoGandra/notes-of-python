#Today's topic: Operators, Part 2 (comparison, logical, and operator precedence)
# Comparison operators compare two values and give back a bool, which is True or False. You already used one on Day 5 when you wrote n % 2 == 0.
#Why is it useful? Programs make decisions. "Is the age at least 18?" "Is the password correct?" These all start as a comparison. Tomorrow's topic, if statements, depends completely on today's.
# Comparison operators, which answer yes/no questions about values
#Logical operators, which combine yes/no answers
#Operator precedence, meaning which operator Python does first
"""
Comparison operators

Operator	Meaning  	              Example	        Result
==	        equal to	               5 == 5	         True
!=	         not equal to	           5 != 3	         True
>	         greater than	          5 > 8	              False
<	         less than	              5 < 8	              True
>=	      greater than or equal to	  5 >= 5	         True
<=	       less than or equal to	  5 <= 3	         False

The most common beginner mistake: = and == are different.
= stores a value: age = 18
== asks a question: age == 18 (is age equal to 18?)


Logical operators

Logical operators combine True/False answers.

Operator 	Meaning	                                 Example	             Result
and	         True only if both sides are True	     5 > 3 and 2 > 1	      True
or	          True if at least one side is True   	5 > 3 or 2 > 9	      True
not	        flips the answer	                     not True	        False


Operator precedence

Precedence means which operator Python does first, like BODMAS in maths. From first to last:

( ) brackets
**
*, /, //, %
+, -
comparisons (==, !=, >, <, >=, <=)
not
and
or

Example: 2 + 3 * 4 gives 14, not 20, because * goes before +. If you want the addition first, use brackets: (2 + 3) * 4 gives 20. When unsure, use brackets. They also make your code easier to read.



"""

# Example 1
age = 20
print(age >= 18)
print(age == 30)
print(age != 30)

#Example 2
marks = 72
attendance = 80

passed = marks >= 40
good_attendance = attendance >= 75

print("Passed:", passed)
print("Eligible for exam:", passed and good_attendance)
print("Needs help:", not passed or not good_attendance)

print(2 + 3 * 4)
print((2 + 3) * 4)
print(10 > 5 and 3 > 1 or 1 > 5)

## 
## Practice
# 1
print(7 > 3)  # here 7 is greater than the 3 yes  so true
print(7 == 3) # here the seven eqlal to 3 no 7==3 not same 7 and 3 so false
print(7 != 3) # seven not equal to 3 so true 
print("apple" == "Apple") # false because in python is case censitive it takes captial and small letters as different
print(10 <= 10) # here they tell that lees than or equal so two condition's so true

# 2 Ask the user for their age. Print True or False for each: is the age at least 18? Is the age less than 60?
age=int(input("enter your age : "))
print(age<=918)
print(age<60)
#3
print(True and False) # False  here we using  and so both must be true like both conditons
print(True or False) # True # in or operatoer only one condtion be true or both or true

print(not False)  # true #  not reverses the boolean value
print(5 > 2 and 8 < 4) # False # here 5 is greater than 2 true and 8 is lessthan 4  false so whle using the and operatoe both conditions must be true
print(5 > 2 or 8 < 4) # true #here one condition is true the ans is true is or operatoer

#4
print(3 + 4 * 2) 
# output 11 is here we follow the BODMAS rule first mulitfication first so 4*2=8 and 8+3 =11 
print((3 + 4) * 2)
# output is 14 here we follow the BODMAS rule here fisrt solve the brackets so 3+4 =7 and 7*2 =14
print(2 ** 3 + 1)
# output  is 9 here we follow the BODMAS rule here first 2**3 is 8 and +1 =9
print(10 - 4 - 2)
# output is 4 here we follow the BODMAS rule 10-4=6 and 6-2 =4 

# 5
number = int(input("Enter a number: "))

print(number % 2 == 0)
print(10 <= number <= 50)
print(number % 2 == 0 and 10 <= number <= 50)

# end of the day
# here = means assigning a value to variable with =
# == means comparing a vaalue with dofferent value like 3==3 is true and 3==4 false like this comprassion
x = 10       # assign 10 to x

x == 10      # check if x is equal to 10 → True
# when the comparison is happen between two numbers it gives true or false
#example
#10 > 5 gives true

# a nd b are true means both conditiond are pass like 2==2 and 2<3
# in or only one condition well be true it gives the value 
# it follows the BODMAS rule fisrst 2*3 =6 and after 6+5 =11
# not (5>3) do give that if it is true it gives the false so here false

# 1. Fixed Exercise 2

# Age = 10
age = 10
print(age >= 18)   # False
print(age < 60)    # True

# Age = 18
age = 18
print(age >= 18)   # True
print(age < 60)    # True

# Age = 70
age = 70
print(age >= 18)   # True
print(age < 60)    # False


# 2. Real-life examples

# AND
# I can take an exam if I have paid the fee AND have good attendance.
paid_fee = True
good_attendance = True
print(paid_fee and good_attendance)   # True

# OR
# I can travel if I have a bus ticket OR a train ticket.
bus_ticket = False
train_ticket = True
print(bus_ticket or train_ticket)     # True


# 3. Rewrite 5 + 2 * 3 to add first

print((5 + 2) * 3)
# Answer: 21


# 4. AND version of 10 <= number <= 50

print(number >= 10 and number <= 50)










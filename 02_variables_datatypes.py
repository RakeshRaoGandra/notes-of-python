# syntax for the variable's
# variable_name=value
# = means store this value in this name
# id a variable name is 2name is wrong name of the variable
# use only first letters after that number's underscore 
# variables are the case sensitive like age and Age 
# dont use of such words like print if for they are functions 

#example 1
name="rakesh"
print(name)

# example 2
student_name="rakesh"
marks=80
bonus=5
print(student_name)
print(marks)
print(marks+bonus)
marks=90
print(marks)

print("Marks:",marks)

#Practice
# create a variable name with your name and city 
name = "rakesh"
city="Karimnagar"
print(name)
print(city)
#2
price=50
quantity=4
print(price,quantity)
print(price*quantity)

#3
score=10
print(score)
score=25
print(score)
print(score+5)# here the score is 25 we add by the 5 so 30 here addition 
#
#4 find mistakes

 #  2name = "Rakesh"  #here id the error because of a variable cannot start with number
#
 #  my age = 25 # in ths space is there so space  gives error
#   print(Name)  # case sensitive letters are

#Programs\Python\Python314\python.exe c:/Users/gandr/Documents/notes-of-python/day2.py
#  File "c:\Users\gandr\Documents\notes-of-python\day2.py", line 21
  #  2name = "Rakesh"  #here id the error because of a variable cannot startwith number
#IndentationError: unexpected indent
#PS C:\Users\gandr\Documents\notes-of-python> 


#5
product_name = "pen"
product_price= 10
quantity=34
print(product_name,product_price*quantity)

# what are the variables
# variables are likea a block where we store a value that are numbers strings etc and after that we use to use that variable to find the answers
# print(name),it print the variable value that we store in the name 

#print("name ") it print the name because of the it is a print wheren ever we write in " " in ths it print the what is inside 
# 1student ,my name because of the variable cannot start with the number and no space between the variables are defining

# = meansassiginig a value in variable
# in ths x=5,x=8
# it print's 8 becaue the updated x=8


score =25
print(score+5)
print(score)

#Then write a line that makes score actually become 30, using =. Here is a hint on how Python reads it: it works out the
#  right side first, then stores the result in the name on the left. Print score afterwards to prove it changed.

##

product_name = "Pen"
product_price = 10
quantity = 3

print("Product:", product_name, "Price:", product_price, "Quantity:", quantity)


score =25
print(score+5)

#

score =25
print(score+5)  # expected oup is 30 because of the 
#Python always works out the right side first, using the value x has at that moment.
#Then it stores the result back in the name on the left.
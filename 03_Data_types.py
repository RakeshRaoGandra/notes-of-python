# Today topc is Data Types
# why data type's
# every value in python has a kind and that kind
# is its data type like numbers,text,true,false etc..
# Types of the data types 
#  int  whole number are 23.234.-2,-123,0
# float number with decimal value 2.32.,-09.23,10.00
# str text form like names even numbers also "23","rakesh",
# bool true or false 
# None nothing or no value ex :  none
 # syntax type (value)

#Example
age=23
print(type(age))

# example
name = "Rakesh"
age = 25
height = 5.8
is_student = True
phone = None

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
print(type(phone))


#Type conversion means changing a value from one data type to another data type
# Example for the conversion's

age = 25 # int to string
age=str(age)
print(age)
print(type(age))

age = input("Enter your age: ")

print(type(age))

age = int(input("Enter your age: "))

print(age + 1)

#  anothere example
age_text = str(age)
print(age_text, type(age_text))

price_text = "100"  # here str to int
price_number = int(price_text)
print(price_number + 50)

#Two things that surprise beginners:
print(int(3.9))     # prints 3, not 4. It cuts off the decimal part, no rounding
print("5" + "5")    # prints 55, because + joins two texts together

# an type arror 
#print("5" + 3)      # TypeError: a text and a number can't be added

# Practice queations
name="shadpw"
age=23
height=123.6
is_learning=True
print(type(name))
print(type(age))
print(type(height))
print(type(is_learning))

a="10"
b="20"
print(a+b)

a=int(a) # contert to string to int 
b=int(b) # contert to string to int 
print(a+b) # the out put is 30 

print(type(7)) # int type 
print(type(7.0)) # float type becaue of 7.0 decimal value
print(type("7")) # string type
print(type(True)) # bool true or false
print(type("True")) # string type
#
#print("Age: " + 25)
#Traceback (most recent call last):
 # File "c:\Users\gandr\Documents\notes-of-python\03_Data_types.py", line 86, in <module>
 ##   print("Age: " + 25)
    #      ~~~~~~~~^~~~
#TypeError: can only concatenate str (not "int") to str

# fixed method 1

print("Age:", 25)  # now it print age : 25
# method 2
print("Age: " + str(25))
#5
a=3.9
a=int (a)
print(a)  # the output is 3 it removes the decimal value and print the value here is 7
b=7
b=float(b)
print(b) # here the value has been chaged to decimal 7.0

# what is data type why python care about it 
#A data type tells Python what kind of value something is.

#int() converts a float into an integer by removing the decimal part. It does not round the number.
# data type is a value that tels you that it is a string type we can use it an for the string function
# 25 is the type is int , and "25 " is a string because of the " "double codes
# print(int(7.9)) show the it removes the decimal value here the .9 

#difference between "5" + "5" and 5 + 5 
# "5"+"5" it is a string type and it print the two text togenter so 55 is answer
# 5+5 it is an int type so it add the two int values to become 10 
# None is a no value for example name ="ralesj",age =4,hpone=None there is no value


print(type(3 + 2.0)) # float because of the 5.0
print(type(str(10))) # it convert to the string type like "10"
#print(int("3.5")) # error value error 


#fix it by the converting 
print(float(3.5))

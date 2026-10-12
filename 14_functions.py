# functions what is a functions
# # once you write a code it will re use again in that code in at any stage
# example
print("Hello, Ravi!")
print("Hello, Sita!")
print("Hello, Arun!")
# here we rite the ocde write again andagain for the each user so automate by function

def greet(name): # here name is called parameters

    print("Hello,", name + "!")
    #
# function calling 
greet("Ravi") # here we give the Argument's

greet("Sita")  #  
greet("Arun")


######################
"""
Parameter: the variable name in the def line (a placeholder).
Argument: the real value you pass when calling.

"""
def square(n):
    print(n * n)

square(4)
square(7)

#  Return 
# How it works 
#  return sending a value back it stores it 
# print only shows a value on the screen 
# return goves give the valur back to the code that called the function so you cah use it
# 
def add(a,b):
    return a+b
result=add(2,3)
print(result)
print(add(10, 20) * 2)

"""
print vs return
print

what is does : show text on screen 

Can you use the value afterwards? no 

Can you use the value afterwards? nO

RETURN
Sends the value back to the caller :
Can you use the value afterwards? yes
Does the function stop?	:	Yes, it ends immediately
"""
def test():
    return 1
    print("never runs")

###

def check(n):
    if n > 10:
        return "big"
    return "small"

print(check(15))
print(check(3))


#   Multiple parameters
def subtract(a, b):
    return a - b

print(subtract(10, 3))
print(subtract(3, 10))


# local and gobal variabeles 

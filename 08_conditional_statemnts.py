# today is multiple condtiond and nested conditions
# comdning conditiond with and /or and if
# why the order of elif conditions matters
# nested conditions and if inside  another if

#Multiple conditions means checking several things at once. You learned and, or and not on Day 6. Now you use them inside if

#Nested conditions means putting an if inside another if. The inner one only runs if the outer one was true. Think of airport security: first "do you have a ticket?" and only if yes, "is your bag allowed?"

#Why is it useful? Real decisions often depend on more than one thing: "You can drive if you're 18 or older and have a licence." Both ideas below handle that.

#########
# examples 
age =20
has_licence= True

if age >=18 and has_licence:
    print("you can drive")
else:
    print("you cannot brive")
#
username=input(" user in put for user name ")
password=input("user password ")
if username=="admin":
    if password == "1234":


        print("welcome,admin")
    else:
        print("wrong passoerd ")
else:
    print("unknown user")

######
marks = int(input("Marks: "))  # if input is 90
if marks >= 50:   # check the condition is true so print pass and exect the ans no neeed to check the else 
    print("Pass")
elif marks >= 80:  #
    print("Very Good")
elif marks >= 90:  
    print("Excellent") # 
####
age=int(input("enter your age :"))
ticket=input("yes or no")
if age >= 18:
    
    if ticket== "yes":
        print("Enter")
    else:
        print("buy a ticket")
    
else:
    print("not allowed")
#### but using else if we can do btter solution here 

age = int(input("Enter your age: "))
ticket = input(" yes no: ")

if age < 18:
    print("Not allowed")
elif age >=18 and ticket == "yes":
    print("Enter")
else:
    print("Buy a ticket")

####
number=int(input("enter a number : "))
if number >=1 and number<=100 and number%5==0:
    print("Yes")
else:
    print("No")

a=5
b=5
c=5
if a>b:
    print(a)
elif b>c:
    print(b)
elif c>a:
    print (c)
#
    

#
# this is the only for the status purpose only


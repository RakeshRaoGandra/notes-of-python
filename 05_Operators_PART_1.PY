# Operators, Part 1 (arithmetic and assignment operators)

"""
What is an operator :
An operatoe is a symbol that does an action
on values you already know + and = .The values it works on are called operands. in 5+3 the operands are 5 and 3 + is a opperatoe
why use ful 
every program calculates something  total's ,disounts,avge's,

Types of operatoes
1 Arthmetic operatoes
2.Assignment operators




1 Arthmetic operatoes
+ it add the numbers
-  it substracts the number

* it multtiplies
/ it divides example 7/2 =3.5
// it  id an floor division 7//2 gives 3 it removes the decinal value

% it gives the remainder 7//2 gives the 1 it is called the modulus

**  power operatoer 7**2 =49

2 . Assignment operators

Shortcut	   Same as
x += 3	       x = x + 3
x -= 3	       x = x - 3
x *= 3	       x = x * 3
x /= 3	       x = x / 3
x //= 3	       x = x // 3
x %= 3	       x = x % 3
x **= 3	       x = x ** 3

syntax = result = a+b
x+=5
"""

total_minutes = 135

hours = total_minutes // 60
minutes = total_minutes % 60
print(hours, "hours and", minutes, "minutes")

balance = 1000
balance += 500
balance -= 200
balance *= 2
print("Balance:", balance)

# Practice problems
#Predict, then run: what does each line print?
print(20 + 4) # the output well be the 24
print(20 / 4) # the ouput is 5.0
print(20 // 3) # the output is 6
print(20 % 3)  # the output is 2
print(2 ** 5) # the output is 32

#Ask the user for a number of days and print how many weeks and leftover days that is. For example, racket 45 gives 6 weeks and 3 days.
# how to calculate the 45. 45 // by 7 it gives the weeks 
# now how to calculate the remaing days now use the % modulo for the remaing days
racket=int(input("enter the number value :"))
print(racket//7,"weeks","and",racket%7,"days")
print(racket%7)

#Predict, then run: what is n after each line, and what does the last print show?
n = 10  # here n=10
n += 5 # here thr n+5 =10+5 = 15
n *= 2 # here 15*2=30
n -= 4 #n= 30 -4= 26
n //= 3 #n=26 26//3=8
print(n) #n=8

#Ask the user for a number and print whether it is even or odd using %. For now just print the result of number % 2, and tell me what you notice for 7 and for 10.
n=int(input("enter a number"))
print(n%2==0) # for 7 it false becausse of it is odd,for 10 true becaue it is even.

#Ask the user for a price (decimals allowed) and a discount in percent. Print the final price after the discount. Example: price 200, discount 10 gives 180.0.
item=input("name of the product : ")
price=int(input("product price : "))
discount = int(input("enter discount : "))
total_price=price*(1-discount/100)
print(total_price)

# end of the day check point
#difference between / and //
# / it is an divide that dive the number example : 5/4=1.25
# // it is an floor division example 7//2 gives 3 it removes the decinal value 
# % meand modulo operator 17%5 gives the remainder there 2 is remainder
#3
x = 4 # here x=4
x += 6 # x+6 here x = 4+6 =10
x *= 2 # here 10 *2 =20 x=20
#
#10 / 2: 5 or 5.0? Why does it matter
# when it use the int data type it gives 5 and when it use the float it gives the 5.0
# in the python it use the true division so the ans =5.0
# yes number %2 is use ful when we find the odd even number 
print(10/2) #(Standard division always produces a float)
print(10%2)# it gives 0 When you apply the modulo operator (%) to exact integers, it returns an exact integer remainder

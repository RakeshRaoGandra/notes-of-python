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
# 
#  
#Local variable: created inside a function. It exists only while the function runs.



def show():
    x=5
    print(x)
show()
print(5)

# Global variable: created outside all functions. A function can read it.

rate = 10

def price(qty):
    return qty * rate

print(price(3))

#####
def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

print(sum_to(4))

######
# functions with strings 
# 
def count_vowels(word):
    count = 0
    for ch in word:
        if ch in "aeiou":
            count = count + 1
    return count

print(count_vowels("education"))
print(count_vowels("sky"))

#
# functions with lists 
def find_max(nums):
    biggerst=nums[0]
    for n in nums:
        if n>biggerst:
            biggerst=n
    return biggerst
print(find_max([4,5,3425,234,23]))

arr=[234,235,234,23,5,23,4,23,4235,2423,3498,6553,5]
bigesr=0
for n in arr:
    if n>bigesr:
        bigesr=n
print(bigesr)

######
# 
# another thatn that practice sone of athe incorect probles,s
def total(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i
        return s

print(total(4))
print(total(5))

"""
Functions: Practice Problems to Write

I took this to mean “give me functions to write for practice.” If you wanted something else, tell me.

Rules:

Write the code yourself. I won’t give solutions until you send your attempt.
Use return, not print, inside the function. Print only when you test it.
Test every function with at least 2 inputs.
Send me your code, and I’ll check it line by line.
Level 1: Basics (parameters and return)
square(n): returns n * n
add(a, b): returns the sum
is_positive(n): returns True if n > 0, else False
is_even(n): returns True if n is even
bigger(a, b): returns the larger of two numbers (without using max())
Level 2: Functions with if
grade(marks): returns "A" if marks ≥ 80, "B" if ≥ 50, else "C"
check_sign(n): returns "positive", "negative", or "zero"
is_adult(age): returns True if age ≥ 18
Level 3: Functions with loops
sum_to(n): returns the sum of 1 to n
factorial(n): returns n! (for example, factorial(4) is 4 * 3 * 2 * 1 = 24)
count_even_upto(n): returns how many even numbers are between 1 and n
multiplication_table(n): prints the table of n from 1 to 10 (this one prints instead of returning)
Level 4: Functions with strings
count_vowels(word): returns the number of vowels
count_char(word, ch): returns how many times ch appears
reverse_string(s): returns the reversed string (use a loop, not [::-1])
is_palindrome(s): returns True or False (compare characters from both ends)
Level 5: Functions with lists
sum_list(nums): returns the sum
find_max(nums): returns the largest number (without max())
count_positive(nums): returns how many numbers are greater than 0
contains(nums, target): returns True if target is in the list (use a loop, not in)
Level 6: Combining functions
Write is_even(n) first, then write count_evens(nums) that calls is_even.
Write is_vowel(ch) first, then write count_vowels(word) that calls it.

#	Topic	Status
1	Why functions are needed	✅ Taught (Day 7)
2	Defining a function (def) and calling it	✅ Taught (Day 7)
3	Parameters vs arguments	✅ Taught (Day 7)
4	return and print vs return	✅ Taught (Day 7)
5	Multiple parameters (order matters)	✅ Taught (Day 8)
6	Local variables	✅ Taught (Day 8)
7	Global variables	✅ Taught (Day 8), but only reading them
8	Functions with loops	✅ Taught (Day 8)
9	Functions with strings	✅ Taught (Day 8)
10	Functions with lists	✅ Taught (Day 8)
11	Breaking a problem into functions	✅ Taught (Day 8)
Extra topics that matter for DSA (not taught yet)
#	Topic	Why it matters
12	Modifying a global variable (the global keyword)	Completes the local vs global topic. You’ll see why it’s usually avoided
13	Local vs global with the same name	A local x and a global x are different variables. A classic trap
14	Returning multiple values	return a, b is used in many problems
15	Default parameters	def greet(name="friend")
16	Keyword arguments	Calling with f(a=1, b=2) so order doesn’t matter
17	Functions calling other functions	The step before recursion
18	A function without return gives None	Common source of bugs
19	Passing a list to a function and changing it	The change is visible outside, which links to mutable vs immutable later


"""


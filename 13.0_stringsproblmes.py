#STRINGS (Part 3): Reversing, Palindromes, Counting

# conatenation joinig string 
# use + to join string and * to reperat them
# example
print("py" + "thon")
print("ab" * 3)
# comparsasin ==,!=,<,>=,<= 
print("cat" == "cat")
print("cat" == "Cat")
print("apple" < "banana")

#  reverse a string in slicing 
s="nithinkumar"
print(s[::-1])
# while loop 
s="abc"
rev=" " # here using stack
for ch in s:
    rev=ch+rev
print(rev)

# palindrome checckign
s="level"
if s==s[::-1]:
   print("paldrome")
else:
   print("not a pladrome")
#
# character counting
s="123234sgvgwesg34"
count=0
for ch in s:
   if ch.isdigit():
      count=count+1
print(count)
"""

Common mistakes
Using rev + ch instead of ch + rev when reversing with a loop.
Forgetting case in palindromes. "Level" is not equal to its reverse "leveL". Use .lower() first.
Checking all len(s) pairs in Way 2. Only half is needed.
Mixing up s[-1 - i] and s[-i]. When i = 0, s[-0] is the same as s[0], which is wrong.
Setting is_pal = True inside the loop, which erases an earlier False.

"""
#   Exercises: predict first, don’t run
print("ab" + "cd")
print("ab" * 3)
print("apple" < "banana")
print("Zebra" < "apple")
print("a" == "A")

s = "dog"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

"""

Exercise 3: Is each string a palindrome by Way 2? Make a trace table like Section 4 for each.

(a) "madam"
(b) "abcd"

Exercise 4 (write code): Count how many times the letter "s" appears in "mississippi" using a loop and an if. Don’t use count().

Exercise 5 (write code): Check if "Racecar" is a palindrome, ignoring capital letters. Print Palindrome or Not palindrome. (Hint: use .lower() first.)


"""

s = "level"
is_pal = True

for i in range(len(s) // 2):
    if s[i] != s[-1 - i]:
        is_pal = False

print(is_pal)
#srtings in not in most usae fuk methods
# SLICING FIVES TOU PAET OF a srting


"""
string:  p  y  t  h  o  n
index:   0  1  2  3  4  5

s[start:stop]
"""
s = "python"
print(s[0:3])
print(s[2:5])

# in and not in : is it inside

s = "python"
print("th" in s)
print("z" in s)
print("z" not in s)

print("aspfand the higher authorty")
#
h="handrudad of the things"
print("the" in h)
print("c" not in h)
#
s = "hello"
s.upper()
print(s)

##
word = "education"
vowels = "aeiou"
count = 0

for ch in word:
    if ch in vowels:
        count = count + 1

print(count)

#
print("..........................................................")

email = "rakesh@gmail.com"
at = email.find("@")
username = email[:at]
domain = email[at + 1:]
print(username)
print(domain)

# computer certificate 
print(s[:3])
print(s[4:8])
print(s[-4:])
print(s[::3])

print("gram" in "programming")
print("Pro" in "programming")
print("x" not in "programming")

print("  Hello World  ".strip().lower())
print("a-b-c".split("-"))
print("banana".count("a"))
print("banana".find("n"))
print("banana".find("z"))

s = "hello"
s[0] +"H"
print(s)

#


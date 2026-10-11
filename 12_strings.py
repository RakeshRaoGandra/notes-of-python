# strngs the strings is text a sequence of characters in quotes 
# letters ,digits ,space and symbols all count as charracters

s="python"
#many dsa problems are aabout strings palindromes ccountinf leerwes reversing words finding patterns 
s = "python"
print(s[0])
print(s[3])
"""
string:     p    y    t    h    o    n
index:      0    1    2    3    4    5
neg index: -6   -5   -4   -3   -2   -1
"""
print(s[-1])
print(s[-2])

# length of a strng
print(len("python"))

s = "python"
print(s[5])

#looping through a string two ways
#character by character
s = "cat"
for ch in s:
    print(ch)
# by index 
s = "cat"
for i in range(len(s)):
    print(i, s[i])
###
word="nithin"
if word[0]==word[-1]:
    print("same")
else:
    print("different")
####
print(len("data analyst"))
s="cpseds"
for i  in range(len(s)):
    print(i,s[i])

s = "python"
for i in range(len(s) - 1, -1, -1):
    print(s[i])
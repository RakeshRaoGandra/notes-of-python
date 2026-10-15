# Today topic is about the arrays
# topics are creating list indxing negative indexing slicing  traversing and updateing searching inserting deleting 
# List 
# IN LIST USE every thing you have indexing slicing loops 

# what is an array
# an array is row of boxed in memery each holding one valuse numbered by position starting form 0 
# index:    0    1    2    3    4
# value:  [10] [20] [30] [40] [50]
#
# python list vs array

# python doesnot't have a built in array for everyday use 
# so it has lists which work like array and we what we use in dsa practice

#  a list stores items in order with index 0,1,2,3........
# a list can hold numbers strings or a amix
# unlike a string a list can be changed after it is created

# creating a lista
nums=[10,20,30]
names=["rakesh","nithin","venugopla","Mahesh"]
empty=[]
mixed=[1,"nithin",3.5,False]

#You can also build a list with range():

numss=list(range(1,9))
print(numss)

#len() gives the number of items:

print(len(numss))



# Indexing
nums=[50,60,70,80]
print(nums[0])
print(nums[3])

# Negative indexing counts from the end, starting at -1:


# index:      0    1    2    3    4
# value:    [10] [20] [30] [40] [50]
# neg index: -5   -4   -3   -2   -1

print(nums[-1])
print(nums[-2])


##### 
# . Slicing
# Same as strings: nums[start:stop], where start is included and stop is not.

nums = [10, 20, 30, 40, 50]
print(nums[1:4])
print(nums[:2])
print(nums[3:])
print(nums[::-1])

"""
nums[1:4] takes indexes 1, 2, 3.
nums[::-1] reverses the list.

"""

#  Traversing a list
# by value
nums = [10, 20, 30]
for n in nums:
    print(n)

#
# by index
for i in range(len(nums)):
    print(i, nums[i])
#
# Updating (changing) items
# Lists are mutable, which means you can change an item in place. Strings can’t do this.
nums = [10, 20, 30]
nums[1] = 99
print(nums)

# Updating every item with a loop:

nums = [1, 2, 3]
for i in range(len(nums)):
    nums[i] = nums[i] * 2
print(nums)

# Slightly realistic example: marks above average


marks = [70, 85, 90, 60]
total = 0

for m in marks:
    total = total + m

average = total / len(marks)
print(average)

for i in range(len(marks)):
    if marks[i] > average:
        print("Index", i, "is above average:", marks[i])

#####
# next is searching, inserting, deleting, and list methods.

# next abou the list of the top indursities
#and to tje necr 

# the maon thye of the main type in thewrol
# rbi 

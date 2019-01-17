#!/usr/bin/python

listint = [1,4,3,5,6,7,8,2]
listchar = ['c','a','r','a','t','h']

# Index
# c
print(listchar[0])

# Negative indexing
# h
print(listchar[-1])

#prints t
print(listchar[-2])

# Slices
# 3rd to 5th element ['r', 'a', 't']
print(listchar[2:5])

# beginning to 3rd last character ['c', 'a', 'r']
print(listchar[:-3])

# 3rd from beginning to end
print(listchar[3:]

# Chaning arrays

# change single element
listchar[0] = 'f'

# change slice
listchar[0:2] = ['f', 'a']

# Append adds single item to the end of the list
listint.append(3)

# Extend adds list to end of list
listint.extend([1,2,3])

# Insert into list, now listint[1] is 4
listint[1:1] = 4

# prepend list
a = [1,2,3]
b = [4,5,6]
a[:0] = b
a
# output [4, 5, 6, 1, 2, 3]

# You can 'insert' another list at any position, just address the empty slice at that location:
a = [1,2,3]
b = [4,5,6]
a[1:1] = b
a
# output [1, 4, 5, 6, 2, 3]

# Removing elements list.remove() removes one matching element from the list
a.remove(2)
print(a)

# finding index of an element, list.index() returns the smallest index matching
print(a.index(3))

# Concatenating lists
#https://www.programiz.com/python-programming/list
odd = [1, 3, 5]

# Output: [1, 3, 5, 9, 7, 5]
print(odd + [9, 7, 5])

# * operator repeats a list a given number of times
#Output: ["re", "re", "re"]
print(["re"] * 3)

# Count recurrences of an item

test = [1, 2, 1, 3, 1]
print(test.count(1))

# Remove and return item at index with pop

item = test.pop(3)
print(item)
print(test)

# Map
def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)

# Sort, sorted
test.sort()
# Or
test = sorted(test)
print(test)

# Max
print(max(test))

# Min
print(min(test))

# Max and min can be passed multiple variables or an iterable
print(max(test[1], test[2])

# Sum of all itmss in list
print(sum(test))

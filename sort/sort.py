#!/bin/python3

import math


#n = int(input().strip())
#unsorted = []
#unsorted_i = 0
#for unsorted_i in range(n):
#    unsorted_t = int(input().strip())
#    unsorted.append(unsorted_t)
unsorted = [6, 31415926535897932384626433832795, 1, 3, 10, 3, 5]

def merge(a,b):
    """ Function to merge two arrays """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

def mergesort(x):
    """ Function to sort an array using merge sort algorithm """
    if len(x) == 0 or len(x) == 1:
        return x
    else:
        middle = math.floor(len(x)/2)
        a = mergesort(x[:middle])
        b = mergesort(x[middle:])
        return merge(a,b)

sorted = mergesort(unsorted)
for key in sorted:
    print(key)

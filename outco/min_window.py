#!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'minimumWindowSubstring' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING fullString
#  2. STRING chars
#

def make_t(string):
    t = {}
    for char in string:
        if char not in t:
            t[char] = 1
        else:
            t[char] += 1
    return t
def update_t(adding, subtracting, table):
    if adding:
        table[adding] += 1
    if subtracting:
        table[subtracting] -= 1
    return table

def key_in_cur(key, cur):


def minimumWindowSubstring(fullString, chars):
    # Write your code here
    key = make_t(chars)
    if len(fullString) < 1:
        return ""
    begin = 0
    end = 0
    if fullString[0] in key:
        cur = {fullString[0]:1}
    else:
        cur  ={}
    while end <= len(fullString):

        if key_in_cur(key, cur):
            temp = update_t()
            begin += 1
        end += 1




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    fullString = raw_input()

    chars = raw_input()

    result = minimumWindowSubstring(fullString, chars)

    fptr.write(result + '\n')

    fptr.close()


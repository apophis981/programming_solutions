#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    num_bribes = 0
    for i in range(len(q)-1):
        diff = q[i] - (i+1)
        print(diff)
        if q[i] > i+1:
            #print diff
            if diff >= 3:
                print("Too chaotic")
                return
            else:
                num_bribes += diff
        elif diff <= -4:
            num_bribes += abs(diff) - 3
    print num_bribes
    return

if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)

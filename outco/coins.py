!/bin/python

import math
import os
import random
import re
import sys



#
# Complete the 'coinSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY coins
#  2. INTEGER total
#

def coinSum(coins, total):
    # Write your code here
    ans = 0
    prev_s = set(coins)
    for i in range(len(coins)):
        for j in range(i, len(coins)):
            print(coins[i], coins[j], prev_s)
            if coins[i] + coins[j] == total:
                ans += 1
                print("found")
            if coins[i] + coins[j] < total:
                prev_s.add(coins[i]+coins[j])
            for item in prev_s:
                t = coins[i] + item
                if t == total:
                    ans +=1
                    print("found")
                if t < total:
                    prev_s.add(t)
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    coins_count = int(raw_input().strip())

    coins = []

    for _ in xrange(coins_count):
        coins_item = int(raw_input().strip())
        coins.append(coins_item)

    total = int(raw_input().strip())

    result = coinSum(coins, total)

    fptr.write(str(result) + '\n')

    fptr.close()


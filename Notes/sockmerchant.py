import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.


def sockMerchant(n, ar):
    count = 0
    pairs = []
    for i in ar:
        if i in pairs:
            count += 1
            print(count)
            pairs.remove(i)
        else:
            pairs.append(i)
            print(pairs)

    return count


sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input())
#
#     ar = list(map(int, input().rstrip().split()))
#
#     result = sockMerchant(n, ar)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()


'''
Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers.
'''


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arr_reverse = arr[::-1]

    result=''
    
    for item in arr_reverse:
        result = result + str(item) + ' '
    
    print(result[0:-1])



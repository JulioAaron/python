'''
Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting 
the maximum number of consecutive 1's in n's binary representation.
'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    nstr = str(bin(n))[2:]
    count_sec_ones=[]
    count_sec=0

    for item in nstr:
        if int(item)==1:
            count_sec +=1
            count_sec_ones.append(count_sec)
        else:
            if count_sec>0:
                count_sec=0

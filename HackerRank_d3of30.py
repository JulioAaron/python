'''
Task 
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5 , print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird

'''


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    #If  is odd, print Weird
    if N%2!=0:
        print("Weird")
    else:
        #If  is even and in the inclusive range of 2 to 5, print Not Weird
        if (2<= N <=5):
            print("Not Weird")
        #If  is even and in the inclusive range of 6  to 20, print Weird
        elif (6<= N <=20):
            print("Weird")
        #If  is even and greater than 20, print Not Weird
        else:
            print("Not Weird")

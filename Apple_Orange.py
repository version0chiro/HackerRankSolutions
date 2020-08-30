#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    positionApples=[]
    countA=0
    countB=0
    positionOranges=[]
    for _ in apples:
        positionApples.append(a+_)
        if ((a+_)>=s and (a+_)<=t):
            countA+=1
    for _ in oranges:    
        positionOranges.append(b+_)
        if ((b+_)>=s and (b+_)<=t):
            countB+=1
    print(countA)
    print(countB) 

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

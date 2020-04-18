#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    arrLength = len(arr)
    for i in range(arrLength):
        print(arr[(arrLength-1) - i], end=' ')
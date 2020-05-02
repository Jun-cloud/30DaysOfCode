#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binN = bin(n)[2:]
    result = 1
    tmpCount = 1
    for i in range(len(binN)):
        if i+1 < len(binN):
            if binN[i] == binN[i+1] == '1':
                tmpCount += 1
            else:
                if tmpCount > result:
                    result = tmpCount
                tmpCount = 1
        else:
            if tmpCount > result:
                    result = tmpCount
print(result)

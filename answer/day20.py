#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
sortingCount = 0
while True:
    tmpCount = 0
    for i in range(n-1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            tmpCount += 1
            sortingCount += 1

    if tmpCount == 0:
        print('Array is sorted in {0} swaps.'.format(sortingCount))
        print('First Element:', a[0])
        print('Last Element:', a[n-1])
        break
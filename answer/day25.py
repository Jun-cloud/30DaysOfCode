# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

testCast = int(input())
for i in range(testCast):
    result = 'Prime'
    case = int(input())
    if case == 1:
        result = 'Not prime'
    elif case == 2:
        result = 'Prime'
    else:
        for i in range(2, int(math.sqrt(case) + 1)):
            if case%i == 0:
                result = 'Not prime'
                break
    print(result)
# Enter your code here. Read input from STDIN. Print output to STDOUT

testCase = int(input())

for i in range(testCase):
    inputText = input()
    evenText = ''
    oddText = ''

    for l in range(len(inputText)):
        if l % 2 == 0:
            evenText += inputText[l]

        if l % 2 == 1:
            oddText += inputText[l]

    print(evenText, oddText)
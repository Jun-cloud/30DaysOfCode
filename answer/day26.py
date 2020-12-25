# Enter your code here. Read input from STDIN. Print output to STDOUT

def checkDueDate(returnDate, dueDate):
    if int(returnDate[2]) > int(dueDate[2]):
        return 10000

    elif int(returnDate[2]) == int(dueDate[2]):
        if int(returnDate[1]) > int(dueDate[1]):
            m = int(returnDate[1]) - int(dueDate[1])
            return m * 500

        elif int(returnDate[1]) == int(dueDate[1]):
            if int(returnDate[0]) > int(dueDate[0]):
                d = int(returnDate[0]) - int(dueDate[0])
                return d * 15
    return 0

returnDate = input().split(' ')
dueDate = input().split(' ')

result = checkDueDate(returnDate, dueDate)
print(result)

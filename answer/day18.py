import sys


class Solution:
    # Write your code here
    stack = []
    queue = []

    def __init__(self):
        super().__init__()

    def pushCharacter(self, s):
        self.stack += s

    def popCharacter(self):
        return_char = self.stack[len(self.stack) - 1]
        del self.stack[len(self.stack) - 1]
        return return_char

    def enqueueCharacter(self, s):
        self.queue += s

    def dequeueCharacter(self):
        return_char = self.queue[0]
        del self.queue[0]
        return return_char

# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
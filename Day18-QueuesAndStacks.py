class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []
        self.stackTop = None

    def pushCharacter(self, c):
        if len(self.stack) == 0:
            self.stackTop = 0
        else:
            self.stackTop += 1
        self.stack.append(c)

    def enqueueCharacter(self, c):
            self.queue.append(c)

    def dequeueCharacter(self):
        if len(self.queue) > 0:
            ch = self.queue[0]
            self.queue.pop(0)
            return ch

    def popCharacter(self):
        if len(self.stack) > 0:
            ch = self.stack[self.stackTop]
            self.stack.pop(self.stackTop)
            self.stackTop -= 1
            return ch

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
    a = obj.popCharacter()
    b = obj.dequeueCharacter()
    if a != b:
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
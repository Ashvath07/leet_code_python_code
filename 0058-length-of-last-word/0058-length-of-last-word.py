class Solution(object):
    def lengthOfLastWord(self, s):
        stack = []
        for i in s.split():
            stack.append(i)
        return len(stack[-1])

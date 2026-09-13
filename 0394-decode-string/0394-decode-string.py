class Solution(object):
    def decodeString(self, s):
        stack1 = []
        num = 0
        current = ''
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])

            elif s[i] == '[':
                stack1.append((num, current))
                num = 0
                current = ''

            elif s[i] == ']':
                current = stack1[-1][1] + current * stack1[-1][0]
                stack1.pop()
                # repeat, previous = stack1.pop()
                # current = previous + current * repeat

            else:
                current += s[i]
        return current
class Solution(object):
    def isValid(self, s):
        freq = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        stack =[]
        for check in s:
            if check in freq:
                if stack and stack[-1] == freq[check]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(check)
        if not stack:
            return True
        else:
            return False
        
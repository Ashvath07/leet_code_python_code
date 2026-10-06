class Solution(object):
    def minAddToMakeValid(self, s):
        stack = []
        pairs = {')': '('}

        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif stack and stack[-1] == pairs[ch]:
                stack.pop()
            else:
                stack.append(ch)

        return len(stack)
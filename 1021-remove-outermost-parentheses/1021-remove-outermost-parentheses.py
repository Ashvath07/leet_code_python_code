class Solution(object):
    def removeOuterParentheses(self, s):
        l,count=[],0
        st=""
        for i in s:
            if i == ')':
                count-=1
            if count >0:
                l.append(i)
            if i == '(':
                count+=1
        return ''.join(l)
class Solution(object):
    def reverseDegree(self, s):
        total =0
        for i,c in enumerate(s):
            rev = 26 - (ord(c)-ord('a'))
            store = i+1
            total += rev * store
        return total
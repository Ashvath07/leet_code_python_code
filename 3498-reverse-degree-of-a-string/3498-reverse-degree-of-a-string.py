class Solution(object):
    def reverseDegree(self, s):
        total =0
        for i,c in enumerate(s,start=1):
            rev = 26 - (ord(c)-ord('a'))
            total += i*rev 
        return total
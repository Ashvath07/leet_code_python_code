class Solution(object):
    def repeatedSubstringPattern(self, s):
       return s in s[1:]+s[:-1]
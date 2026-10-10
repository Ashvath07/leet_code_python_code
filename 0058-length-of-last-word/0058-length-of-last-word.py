class Solution(object):
    def lengthOfLastWord(self, s):
        word = s.split()
        last = word[-1]
        return len(last)

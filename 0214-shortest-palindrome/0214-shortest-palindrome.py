class Solution(object):
    def shortestPalindrome(self, s):
        if not s or s[::-1] == s:
            return s

        i = 0
        for j in range(len(s)-1, -1, -1):
            if s[j] == s[i]:
                i += 1

        if i == len(s):
            return s

        s1 = s[i:]

        s2 = s1[::-1] + s

        while s2 != s2[::-1]:
            i -= 1
            s3 = s[i::]
            s2 = s3[::-1] + s
        
        return s2
class Solution(object):
    def distinctSubseqII(self, s):
        mod = 10**9 +7
        total = 0
        dp = [0]*26
        for c in s:
            index = ord(c)-ord('a')
            add = (total+1)%mod
            total = (total+add - dp[index]+mod) % mod
            dp[index] = add 
        return total

class Solution(object):
    def maxPalindromes(self, s, k):
        n,ans,last_end = len(s),0,-1
        for i in range(n):
            start_k = i - k + 1 
            if start_k >= 0 and start_k > last_end:
                if s[start_k : i + 1] == s[start_k : i + 1][::-1]:
                    ans += 1
                    last_end = i
                    continue
            start_k1 = i - k
            if start_k1 >= 0 and start_k1 > last_end:
                if s[start_k1 : i + 1] == s[start_k1 : i + 1][::-1]:
                    ans += 1
                    last_end = i
        return ans
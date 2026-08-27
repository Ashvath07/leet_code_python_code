class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        best = ""
        left = 0
        ones = 0
        for right in range(len(s)):
            if s[right] == "1":
                ones += 1
            while ones == k:
                cand = s[left:right + 1]
                if s[left] == "1":
                    ones -= 1
                left += 1
                if best == "" or len(cand) < len(best) or (len(cand) == len(best) and cand < best):
                    best = cand
        return best
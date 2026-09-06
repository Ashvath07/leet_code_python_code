class Solution(object):
    def numDistinct(self, s, t):
        memo = {}
        def findOccurrences(i, j):
            s_len = len(s)
            t_len = len(t)
            if j == t_len:
                return 1          
            if i == s_len or s_len - i < t_len - j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            add = findOccurrences(i + 1, j)
            if s[i] == t[j]:
                add += findOccurrences(i + 1, j + 1)          
            memo[(i, j)] = add
            return add        
        return findOccurrences(0, 0)




            
        
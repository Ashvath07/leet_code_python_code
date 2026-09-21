class Solution(object):
    def resultArray(self, nums, k):
        prefix = [0]*k
        suffix = [0]*k
        for n in nums:
            n%=k
            cur = [0]*k
            cur[n] =1
            for x,y in enumerate(suffix):
                cur[x*n%k] += y
            suffix = cur
            for x,y in enumerate(suffix):
                prefix[x] += y
        return prefix
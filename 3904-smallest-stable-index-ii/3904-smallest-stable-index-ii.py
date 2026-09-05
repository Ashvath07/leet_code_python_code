class Solution(object):
    def firstStableIndex(self, nums, k):
        n=len(nums)
        prefix = [0]*n
        prefix[n-1] = nums[-1]
        for i in range(n-2,-1,-1):
            prefix[i] = min(prefix[i+1],nums[i])
        score =0
        for i,x in enumerate(nums):
            score = max(score,x)
            if score-prefix[i] <= k:
                return i
        return -1
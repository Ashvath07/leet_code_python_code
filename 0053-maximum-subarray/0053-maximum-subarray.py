class Solution(object):
    def maxSubArray(self, nums):
        curr,maxm = nums[0],nums[0]
        for i in range(1,len(nums)):
            curr = max(nums[i],curr+nums[i])
            maxm = max(maxm,curr)
        return maxm
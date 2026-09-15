class Solution(object):
    def arrayPairSum(self, nums):
        nums.sort()
        maxval=0
        i=0
        n=len(nums)
        while i<n:
            maxval+=nums[i]
            i+=2
        return maxval
        
class Solution(object):
    def sumOfSquares(self, nums):
        count =0
        for i in range(len(nums)):
            if len(nums)%(i+1) == 0:
                count+=nums[i]*nums[i]
        return count
class Solution(object):
    def sumOfSquares(self, nums):
        count =0
        n = len(nums)
        for i in range(n):
            if n%(i+1) == 0:
                count+=nums[i]*nums[i]
        return count
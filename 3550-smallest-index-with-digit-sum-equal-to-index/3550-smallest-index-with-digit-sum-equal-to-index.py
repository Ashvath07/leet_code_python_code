class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            dig = nums[i]
            sum = 0
            while dig>0:
                sum += dig%10
                dig//=10
            if sum == i:
                return i
        return -1

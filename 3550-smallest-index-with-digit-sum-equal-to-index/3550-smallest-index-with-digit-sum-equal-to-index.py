class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            sum = 0
            while nums[i]>0:
                sum += nums[i]%10
                nums[i]//=10
            if sum == i:
                return i
        return -1

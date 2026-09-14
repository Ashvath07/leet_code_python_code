class Solution(object):
    def sortArrayByParity(self, nums):
        even = []
        odd =[]
        for right in range(len(nums)):
            if nums[right]%2 == 0:
                even.append(nums[right])
            else:
                odd.append(nums[right])
        return even + odd
class Solution(object):
    def sortArrayByParityII(self, nums):
        
        even = 0
        odd = 1

        while even < len(nums) and odd < len(nums):

            if nums[even] & 1 == 0:
                even += 2
                continue
            
            if nums[odd] & 1 == 1:
                odd += 2
                continue

            nums[even], nums[odd] = nums[odd], nums[even]
            even += 2
            odd += 2

        return nums
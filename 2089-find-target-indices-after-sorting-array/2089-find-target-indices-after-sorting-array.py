class Solution(object):
    def targetIndices(self, nums, target):
        stack =[]
        for i in range(len(nums)):
            for j in range(0,len(nums)):
                if nums[j] > nums[i]:
                    nums[i],nums[j] = nums[j],nums[i]
        for i in range(len(nums)):
            if nums[i] == target:
                stack.append(i)
        return stack
class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        stack =[]
        for i in range(len(nums)):
            if nums[i] == target:
                stack.append(i)
        return stack
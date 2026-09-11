class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        freq={}
        for i in range(len(nums)):
            if nums[i] in freq and abs(i-freq[nums[i]])<=k:
                return True
            freq[nums[i]] = i
        return False
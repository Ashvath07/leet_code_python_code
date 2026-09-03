class Solution(object):
    def uniformArray(self, nums1):
        return not (min(nums1) ^ reduce(or_ , nums1)) & 1
class Solution(object):
    def findKthLargest(self, nums, k):
        store = sorted(nums,reverse =True)
        return store[k-1]
class Solution(object):
    def minMoves(self, nums):
        maxnum = float('-inf')
        total = 0
        for num in nums:
            total += num
            maxnum = max(num,maxnum)
        return len(nums)*maxnum - total
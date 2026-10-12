class Solution(object):
    def maxSum(self, nums, k):
        mod = 10**9+7
        count =[sum(x >> b&1 for x in nums)for b in range(30)]
        total= 0
        for i in range(k):
            row = sum(1<<b for b in range(30)if count[b]>i)
            total+=row**2
        return total % mod
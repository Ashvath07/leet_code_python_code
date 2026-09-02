class Solution(object):
    def reversePairs(self, nums):
       from bisect import bisect_left,insort
       sorted_right=[]
       c=0
       n=len(nums)
       for i in range(n-1,-1,-1):
            c+=bisect_left(sorted_right,(nums[i]+1)//2)
            insort(sorted_right,nums[i])

       return c
        
        
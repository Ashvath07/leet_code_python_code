class Solution(object):
    def arrayPairSum(self, nums):
        s = sorted(nums)
        s1 =0
        for i in range(0,len(nums),2):
            s1+=min(s[i],s[i+1])
        return s1
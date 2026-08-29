class Solution(object):
    def lexicographicallySmallestArray(self, nums, limit):
        groups=[]
        freq={}
        for val in sorted(nums):
            if not groups or val - groups[-1][-1] >limit:
                groups.append([])
            groups[-1].append(val)
            freq[val] = len(groups)-1
        itr =[iter(g) for g in groups]
        for i in range(len(nums)):
            nums[i] = next(itr[freq[nums[i]]])
        return nums
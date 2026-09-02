class Solution(object):
    def sortArray(self, nums):
        if len(nums)<=1:
            return nums
        mid = len(nums)//2
        first = self.sortArray(nums[:mid])
        second = self.sortArray(nums[mid:])
        return self.merge(first,second)
    def merge(self,first,second):
        r,i,j =[],0,0
        while i<len(first) and j<len(second):
            if first[i]<=second[j]:
                r.append(first[i])
                i+=1
            else:
                r.append(second[j])
                j+=1
        r.extend(first[i:])
        r.extend(second[j:])
        return r






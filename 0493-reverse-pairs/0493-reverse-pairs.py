class Solution(object):
    def reversePairs(self, nums):
        count=0
        if len(nums)>1:
            # calculate mid
            mid=len(nums)//2
            # divide the input array in to right and left
            left=nums[:mid]
            right=nums[mid:]
            count+=self.reversePairs(left)
            count+=self.reversePairs(right)
            i=0
            j=0
            # the tricky part - updating the count of number of possible pairs
            for i in range(len(left)):
                while j<len(right) and left[i]>right[j]*2:
                    j+=1
                count+=j
            # merge two sorted array
            i=j=k=0        
            while i<len(left) and j<len(right):
                if left[i]>right[j]:
                    nums[k]=right[j]
                    j+=1
                    k+=1
                else:
                    nums[k]=left[i]
                    i+=1
                    k+=1
            while j<len(right):
                nums[k]=right[j]
                j,k=j+1,k+1
            while i<len(left):
                nums[k]=left[i]
                i,k=i+1,k+1     
        return count       
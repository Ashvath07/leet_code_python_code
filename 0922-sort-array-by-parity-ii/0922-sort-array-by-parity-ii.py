class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        visited = [0]*len(nums)

        even = 0
        odd = 1

        for i in range(len(nums)):

            if nums[i]%2 ==0:           
                visited[even] = nums[i]
                even += 2

            if nums[i]%2 !=0:
                visited[odd] = nums[i]
                odd +=2

        return visited







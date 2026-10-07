class Solution(object):
    def plusOne(self, digits):
        nums =0
        for i in range(len(digits)):
            nums += digits[i]*(10**(len(digits)-1-i))
        nums+=1
        ans = []
        while nums > 0:
            ans.append(nums%10)
            nums //=10
        ans.reverse()
        return ans
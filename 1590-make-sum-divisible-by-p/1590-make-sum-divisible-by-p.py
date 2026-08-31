class Solution(object):
    def minSubarray(self, nums, p):

        total = sum(nums)
        remainder = total % p

        if remainder == 0:
            return 0

        prefix = 0
        seen = {0: -1}
        answer = len(nums)

        for i in range(len(nums)):
            prefix = (prefix + nums[i]) % p

            needed = (prefix - remainder) % p

            if needed in seen:
                answer = min(answer, i - seen[needed])

            seen[prefix] = i

        if answer == len(nums):
            return -1

        return answer
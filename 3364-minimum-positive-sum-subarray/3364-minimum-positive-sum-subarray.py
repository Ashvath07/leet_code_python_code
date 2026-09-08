class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        ans = float('inf')

        for length in range(l, r + 1):
            window = sum(nums[:length])

            if window > 0:
                ans = min(ans, window)

            for i in range(length, n):
                window += nums[i] - nums[i - length]

                if window > 0:
                    ans = min(ans, window)

        return ans if ans != float('inf') else -1
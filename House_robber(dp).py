class Solution(object):
    def rob(self, nums):
        n = len(nums)
        # If there is only one house
        if n == 1:
            return nums[0]
        # DP array
        dp = [0] * n
        # Base cases
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        # Fill DP array
        for i in range(2, n):
            # Either rob current house or skip it
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        # Maximum money that can be robbed
        return dp[n - 1]

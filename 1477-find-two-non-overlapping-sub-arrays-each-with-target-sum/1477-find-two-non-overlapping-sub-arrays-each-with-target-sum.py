class Solution(object):
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        prefix,suffix,ans = n+1,0,0
        dp = [n]*(n+1)
        for i in range(n):
            suffix += arr[i]
            while suffix > target:
                suffix -= arr[ans]
                ans+=1
            dp[i+1]=dp[i]
            if suffix == target:
                prefix = min(prefix,i-ans+1+dp[ans])
                dp[i+1] = min(dp[i],i-ans+1)
        return -1 if prefix == n+1 else prefix

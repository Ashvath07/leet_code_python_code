# class Solution(object):
#     def numberOfSets(self, n, k):
#         # mod = 10**9 +7
#         # dp = [[0]*(k+1) for _ in range(n)]
#         # for i in range(n):
#         #     dp[i][0] =1
#         # for i in range(1,k+1):
#         #     total = 0
#         #     for j in range(1,n):
#         #         total  = (total+dp[j-1][i-1]) % mod
#         #         dp[j][i] = (dp[j-1][i] + total)%mod
#         # return dp[n-1][k]
class Solution(object):
    def numberOfSets(self, n, k):
        MOD = 10 ** 9 + 7
        numerator = 1
        denominator = 1
        for i in range(1, 2*k+1):
            numerator = (numerator * (n + k - i)) % MOD
            denominator = (denominator * i) % MOD
        return (numerator * pow(denominator, MOD - 2, MOD)) % MOD
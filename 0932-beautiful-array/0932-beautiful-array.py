class Solution(object):
    def beautifulArray(self, n):
        memo = {1 : [1]}
        def generate(size):
            if size in memo:
                return memo[size]
            odds = []
            evens = []
            for x in generate((size + 1) // 2):
                odds.append(2 * x - 1)
            for x in generate(size // 2):
                evens.append(2 * x)
            memo[size] = odds + evens
            return memo[size]
        return generate(n)
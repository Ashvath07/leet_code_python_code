class Solution(object):

    def waysToMakeFair(self, nums):

        even_total = 0
        odd_total = 0

        # Total even and odd index sums
        for i in range(len(nums)):
            if i % 2 == 0:
                even_total += nums[i]
            else:
                odd_total += nums[i]

        even_left = 0
        odd_left = 0
        answer = 0

        for i in range(len(nums)):

            # Remove nums[i] from the right side
            if i % 2 == 0:
                even_total -= nums[i]
            else:
                odd_total -= nums[i]

            # After removing nums[i],
            # right-side indexes change parity.
            even_sum = even_left + odd_total
            odd_sum = odd_left + even_total

            if even_sum == odd_sum:
                answer += 1

            # Add current element to left side
            if i % 2 == 0:
                even_left += nums[i]
            else:
                odd_left += nums[i]

        return answer
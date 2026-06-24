class Solution(object):

    def minEatingSpeed(self, piles, h):

        # Minimum possible speed
        left = 1

        # Maximum possible speed
        right = 1000000000

        # Binary Search
        while left < right:

            # Middle speed
            mid = left + (right - left) // 2

            # Total hours needed
            total = 0

            for num in piles:

                # Ceiling Division
                total += (num + mid - 1) // mid

            # Too slow
            if total > h:
                left = mid + 1

            # Can finish, try smaller speed
            else:
                right = mid

        return left

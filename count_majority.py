class Solution(object):

    def countMajoritySubarrays(self, nums, target):

        # Stores total number of valid subarrays
        total_count = 0

        # Choose starting index of subarray
        for i in range(len(nums)):

            # Count occurrences of target in current subarray
            ans = 0

            # Extend subarray from i to j
            for j in range(i, len(nums)):

                # If current element equals target
                if nums[j] == target:
                    ans += 1

                # Current subarray length
                length = j - i + 1

                # Check if target is majority element
                # Majority means frequency > length // 2
                if ans > length // 2:

                    # Count this subarray
                    total_count += 1

        # Return total valid subarrays
        return total_count

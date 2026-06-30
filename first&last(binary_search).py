class Solution(object):

    # Function to find the first occurrence of the target
    def first(self, nums, target):

        # Initialize binary search pointers
        left, right = 0, len(nums) - 1

        # Store answer (-1 if target is not found)
        store = -1

        # Perform binary search
        while left <= right:

            # Calculate middle index
            mid = left + (right - left) // 2

            # Target found
            if nums[mid] == target:

                # Save current index
                store = mid

                # Continue searching on the left side
                # to find the first occurrence
                right = mid - 1

            # Target is smaller than middle element
            elif nums[mid] > target:

                # Search left half
                right = mid - 1

            # Target is greater than middle element
            else:

                # Search right half
                left = mid + 1

        # Return first occurrence index
        return store


    # Function to find the last occurrence of the target
    def last(self, nums, target):

        # Initialize binary search pointers
        left, right = 0, len(nums) - 1

        # Store answer (-1 if target is not found)
        store = -1

        # Perform binary search
        while left <= right:

            # Calculate middle index
            mid = left + (right - left) // 2

            # Target found
            if nums[mid] == target:

                # Save current index
                store = mid

                # Continue searching on the right side
                # to find the last occurrence
                left = mid + 1

            # Target is smaller than middle element
            elif nums[mid] > target:

                # Search left half
                right = mid - 1

            # Target is greater than middle element
            else:

                # Search right half
                left = mid + 1

        # Return last occurrence index
        return store


    # Main function
    def searchRange(self, nums, target):

        # Return first and last occurrence
        return (self.first(nums, target), self.last(nums, target))

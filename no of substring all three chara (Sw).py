class Solution(object):

    # Function to count the number of substrings
    # containing at least one 'a', one 'b', and one 'c'
    def numberOfSubstrings(self, s):
        def back(s,left,max_sum):

        # Dictionary to store the count of each character
        char = {'a': 0, 'b': 0, 'c': 0}

        # Left pointer of the sliding window
        left = 0

        # Variable to store the total number of valid substrings
        max_sum = 0

        # Expand the sliding window
        for right in range(len(s)):

            # Include the current character in the window
            char[s[right]] += 1

            # If the current window contains all three characters
            while char['a'] > 0 and char['b'] > 0 and char['c'] > 0:

                # All substrings from 'right' to the end are valid
                max_sum += len(s) - right

                # Remove the leftmost character
                char[s[left]] -= 1

                # Shrink the window
                left += 1

        # Return the total number of valid substrings
        return max_sum
    return back(s,0,0)

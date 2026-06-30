class Solution(object):

    # Function to find the number of days until a warmer temperature
    def dailyTemperatures(self, temperatures):

        # Stack stores the indices of temperatures
        stack = []

        # Initialize answer array with 0
        ans = [0] * len(temperatures)

        # Traverse from right to left
        for i in range(len(temperatures) - 1, -1, -1):

            # Remove all temperatures that are
            # smaller than or equal to the current temperature
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            # If stack is not empty,
            # calculate the number of waiting days
            if stack:
                ans[i] = stack[-1] - i

            # Otherwise, no warmer temperature exists
            else:
                ans[i] = 0

            # Push the current index onto the stack
            stack.append(i)

        # Return the final answer
        return ans

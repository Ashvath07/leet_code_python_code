class Solution:
    def sortByBits(self, arr):
        # Sort the array based on:
        # 1️⃣ Number of 1's in binary representation
        # 2️⃣ If bit count is same, then sort by number value
        
        result = sorted(
            arr, 
            key=lambda x: (bin(x).count('1'), x)
        )
        
        # Return the sorted result
        return result

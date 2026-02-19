class Solution(object):
    def countBinarySubstrings(self, s):
        
        S = str(s)   # Convert input to string (not really needed if s is already string)
        
        count = 1    # To count consecutive same characters
        groups = []  # To store lengths of consecutive groups
        
        # Step 1: Count consecutive 0s or 1s
        for i in range(1, len(S)):
            
            if s[i] == s[i-1]:   # If current char same as previous
                count += 1       # Increase group count
            else:
                groups.append(count)  # Store completed group length
                count = 1            # Reset count for new group
        
        groups.append(count)  # Append last group
        
        # Step 2: Count valid substrings
        result = 0
        
        for i in range(1, len(groups)):
            # Add minimum of adjacent groups
            # Because balanced substring depends on smaller group
            result += min(groups[i-1], groups[i])
        
        return result   # Return total count

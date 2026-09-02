class Solution(object):

    def magicalString(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 3:
            return 1

        # Initial prefix of the magical string
        s = [1, 2, 2]
        head = 2  # Pointer indicating group length for next element(s)
        num = 1  # Next number to append (alternates between 1 and 2)

        while len(s) < n:
            # Append `num` repeated `s[head]` times
            s.extend([num] * s[head])

            # Alternate num between 1 and 2 (1 ^ 3 = 2, 2 ^ 3 = 1)
            num ^= 3

            # Move pointer to the next group length instruction
            head += 1

        # Count 1s in the first n elements
        return s[:n].count(1)
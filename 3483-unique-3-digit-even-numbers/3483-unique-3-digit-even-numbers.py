class Solution(object):
    def totalNumbers(self, digits):
        freq = set()
        for i,j,k in permutations(digits,3):
            if i != 0 and k%2 == 0:
                freq.add((i,j,k))
        return len(freq)

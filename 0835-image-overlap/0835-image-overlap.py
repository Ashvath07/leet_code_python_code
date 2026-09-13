class Solution(object):
    def largestOverlap(self, img1, img2):
        N = len(img1)
        ones1 = [(r, c) for r in range(N) for c in range(N) if img1[r][c] == 1]
        ones2 = [(r, c) for r in range(N) for c in range(N) if img2[r][c] == 1]

        shift_counts = defaultdict(int)
        for r1, c1 in ones1:
            for r2, c2 in ones2:
                shift_counts[(r1 - r2, c1 - c2)] += 1

        return max(shift_counts.values()) if shift_counts else 0
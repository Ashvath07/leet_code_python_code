class Solution(object):
    def largestOverlap(self, img1, img2):
        n = len(img1)
        best =0
        for i in range(-n+1,n):
            for j in range(-n+1,n):
                score =0
                for m in range(n):
                    for o in range(n):
                        c =0
                        if 0 <= i+m < n and 0 <= j+o<n:
                            c = img1[i+m][j+o]
                        score += img2[m][o] & c
                best = max(best,score)
        return best
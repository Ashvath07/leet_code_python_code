class Solution(object):
    def judgeSquareSum(self, c):
        left =0
        right = int(math.sqrt(c))
        while left<=right:
            store = left*left+right*right
            if store == c:
                return True
            elif store < c:
                left+=1
            else:
                right-=1
        return False
        
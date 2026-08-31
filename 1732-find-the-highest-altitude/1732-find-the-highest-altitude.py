class Solution(object):
    def largestAltitude(self, gain):
        a=0
        m=0
        for i in gain:
            a+=i
            m = max(m,a)
        return m
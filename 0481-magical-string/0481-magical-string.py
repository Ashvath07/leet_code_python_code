class Solution(object):
    def magicalString(self, n):
        if n<=3:
            return 1
        else:
            s="122"
            i=len(s)-1
            while True:
                if s[-1]=='2':
                    s=s+('1'*int(s[i]))

                else:
                    s=s+('2'*int(s[i]))
                if len(s)>=n:
                    break
                i=i+1
            s=s[:n]
            return s.count('1')
        
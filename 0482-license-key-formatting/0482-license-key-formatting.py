class Solution(object):
    def licenseKeyFormatting(self, s, k):
        s = s.replace("-","").upper()
        first=len(s)%k
        result =[]
        if first:
            result.append(s[:first])
        for i in range(first,len(s),k):
            result.append(s[i:i+k])
        return "-".join(result)
class Solution(object):
    def characterReplacement(self, s, k):
        count=defaultdict(int)
        max_count=0
        left=0
        for right, c in enumerate(s):
            count[c]+=1
            if count[c]>max_count:
                max_count=count[c]
            elif right-left+1>max_count+k:
                left+=1
                count[s[left-1]]-=1
        return len(s)-left   
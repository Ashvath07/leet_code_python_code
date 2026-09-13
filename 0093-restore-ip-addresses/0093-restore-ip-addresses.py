class Solution(object):
    def restoreIpAddresses(self, s):
        result = []
        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return
            for end in range(start + 1, min(start + 3, len(s)) + 1):
                part = s[start:end]
                if len(part) > 1 and part[0] == '0':
                    continue
                if int(part) > 255:
                    continue
                backtrack(end, parts + [part])
        backtrack(0, [])
        return result
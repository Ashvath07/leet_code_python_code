class Solution(object):
    def minAddToMakeValid(self, s):
        open_count = 0
        count = 0

        for ch in s:
            if ch == '(':
                open_count += 1
            else:
                if open_count > 0:
                    open_count -= 1
                else:
                    count += 1

        return count + open_count
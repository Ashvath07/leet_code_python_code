from collections import Counter

class Solution(object):
    def lexGreaterPermutation(self, s, target):
        compare = ''.join(sorted(s))
        if compare > target:
            return compare
        
        compare = compare[::-1]
        if compare <= target:
            return ""

        counts = Counter(s)
        mirror_idx = 0

        for c in target:
            if counts[c] > 0:
                mirror_idx += 1
                counts[c] -= 1
            else:
                break

        if mirror_idx == len(target):
            mirror_idx -= 1
            counts[target[-1]] += 1

        iterate = sorted(counts.keys())
        res = ""

        def sorted_counts(counts):
            temp = ""
            for k in iterate:
                temp += k * counts[k]
            return temp
        
        for s_idx in range(mirror_idx, -1, -1):
            for key in iterate:
                if key > target[s_idx] and counts[key] > 0:
                    res = target[:s_idx]
                    res += key
                    counts[key] -= 1
                    res += sorted_counts(counts)
                    return res

            counts[target[s_idx - 1]] += 1

        return ""
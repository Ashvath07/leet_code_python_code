class Solution:
    def lexGreaterPermutation(self, s, target):
        cnt = [0] * 26
        for c in s:
            cnt[ord(c) - 97] += 1

        pre = []

        for i in range(len(s)):
            x = ord(target[i]) - 97

            if cnt[x]:
                cnt[x] -= 1
                pre.append(target[i])
            else:
                break

        for i in range(len(pre), -1, -1):
            if i < len(pre):
                cnt[ord(pre.pop()) - 97] += 1

            x = ord(target[i]) - 97 if i < len(target) else 26

            for c in range(x + 1, 26):
                if cnt[c]:
                    cnt[c] -= 1
                    return ''.join(pre) + chr(c + 97) + ''.join(
                        chr(j + 97) * cnt[j] for j in range(26)
                    )

        return ""
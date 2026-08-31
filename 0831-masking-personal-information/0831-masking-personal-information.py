class Solution(object):

    def maskPII(self, s):
        if '@' in s:
            s = s.lower()

            name, domain = s.split('@')

            return name[0] + "*****" + name[-1] + "@" + domain

        else:
            digits = ""

            for ch in s:
                if ch.isdigit():
                    digits += ch

            last4 = digits[-4:]

            if len(digits) == 10:
                return "***-***-" + last4
            else:
                country = len(digits) - 10
                return "+" + "*" * country + "-***-***-" + last4
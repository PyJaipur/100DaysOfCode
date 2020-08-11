# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        final = []
        balance = 0
        i = 0
        oidx = list()
        cidx = list()
        while i < len(s):
            c = s[i]
            if c == "(":
                balance += 1
                oidx.append(len(final))
            elif c == ")" and balance <= 0:
                i += 1
                continue
            elif c == ")" and balance > 0:
                balance -= 1
                cidx.append(len(final))
            final.append(c)
            i += 1
        if balance < 0:  # more ) than (
            while balance != 0:
                final.pop(cidx.pop(0))
                balance += 1
        if balance > 0:  # more ( than )
            while balance != 0:
                final.pop(oidx.pop(-1))
                balance -= 1
        return "".join(final)

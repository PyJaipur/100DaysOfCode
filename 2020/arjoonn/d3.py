# https://leetcode.com/problems/remove-comments/
def fn(source):
    o, s, e = "//", "/*", "*/"
    in_block = False
    buf = []
    for line in source:
        i = 0
        l = len(line)
        while i < l:
            c = line[i]
            if not in_block and c == "/" and i + 1 < l and line[i + 1] == "/":
                break
            if not in_block and c == "/" and i + 1 < l and line[i + 1] == "*":
                in_block = True
                i += 2
                continue
            if in_block and c == "*" and i + 1 < l and line[i + 1] == "/":
                in_block = False
                i += 2
                continue
            if not in_block:
                buf.append(c)
            i += 1
        if buf and not in_block:
            yield "".join(buf)
            buf = []


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        return list(fn(source))

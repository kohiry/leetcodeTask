class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = [i for i in t if i in s]
        i, j = 0, 0
        while i < len(s):
            if s[i] != l[j]:
                j += 1
            else:
                j += 1
                i += 1
        return "".join(l) == s

class Solution:
    def reverseVowels(self, s: str) -> str:
        v = []
        for i in range(len(s)):
            for j in range(len(s)-1, -1,-1):
                if i == j:
                    return s
                if s[i]


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        curr = 0
        for i, v in enumerate(s):
            if i >= k:
                if s[i - k] in "aeiou":
                    curr -= 1
            if v in "aeiou":
                curr += 1
            res = max(res, curr)
        return res


test_case = [
    (("uaiptsvkdadtefchtnftwjepohdfvgn", 24), 6),
]


for test, answer in test_case:
    print(Solution().maxVowels(test[0], test[1]), answer)

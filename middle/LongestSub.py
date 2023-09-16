"""Given a string s, find the length of the longest.

substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        if l == 0:
            return 0
        dicts = {}
        max_len = 0
        start = 0
        for i in range(l):
            print(dicts)
            if s[i] in dicts and start <= dicts[s[i]]:
                start = dicts[s[i]] + 1
                print(start, "|")
            else:
                max_len = max(max_len, i - start + 1)
                print(max_len, "/")
            dicts[s[i]] = i
        return max_len


test _case = [
    # ("abcabcbb", 3),
    ("bbbbb", 1),
    # ("pwwkew", 3),
    # ("dvdf", 3),
    # ("anviaj", 5),
    ("asjrgapa", 6),
]

for test, answer in test_case:
    print(Solution().lengthOfLongestSubstring(test) == answer)

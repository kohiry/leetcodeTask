from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


test_case = [["flower", "flow", "flight"], ["dog", "racecar", "car"]]
for test in test_case:
    print(Solution().longestCommonPrefix(test))
    # Solution().longestCommonPrefix(test)

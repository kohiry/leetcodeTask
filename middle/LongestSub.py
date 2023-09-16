""" Given a string s, find the length of the longest
substring
without repeating characters."""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        new_s = ""
        count = 0
        for letter in s:
            new_s = new_s + letter if letter not in new_s else letter
            if len(new_s) > count:
                count += 1
        return count

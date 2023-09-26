from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr):
        vs = [v for v in Counter(arr).values()]
        return len(vs) == len(set(vs))

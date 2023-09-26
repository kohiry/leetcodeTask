from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        left, maxx = 0, 0
        for i in gain:
            maxx = max(left, maxx)
            left += i
        return max(left, maxx)

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            area = (r - l) * (min(height[l], height[r]) ** 2)
            max_area = max(max_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area


test_case = [
    ([1, 2, 1], 2),
]

for test, answer in test_case:
    print(Solution().maxArea(test), answer)
    assert Solution().maxArea(test), answer

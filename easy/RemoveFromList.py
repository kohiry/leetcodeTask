from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)


test_case = [
    ([3, 2, 2, 3], 2),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2),
    ([3, 2, 2, 3], 3),
    ([2, 2, 3], 2),
    ([0, 4, 4, 0, 4, 4, 4, 0, 2], 4),
]
for test, val in test_case:
    k = Solution().removeElement(test, val)
    print(test, k)

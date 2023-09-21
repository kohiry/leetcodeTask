from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        M = d = 0
        for i in range(len(nums) - k):
            d += nums[i + k] - nums[i]
            if d > M:
                M = d
        return (sum(nums[:k]) + M) / k


test_case = [
    (([0, 1, 1, 3, 3], 4), 2.0),
    (([4, 2, 1, 3, 3], 2), 3.0),
]


for test, answer in test_case:
    print(Solution().findMaxAverage(test[0], test[1]), answer)

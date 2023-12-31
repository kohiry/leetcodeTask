from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = r = 0
        for r in range(len(nums)):
            print(f"{r}) r={r} k={k} l={l}")
            if nums[r] == 0:
                k -= 1
            if k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
        return r - l + 1


test_case = [
    (([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6),
]

for test, answer in test_case:
    res = Solution().longestOnes(test[0], test[1])
    print(res, answer)
    assert res == answer

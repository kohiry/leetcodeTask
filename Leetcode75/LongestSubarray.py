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
    ([1, 1, 0, 1], 3),
    ([1, 1, 1], 2),
    ([0, 1, 1, 1, 0, 1, 1, 0, 1], 5),
]

for test, answer in test_case:
    res = Solution().longestSubarray(test)
    print(res, answer)
    assert res == answer

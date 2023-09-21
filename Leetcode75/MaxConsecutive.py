class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        curr = res = 0
        print(nums)
        for i in nums:
            if i == 0:
                curr = 0
                res = max(curr, res)
            else:
                curr += 1

        return max(curr, res)

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]

        for k in range(i + 1, len(nums)):
            nums[k] = 0

        return i + 1


test_case = [
    ([1, 1, 2], [1, 2, 0]),
    ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 3, 4], [0, 1, 2, 3, 4, 0, 0, 0, 0, 0, 0]),
]
for test, answer in test_case:
    start_test = len(list(set(test.copy())))
    k = Solution().removeDuplicates(test)
    print(k, test, start_test)
    assert k == start_test
    for i in range(k):
        assert test[i] == answer[i]

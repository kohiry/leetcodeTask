from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # return ([int(letter) for letter in str(sum([digits[i] * 10 ** abs(i - len(digits) + 1) for i in range(len(digits))]) + 1)])
        nums = digits[0]
        for i in digits[1:]:
            nums = nums * 10 + i
        return [int(i) for i in list(str(nums + 1))]


test_case = [
    ([1, 2, 3], [1, 2, 4]),
    ([4, 3, 2, 1], [4, 3, 2, 2]),
    ([9], [1, 0]),
]

for test, answer in test_case:
    print(Solution().plusOne(test), answer)
    assert Solution().plusOne(test) == answer

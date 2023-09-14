class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)
        return str(bin(a + b))[2:]


# test_case = [
#     ([1, 2, 3], [1, 2, 4]),
#     ([4, 3, 2, 1], [4, 3, 2, 2]),
#     ([9], [1, 0]),
# ]

# for test, answer in test_case:
#     print(Solution().plusOne(test), answer)
#     assert Solution().plusOne(test) == answer

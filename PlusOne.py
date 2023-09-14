class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        print([digits[i] * 10**i for i in range(len(digits))])

        # return [
        #     int(j)
        #     for j in str(sum([digits[i] * 10**i for i in range(len(digits))]) + 1)
        # ]

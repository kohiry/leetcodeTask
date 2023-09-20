class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        i = 0
        while i < len(nums):
            j = 0
            v = 1
            while j < len(nums):
                if j != i:
                    v *= nums[j]
                j += 1
            answer.append(v)
            i += 1
        return answer

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer = []
        for i in range(0, len(nums)):
            for j in range(1, len(nums)):
                if i != j and nums[i] + nums[j] == target:
                    answer = [i, j]
                    break
            if answer:
                break
        return answer


print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))

class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        while num != 0:
            step += 1
            num -= num // 2 if num % 2 == 0 else 1
        return step

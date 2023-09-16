from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        i = 1
        while i <= n:
            if i % 5 == 0 and i % 3 == 0:
                answer.append("FizzBuzz")
            elif i % 5 == 0:
                answer.append("Buzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            else:
                answer.append(str(i))
            i += 1
        return answer

class Solution(object):
    def __init__(self):
        self.reverse_number = 0

    def count(self, x):
        """
        :type x: int
        :rtype: int
        """
        count = 1
        x_abs = abs(x)
        while x_abs // 10 > 0:
            count += 1
            x_abs = x_abs // 10
        return count

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        length = self.count(x)
        count_n = length
        while count_n > 0:
            count_n -= 1
            if x % 10 > 0:
                self.reverse_number += (x // (10**count_n)) * (
                    10 ** (length - 1 - count_n)
                )
                x = x % (10**count_n)
                # print(x, count_n)
            else:
                break
        return int(self.reverse_number)

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        print(x, self.reverse(x))
        return x == self.reverse(x)


print(Solution().isPalindrome(-1))

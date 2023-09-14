class Solution(object):
    data = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def next_roman(self, letter, next_letter):
        data_keys = list(self.data.keys())

        for i in range(len(data_keys)):
            if (
                i + 1 != len(data_keys)
                and letter == data_keys[i]
                and next_letter == data_keys[i + 1]
            ):
                return True
            elif (
                i + 2 < len(data_keys)
                and letter == data_keys[i]
                and next_letter == data_keys[i + 2]
            ):
                return True

        return False

    def minus_number(self, number):
        if "5" in str(number):
            return 0.8
        else:
            return 0.9

    def romanToInt(self, s):
        next_smal = False
        result = 0
        for i in range(len(s)):
            if next_smal:
                next_smal = False
                result += self.data[s[i]] * self.minus_number(self.data[s[i]])
            elif i + 1 != len(s) and self.next_roman(s[i], s[i + 1]):
                next_smal = True
            else:
                result += self.data[s[i]]

        return int(result)


test_1: str = "III"
test_2: str = "LVIII"
test_3: str = "MCMXCIV"
test_cases = [test_1, test_2, test_3]

for i in test_cases:
    print(Solution().romanToInt(i))

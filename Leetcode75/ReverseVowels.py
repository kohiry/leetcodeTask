class Solution:
    def reverseVowels(self, s: str) -> str:

        sets = {'a','e','i','o','u','A','E','I','O','U'}
        sets = set(sets)
        i, j = 0, len(s) - 1
        x = [*s]
        while i < j:
            if x[i] not in sets:
                i += 1
            if x[j] not in sets:
                j -= 1

            elif x[i] in sets and x[j] in sets:
                x[i], x[j] = x[j], x[i]
                i += 1
                j -= 1

        return "".join(x)

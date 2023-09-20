class Solution:
    def compress(self, chars: List[str]) -> int:
        d = {}
        for i in chars:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        print(d)
        chars.clear()
        print(chars)
        for i in [j for j in "".join([c + str(d[c]) for c in d.keys()])]:
            chars.append(i)
        return len(chars)

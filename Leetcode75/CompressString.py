class Solution:
    def compress(self, chars: List[str]) -> int:
        count = 1
        cl = []
        for i in range(0, len(chars)):
            if i > 0 and chars[i - 1] == chars[i]:
                count += 1
                if i == len(chars) - 1:
                    cl.append(str(count))
            else:
                if count > 1:
                    cl.append(str(count))
                cl.append(chars[i])
                count = 1
        chars.clear()
        for c in "".join(cl):
            chars.append(c)
        return len(chars)

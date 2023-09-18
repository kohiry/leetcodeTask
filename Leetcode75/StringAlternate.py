class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l_s = len(word1) + len(word2)
        s = ""
        if l_s == 0:
            return ""
        wi, wj = 0, 0
        for i in range(l_s):
            if i % 2 == 0 and wi < len(word1):
                s += word1[wi]
                wi += 1
            elif wi == len(word1):
                s += word2[wj]
                wj += 1
            elif i % 2 != 0 and wj < len(word2):
                s += word2[wj]
                wj += 1
            elif wj == len(word2):
                s += word1[wi]
                wi += 1
        return s

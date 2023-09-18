class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minn = min(len(word1), len(word2))
        return (
            "".join([word1[i] + word2[i] for i in range(0, minn)])
            + word1[minn:]
            + word2[minn:]
        )

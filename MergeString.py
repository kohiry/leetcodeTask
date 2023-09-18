class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word = ""
        replaced = lambda x: (i for i in x)
        count = 0
        while True:
            letter1, letter2 = replaced(word1).__next__(), replaced(word2).__next__()
            count += 1
            word += letter1 if count % 2 == 0 else letter2
            if not letter1 and not letter2:
                break
        return word

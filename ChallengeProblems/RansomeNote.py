class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in ransomNote:
            index = magazine.find(i)
            if index == -1:
                return False
            magazine = magazine.replace(magazine[index], "", 1)
        return True

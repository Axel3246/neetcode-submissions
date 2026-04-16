class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmapA = {}
        hmapB = {}

        for char in s:
            hmapA[char] = hmapA.get(char, 0) + 1
        
        for char in t:
            hmapB[char] = hmapB.get(char, 0) + 1
        
        return hmapA == hmapB




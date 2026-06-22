class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        v1 = sorted(Counter(word1).values())
        v2 = sorted(Counter(word2).values())

        if v1 != v2:
            return False

        #print(set(word1))
        if set(word1) == set(word2):
            return True 
        return False
        
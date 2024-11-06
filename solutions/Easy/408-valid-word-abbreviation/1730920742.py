class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:


        j = i = 0
        n = len(abbr)
        while i < n:
            if j == len(word):
                return False
            if abbr[i].isalpha():
                if abbr[i] != word[j]:
                    return False
                i+=1
                j+=1
            else:
                start = i
                if abbr[i] == '0':
                    return False
                while i < n and not abbr[i].isalpha():
                    i+=1
                m = int(abbr[start:i])
                if j + m > len(word):
                    return False
                j+=m
        return j == len(word)

        
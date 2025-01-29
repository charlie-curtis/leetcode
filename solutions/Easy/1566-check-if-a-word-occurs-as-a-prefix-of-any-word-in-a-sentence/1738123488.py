class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        for i,x in enumerate(sentence.split(" ")):
            if x.find(searchWord) == 0:
                return i+1
        return -1
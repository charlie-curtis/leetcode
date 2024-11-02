class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        split = sentence.split(" ")
        n = len(split)
        for i in range(n):
            if split[i][-1] != split[(i+1)%n][0]:
                return False
        return True
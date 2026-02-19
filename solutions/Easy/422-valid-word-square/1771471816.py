class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        candidate = []
        n = max([len(words)] + [len(x) for x in words])

        for i in range(n):
            for j in range(n):
                a_valid = (i < len(words)) and (j < len(words[i]))
                b_valid = (j < len(words)) and (i < len(words[j]))
                if a_valid != b_valid:
                    return False
                if a_valid and words[i][j] != words[j][i]:
                    return False
        return True
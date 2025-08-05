class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        n = len(score)
        out = [0]*n
        A = [[-x, i] for i,x in enumerate(score)]
        A.sort()
        for i in range(len(A)):
            _, idx = A[i]
            if i == 0:
                out[idx] = "Gold Medal"
            elif i == 1:
                out[idx] = "Silver Medal"
            elif i == 2:
                out[idx] = "Bronze Medal"
            else:
                out[idx] = str(i+1)
        return out

        
class Solution:
    def peopleIndexes(self, favorite: List[List[str]]) -> List[int]:

        A = [set(x) for i,x in enumerate(favorite)]


        out = []
        for i in range(len(A)):
            good = True
            s1 = A[i]
            for j in range(len(A)):
                if i == j:
                    continue
                s2 = A[j]
                if len(s1 - s2) == 0:
                    good = False
                    break
            if good:
                out.append(i)
        return out
        
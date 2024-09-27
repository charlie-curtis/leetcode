class Solution:
    def fourSum(self, A: List[int], target: int) -> List[List[int]]:

        A.sort()

        out = set()
        n = len(A)
        for i in range(n):
            for j in range(i+1, n-2):

                lookingFor = target - A[i] - A[j]

                l = j+1
                r = len(A)-1
                while l < r:
                    q = [A[i], A[j], A[l], A[r]]

                    if A[l] + A[r] == lookingFor:
                        t = tuple(sorted(q))
                        out.add(t)
                    if A[l] + A[r] > lookingFor:
                        r-=1
                    else:
                        l+=1
        return [list(x) for x in out]

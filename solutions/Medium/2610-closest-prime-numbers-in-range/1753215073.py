cutoff = (10**6)
P = [True]*(cutoff+1)
P[0] = P[1] = False
i = 2
for i in range(2, int(sqrt(cutoff)) +1):
    if P[i]:
        for j in range(2, int(cutoff//i)+1):
            P[i*j] = False
A = [i for i,x in enumerate(P) if x]
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        i = bisect_left(A, left)
        n = len(A)
        ans = [-1,-1]
        while i+1 < n and A[i+1] <= right:
            if ans == [-1, -1] or (ans[1] - ans[0]) > A[i+1] - A[i]:
                ans = [A[i], A[i+1]]
            i+=1
        return ans


        
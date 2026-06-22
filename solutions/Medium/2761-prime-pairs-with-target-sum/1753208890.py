cutoff = (10**6)
P = [True]*(cutoff+1)
P[0] = P[1] = False
i = 2
for i in range(2, int(sqrt(cutoff)) +1):
    if P[i]:
        for j in range(2, int(cutoff//i)+1):
            P[i*j] = False
A = [i for i in range(cutoff+1) if P[i]]
class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:

        out = []
        for x in A:
            y = n-x
            if x > y:
                break
            if P[y]:
                out.append([x,y])
        return out
            
        
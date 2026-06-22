#999,999
cut = 1000000
P = [True]*cut
i = 2
while i*i <= cut:
    if P[i]:
        j = 2
        while j*i < cut:
            P[j*i] = False
            j+=1
    i+= (1 if i % 2 == 0 else 2)
class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:

        m,n = len(mat), len(mat[0])

        C = Counter()

        def bt(i,j, dx,dy):

            v = ""
            while min(i,j) >= 0 and i < m and j < n:
                v = int(str(v) + str(mat[i][j]))
                C[v]+=1
                i+=dx
                j+=dy


        for i in range(m):
            for j in range(n):
                for dx in range(-1,2):
                    for dy in range(-1,2):
                        if dx == dy == 0:
                            continue
                        bt(i,j,dx,dy)
        

        A = sorted([-v,-k] for (k,v) in C.items())

        for _,k in A:
            k = -k
            if P[k] and k >= 10:
                return k
        return -1
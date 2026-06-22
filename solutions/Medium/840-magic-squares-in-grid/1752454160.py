class Solution:
    def numMagicSquaresInside(self, g: List[List[int]]) -> int:

        m,n= len(g),len(g[0])
        ans=0
        for i in range(0,m-2):
            for j in range(0,n-2):
                R = Counter()
                C = Counter()
                diag = 0
                antidiag = 0
                seen = set()
                for k in range(3):
                    for l in range(3):
                        seen.add(g[i+k][l+j]) #unique set
                        R[k]+=g[i+k][l+j] #row sums
                        C[l]+=g[i+k][l+j] #col sums
                        if l == k:
                            diag+=g[i+k][l+j]
                        #[0,2], [1,1], [2,0]
                        if l + k == 2:
                            antidiag+=g[i+k][l+j]

                good = diag == 15 and antidiag == 15 and len(seen) == 9
                good&=max(seen) == 9 and min(seen) == 1
                good&= min(R.values()) == 15 and max(R.values()) == 15
                good&= min(C.values()) == 15 and max(C.values()) == 15
                ans+=int(good)

        return ans
        
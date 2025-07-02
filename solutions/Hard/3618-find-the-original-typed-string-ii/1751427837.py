class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:

        #editorial - hard problem that i didn't fully get the implementation down for. had trouble visualizing.


        #iterate through all the characters, grouped.
        #if a groups size is > 1, then you can reduce it, but you need
        #to make sure the overall size is >=k at the end

        #so if i have aaaaaaaaab, k = 2, i can reduce the a's

        # [8,1]
        A = []
        for _, g in groupby(word):
            A.append(len(list(g)))

        n = len(A)
        MOD = 10**9 + 7

        multi = 1
        for x in A:
            multi*=x
            multi%=MOD
        if n >= k:
            #there are enough runs to always form a string of atleast length k -- even if we reduce
            #each run to length = 1
            return multi
        
        #there isn't room to always form a multi of length=k, so we're going to have to subtract the
        #runs [0...k-1] as those are currently being counted in `multi`

        #f(i,j) - number of ways to form a string of length j using the prefix [0,i-1]
        f = [[0 for _ in range(k)] for _ in range(n+1)]

        f[0][0] = 1

        prev = [1] *k
        for i in range(1,n+1):
            for j in range(k):
                p = A[i-1]

                idx1 = j-1
                idx2 = j-p-1
                v1 = prev[idx1] if idx1 >= 0 else 0
                v2 = prev[idx2] if idx2 >= 0 else 0
                f[i][j] = (v1 - v2) % MOD

            prev = [0]*k
            prev[0] = f[i][0]
            for t in range(1,k):
                prev[t] = prev[t-1] + f[i][t]
                prev[t]%=MOD

        
        return (multi - prev[k-1]) % MOD

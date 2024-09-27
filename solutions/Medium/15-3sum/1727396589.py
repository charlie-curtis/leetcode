class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:

        seen = set()
        ans = set()
        C = Counter()
        f = []
        for x in A:
            if C[x] <3:
                f.append(x)
            C[x]+=1
        
        A = f
        n = len(A)
        for i in range(n):
            for j in range(i+1, n):
                ssum = A[i] + A[j]
                if -ssum in seen:
                    k = tuple(sorted([A[i], A[j], -ssum]))
                    if k not in ans:
                        ans.add(k)
            seen.add(A[i])

        return [list(t) for t in ans]
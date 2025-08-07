class Solution:
    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        
        #Use rolling hash + dfs to compute palindromes
        n = len(parent)
        children = defaultdict(list)
        for i in range(n): #O(N)
            children[parent[i]].append(i)
        
        MOD = 10**9 + 7
        ans = [-1]*n
        H = defaultdict(set)
        def compute(node):
            cur = 0
            sz = 1
            for x in children[node]:
                t,L = compute(x)
                cur = cur*pow(26*31,L, MOD) + t
                cur%=MOD
                sz+=L
            cur = cur*26*31 + ord(s[node]) - ord('a')
            cur%=MOD

            H[node].add(cur)
            return [cur, sz]
        

        def rev_compute(node):
            cur = ord(s[node]) - ord('a')
            sz = 1
            for x in reversed(children[node]):
                t, L = rev_compute(x)
                cur = cur*pow(26*31,L, MOD) + t
                cur%=MOD
                sz+=L
            H[node].add(cur)
            return [cur, sz]
        
        compute(0)
        rev_compute(0)
        return [len(H[i]) == 1 for i in range(n)]
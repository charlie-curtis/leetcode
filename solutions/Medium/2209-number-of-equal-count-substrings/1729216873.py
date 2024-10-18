class Solution:
    def equalCountSubstrings(self, s: str, k: int) -> int:

        d = defaultdict(list)
        n = len(s)

        def check(t):
            j = 0
            C = Counter()
            ans = 0
            for i in range(n):
                v = s[i]

                C[v]+=1

                while C[v] > k or (s[j] != t and j < i):
                    C[s[j]]-=1
                    j+=1

                if C[v] == k and s[j] == t:
                    good = True
                    for v in C.values():
                        if v != k and v != 0:
                            good = False
                            break
                    if good:
                        ans+=1
            return ans

            
        ans = 0
        for i in range(26):
            ans+=check(chr(ord('a') + i))
        return ans

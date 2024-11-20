class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        allowance = Counter()
        allowance['a'] = s.count('a') - k
        allowance['b'] = s.count('b') - k
        allowance['c'] = s.count('c') - k
        j = 0
        n = len(s)
        C = Counter()
        def invalid():
            for x in ['a', 'b', 'c']:
                if C[x] > allowance[x]:
                    return True
            return False

        best_deletes = -1 
        for i in range(n):
            C[s[i]]+=1

            while invalid() and j <= i:
                C[s[j]]-=1
                j+=1
            
            sz = i-j+1
            if not invalid():
                best_deletes = max(best_deletes, i-j+1)


        if best_deletes == -1:
            return -1
        return n - best_deletes

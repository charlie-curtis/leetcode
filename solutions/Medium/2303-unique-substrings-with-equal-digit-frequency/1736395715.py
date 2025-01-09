class Solution:
    def equalDigitFrequency(self, s: str) -> int:


        n = len(s)
        seen = set()

        def good(C):
            return len(set(C.values())) == 1
        def getKey(start,end):
            return hash(s[start:end+1])

        def count_for_size(k):
            C = Counter()
            j = 0
            for i in range(n):
                C[s[i]]+=1

                if i-j+1 > k:
                    C[s[j]]-=1
                    if C[s[j]] == 0:
                        del C[s[j]]
                    j+=1

                if i-j+1 == k and good(C):
                    kkey = getKey(j,i)
                    seen.add(kkey)


        for i in range(1,n+1):
            count_for_size(i)

        return len(seen)

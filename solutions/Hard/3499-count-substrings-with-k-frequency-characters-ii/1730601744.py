class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:


        n = len(s)

        ans = 0

        C = Counter()
        def is_good(C, letter):
            return C[letter] >=k
        j = 0
        for i in range(n):
            C[s[i]]+=1

            while is_good(C, s[i]):
                ans+=n-i
                C[s[j]]-=1
                j+=1

        return ans


        
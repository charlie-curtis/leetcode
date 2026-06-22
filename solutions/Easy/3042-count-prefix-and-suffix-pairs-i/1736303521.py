class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        n = len(words)
        ans=0
        for i in range(n):
            for j in range(i):
                short = words[j]
                llong = words[i]
                l = llong.find(short)
                r = llong.rfind(short)
                if l == -1 or r == -1:
                    continue
                if l == 0 and r == len(llong) - len(short):
                    ans+=1
        return ans
        
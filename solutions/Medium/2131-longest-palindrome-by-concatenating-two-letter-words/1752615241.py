class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        C = Counter()
        ans = 0
        for s in words:
            t = s[::-1]
            if C[t] > 0:
                C[t]-=1
                ans+=4
            else:
                C[s]+=1
        
        for k,v in C.items():
            if k == k[::-1] and v > 0:
                ans+=2
                return ans
        return ans
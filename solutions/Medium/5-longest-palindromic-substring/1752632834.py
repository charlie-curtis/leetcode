class Solution:
    def longestPalindrome(self, s: str) -> str:
        #there is an algo that solves this in O(n) but is not worth trying to learn. maybe tempating for contests at best
        n=len(s)
        def check(i,off):
            j=i+off
            while i >=0 and j < n and s[i] == s[j]:
                i-=1
                j+=1
            return [j-i-1, s[i+1:j]]

        a=max([check(i,0) for i in range(n)])
        b=max([check(i,1) for i in range(n)])

        if b[0] > a[0]: return b[1]
        return a[1]
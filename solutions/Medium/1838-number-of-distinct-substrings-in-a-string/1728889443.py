class Solution:
    def countDistinct(self, s: str) -> int:

        n = len(s)
        ans = set()
        for i in range(1,n+1):
            for j in range(n-i+1):
                ans.add(s[j:j+i])

        return len(ans) 
        
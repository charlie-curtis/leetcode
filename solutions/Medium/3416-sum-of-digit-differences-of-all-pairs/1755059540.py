class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:

        C = Counter()
        mx = 0
        for x in nums:
            s = str(x)[::-1]
            n = len(s)
            for i in range(n):
                mx = max(i,mx)
                C[(i,int(s[i]))]+=1

        
        ans = 0
        for i in range(mx+1):
            for j in range(0,10):
                for k in range(j+1,10):
                    ans+=C[(i,j)]*C[(i,k)]
        return ans
        



        
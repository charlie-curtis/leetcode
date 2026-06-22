class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n= len(s)
        zeros, ones = s.count('0'), 0
        ans = float('inf')
        for x in s:
            if x == '0':
                zeros-=1
            ans=min(ans,zeros+ones)
            if x == '1':
                ones+=1
        return ans
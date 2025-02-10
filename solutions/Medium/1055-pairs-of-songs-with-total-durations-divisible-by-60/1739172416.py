class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time=[x%60 for x in  time]
        C=Counter()
        ans=0
        for x in time:
            ans+=C[(60-x)%60]
            C[x]+=1
        return ans
        
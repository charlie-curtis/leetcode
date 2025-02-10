class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ssum,d=0,{0:-1}
        ans=0
        b=0
        for i,x  in  enumerate(nums):
            if x == 0:b+=1
            else:b-=1
            if b in d: ans=max(ans,i-d[b])
            else: d[b]=i
        return ans
                
            
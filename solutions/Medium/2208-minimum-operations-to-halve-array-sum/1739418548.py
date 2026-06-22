class Solution:
    def halveArray(self, nums: List[int]) -> int:
        
        ssum= ans=0
        sl=SortedList(nums)
        T=sum(nums)
        ssum=T
        
        while ssum*2 > T:
            ans+=1
            v=sl.pop(-1)
            ssum-=v
            v/=2
            ssum+=v
            sl.add(v)
        return ans
        
        
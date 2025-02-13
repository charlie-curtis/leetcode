class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        
        sl=SortedList(nums)
        
        ans=0
        while sl[0] < k:
            a,b=sl.pop(0),sl.pop(0)
            ans+=1
            sl.add(2*a + b)
        return ans
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        expected=0
        for x in arr:
            expected=min(expected+1,x)
        return expected
            
        
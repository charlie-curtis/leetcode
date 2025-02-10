class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        n=len(arr)
        high,low= [1]*n,[1]*n
        
        for i in range(1,n):
            if arr[i] > arr[i-1]:
                high[i] = low[i-1] + 1
            if arr[i] < arr[i-1]:
                low[i] =  high[i-1] + 1
        return max(max(high), max(low))
        
        
        
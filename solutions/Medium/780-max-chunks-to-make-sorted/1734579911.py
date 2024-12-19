class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:

        n = len(arr)
        stop = -1
        ans = 0
        for i in range(n):
            stop = max(stop, arr[i])
            if stop == i:
                ans+=1
        return ans
        
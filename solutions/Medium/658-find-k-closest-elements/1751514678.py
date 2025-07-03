class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l = bisect_right(arr, x)-1
        r = l+1

        n = len(arr)
        for _ in range(k):
            if l < 0:
                r+=1
            elif r >= n:
                l-=1
            elif abs(arr[l]-x) <= abs(arr[r]-x):
                l-=1
            else:
                r+=1
        return arr[l+1:r]
        
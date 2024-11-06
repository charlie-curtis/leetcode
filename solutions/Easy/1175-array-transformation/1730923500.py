class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:

        n = len(arr)
        out = arr.copy()
        moved = True
        while moved:
            moved = False
            out = arr.copy()
            for i in range(1,n-1):
                if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                    moved = True
                    out[i]+=1
                elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    moved = True
                    out[i]-=1
            arr = out
        return arr
        
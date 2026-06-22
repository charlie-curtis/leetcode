class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:

        arr.sort()
        n = len(arr)
        if n % 2 == 1:
            med = arr[n//2]
        else:
            med = arr[n//2-1]
        A = [(-abs(x-med), -x, x) for x in arr]
        A.sort()
        out = []
        for i in range(k):
            out.append(A[i][2])
        return out
        
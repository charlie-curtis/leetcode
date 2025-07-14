class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:

        hmx = vmx = 1
        hBars.sort()
        vBars.sort()

        streak = 1
        for _, g in groupby(enumerate(hBars), key=lambda x: x[1] - x[0]):
            hmx = max(hmx, len(list(g)))
        
        for _, g in groupby(enumerate(vBars), key=lambda x: x[1] - x[0]):
            vmx = max(vmx, len(list(g)))
        vmx+=1
        hmx+=1

        return max(1, min(vmx,hmx)*min(vmx,hmx))
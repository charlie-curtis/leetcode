class Solution:
    def isRectangleOverlap(self, rectA: List[int], rectB: List[int]) -> bool:

        L1 = rectA[0]
        L2 = rectA[2]
        L3 = rectB[0]
        L4 = rectB[2]

        R1 = rectA[1]
        R2 = rectA[3]
        R3 = rectB[1]
        R4 = rectB[3]

        #This problem took me a really long time and I had to look at the editorial. Basically, we can solve this problem
        #as 2 separate 1D problems (and this pattern can be applicable to other problems too). For this idea specifically, there should be
        #an X value that exists in the overlapped region, and so doing the min,max stuff checks to see whether such an X exists

        x_range = min(L2, L4) - max(L3, L1)
        y_range = min(R2, R4) - max(R3, R1)

        return x_range > 0 and y_range > 0


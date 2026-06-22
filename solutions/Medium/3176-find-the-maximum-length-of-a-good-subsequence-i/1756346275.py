class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:


        #original time complexity was O(N^2*k). After looking at solutions, revised it to O(N*K)


        C = Counter() # C[(x,i)] = longest subsequence ending in x with exactly i mismatches
        R = Counter() # R(i) = longest subsequence with at most i mismatches
        for x in nums:
            for i in range(k,-1, -1):
                C[(x,i)] = max(C[(x,i)]+1, R[i-1]+1)
                R[i] = max(C[(x,i)], R[i])
        return max(C.values())

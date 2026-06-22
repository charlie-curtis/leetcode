class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        m,n = max(len(nums1), len(nums2)), min(len(nums1), len(nums2))
        
        #m > n
        if 6*n < m:
            return -1 

        S, T = sum(nums1) , sum(nums2)
        if S == T:
            return 0
        if T > S:
            T,S = S, T
            nums1, nums2 = nums2, nums1
        
        #S > T
        moves = 0
        A = deque(sorted(nums1))
        B = deque(sorted(nums2))
        diff = S - T
        #since S > T, we want to replace HIGH values in S with low values
        #likewise, we want to replace LOW values in T with high values
        while diff > 0:
            a = A[-1] if A else float('inf')
            b = B[0] if B else float("inf")
            if abs(6-a) <= abs(1-b):
                #we changed A.pop() to 1, and got closer to our goal by A.pop()-1
                diff-= (A.pop()-1)
            else:
                #we changed B.popleft to 6, and increased T by 6-B.popleft()
                diff-=(6-B.popleft())
            moves+=1
        return moves
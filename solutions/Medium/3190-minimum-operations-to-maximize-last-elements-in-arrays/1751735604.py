class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        def score(A,B, flag):

            score = 0 if not flag else 1
            for a,b in zip(A[:-1], B[:-1]):
                if a <= A[-1] and b <= B[-1]:
                    continue
                if b <= A[-1] and a <= B[-1]:
                    score+=1
                else:
                    return -1
            return score
        

        a = score(nums1, nums2, False)
        nums1[-1], nums2[-1] = nums2[-1], nums1[-1]
        b = score(nums1, nums2, True)

        if a == -1: return b
        if b == -1: return a
        return min(a,b)
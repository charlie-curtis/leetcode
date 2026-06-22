#4,7
#[4,7] mid = 3 (target = 1,4)
class Solution:
    def kthSmallestSubarraySum(self, A: List[int], k: int) -> int:

        n = len(A)
        def check(mid):
            j = 0
            ssum = 0
            cnt = 0
            for i in range(n):
                ssum+=A[i]

                while ssum > mid and j <= i:
                    ssum-=A[j]
                    j+=1
                cnt+=(i-j+1)
            return cnt >= k



        # True means >= k subarray sums that are <= mid

        l = 0
        r = 10**9

        #FFFFFFTTTTTTTT
        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                #there are >=k values, so move window left
                r = mid -1
            else:
                l = mid +1

        return l
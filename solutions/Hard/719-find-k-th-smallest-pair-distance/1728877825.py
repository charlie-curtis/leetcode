class Solution:
    def smallestDistancePair(self, A: List[int], k: int) -> int:

        #1 3 4 6 8 10 13 15
        A.sort()


        def check(mid):

            cnt = 0
            j = 0
            n = len(A)
            for i in range(n):
                while j < n and (A[j] - A[i] <= mid):
                    j+=1
                cnt+=j-i-1
            return cnt >= k

        l = 0
        r = 10**6

        #FFFFFTTTTTTTT
        #small dists = less than k
        #too big of distances = big k
        #i want to find the smallest dist where pairs >=k (check function returns true for >=k found)

        while l <= r:
            mid = l + (r-l)//2
            if check(mid):
                r = mid -1
            else:
                l = mid + 1

        return l
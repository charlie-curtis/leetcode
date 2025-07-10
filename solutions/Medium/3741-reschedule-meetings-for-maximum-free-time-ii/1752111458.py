class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:


        A = list(zip(startTime,endTime))
        n = len(startTime)

        left = [0]*n
        right = [0]*n

        prevEnd = 0
        ans = 0
        for i,(start,end) in enumerate(A):
            free = start - prevEnd
            ans = max(ans, free)
            if i > 0:
                left[i] = left[i-1]
            left[i] = max(left[i], free)
            prevEnd = end

        prevStart = eventTime
        for i in range(n-1,-1,-1):
            ans = max(ans, free)
            start,end = A[i]
            free = prevStart - end
            if i+1 < n:
                right[i] = right[i+1]
            right[i] = max(right[i], free)
            prevStart = start


        for i in range(n):
            start,end = A[i]
            d = end-start
            lower = 0 if i == 0 else A[i-1][1]
            upper = eventTime if i == n-1 else A[i+1][0]
            if (i-1 >= 0 and left[i-1] >= d) or (i+1 < n and right[i+1] >= d):
                ans = max(ans, upper-lower)
            else:
                ans = max(ans, upper-lower - d)
            
        return ans
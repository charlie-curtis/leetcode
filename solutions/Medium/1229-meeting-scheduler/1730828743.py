class Solution:
    def minAvailableDuration(self, A: List[List[int]], B: List[List[int]], duration: int) -> List[int]:

        A.sort()
        B.sort()

        m,n = len(A), len(B)

        p1 = p2 = 0
        while p1 + p2 < m+n:
            a = [1e15, 1e15] if p1 == m else A[p1]
            b = [1e15, 1e15] if p2 == n else B[p2]

            high = min(a[1], b[1])
            low = max(a[0], b[0])

#            print(a,b)
#            print(low, high)
            good = high-low >= duration
            if good:
                return [low, low+duration]
            if a[1] <= b[1]:
                p1+=1
            else:
                p2+=1

            # 52 - 80
            # 60 - 90
        return []
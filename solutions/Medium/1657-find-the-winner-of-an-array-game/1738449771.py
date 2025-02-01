class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:

        A = deque(arr)

        mmax = max(arr)

        t = 0
        while A[0] != mmax:
            if A[0] > A[1]:
                first,second = A.popleft(), A.popleft()
                A.append(second)
                A.appendleft(first)
                t+=1
            else:
                A.append(A.popleft())
                t = 1
            if t == k:
                return A[0]
        return mmax
                
        
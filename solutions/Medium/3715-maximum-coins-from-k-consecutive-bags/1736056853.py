class Solution:
    def maximumCoins(self, A: List[List[int]], K: int) -> int:
        n = N = len(A)
        k = K

        # Solve for all I with I.left = A[i].left
        def solve(A):
            A.sort()
            ans = window = j = 0

            # We are considering interval I = [l..l+K-1]
            for i, (l, r, v) in enumerate(A):
                
                if r-l+1 >=k:
                    #if this window is too large, calculate, then continue sliding
                    ans = max(ans, k*v)
                    if i != j:
                        raise ValueError("Wrong")
                    if window != 0:
                        raise ValueError("Wrong")
                    j = i+1
                    continue

                while j<n and A[j][1] < l+K:
                    window+=(A[j][1]-A[j][0]+1)*A[j][2]
                    j+=1

                extra = 0
                if j<n and A[j][0] < l+K:
                    boundary = min(A[j][1],l+K-1)
                    extra = (boundary - A[j][0]+1)*A[j][2]

                ans = max(ans, window+extra)
                window-= (r-l+1)*v

            return ans

        ans = solve(A)
        for i, (l, r, c) in enumerate(A):
            A[i] = [-r, -l, c]
        ans = max(ans, solve(A))
        return ans

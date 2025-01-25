class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:

        items = []
        items.append(1)
        items.append(1)
        while items[-1] < k:
            f,f0 = items[-1], items[-2]
            items.append(f+f0)

        moves = 0
        while k > 0:
            moves+=1
            idx = bisect_right(items, k)-1
            k-=items[idx]
        return moves
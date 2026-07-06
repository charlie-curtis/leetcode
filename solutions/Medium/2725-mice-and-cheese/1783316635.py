class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        A = []
        for x,y in zip(reward1, reward2):
            A.append([y-x, x, y])

        A.sort()
        ans = 0
        for i, (_,x,y) in enumerate(A):
            ans+=x if (i < k) else y
        return ans
        
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:

        m,n = len(fruits), len(baskets)
        ans = 0
        for i in range(m):
            found = False
            for j in range(n):
                if fruits[i] <= baskets[j]:
                    found = True
                    baskets[j] = -1
                    break
            if not found:
                ans+=1
        return ans
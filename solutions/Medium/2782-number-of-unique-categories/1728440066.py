# Definition for a category handler.
# class CategoryHandler:
#     def haveSameCategory(self, a: int, b: int) -> bool:
#         pass
class Solution:
    def numberOfCategories(self, n: int, categoryHandler: Optional['CategoryHandler']) -> int:

        ans = 0
        for i in range(n):
            good = True
            for j in range(i):
                if categoryHandler.haveSameCategory(i,j):
                    good = False
                    break
            if good:
                ans+=1

        return ans
        
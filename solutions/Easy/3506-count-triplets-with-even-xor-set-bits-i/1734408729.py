class Solution:
    def tripletCount(self, a: List[int], b: List[int], c: List[int]) -> int:

        ans = 0
        for x in a:
            for y in b:
                for z in c:
                    if (x^y^z).bit_count() % 2 == 0:
                        ans+=1
        return ans
        
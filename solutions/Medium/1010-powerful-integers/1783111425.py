class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:

        out = set()
        #log2(1,000,000) = 20
        for i in range(0,21):
            v1 = x**i
            for j in range(0,21):
                v2 = v1 + y**j
                if v2 <= bound:
                    out.add(v2)
                else:
                    break
        return list(out)
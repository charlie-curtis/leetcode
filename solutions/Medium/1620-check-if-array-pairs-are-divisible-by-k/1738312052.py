class Solution:
    def canArrange(self, A: List[int], k: int) -> bool:

        C = Counter([x%k for x in A])


        for t in C.keys():

            k1 = t
            k2 = k-t
            if (k1 == 0) or k1==k2:
                if C[k1] % 2 == 1:
                    return False
            elif C[k1] != C[k2]:
                return False
        return True
            

            
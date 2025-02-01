class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:

        seen = set()
        def do(x):

            if x not in seen:
                return x

            k = 1
            while True:
                t = x + '(' + str(k)  + ')'
                if t not in seen:
                    return t
                k+=1
        out = []
        for x in names:
            res = do(x)
            seen.add(res)
            out.append(res)
        return out
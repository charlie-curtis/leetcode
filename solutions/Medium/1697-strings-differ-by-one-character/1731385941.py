class Solution:
    def differByOne(self, dict: List[str]) -> bool:



        p = 31
        seen = set()
        for i,x in enumerate(dict):
            for j in range(len(x)):
                strval = x[:j] + '*' + x[j+1:]
                h = hash(strval)*p

                if h in seen:
                    return True
                seen.add(h)

        return False
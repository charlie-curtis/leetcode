class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:

        m = len(rolls)
        expected = (n+m)*mean
        actual = sum(rolls)
        needed = expected-actual
        rem_avg = needed/n
        if rem_avg < 1 or rem_avg > 6:
            return []
        out = [needed//n]*n
        r = needed % n
        for i in range(r):
            out[i]+=1
        return out
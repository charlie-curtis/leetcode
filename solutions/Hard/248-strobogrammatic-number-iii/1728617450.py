class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:

        sset = set()
        a = ['9', '6', '8', '1', '0']
        b = ['6', '9', '8', '1', '0']
        d = dict(zip(a,b))

        n = len(high)
        low = int(low)
        high = int(high)

        def bt(cur):

            if cur:
                can = int(cur)
                if low <= can <= high:
                    if cur[0] != '0' or can == 0: #cannot have leading zeros UNLESS the number is 0 itself
                        sset.add(can)

            if len(cur) > n:
                return

            
            for k,v in d.items():
                x = k + cur + v
                bt(x)

                if not cur and k == v:
                    bt(k)
        bt("")
        return len(sset)

        
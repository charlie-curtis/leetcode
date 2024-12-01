# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    def __init__(self):
        self.prev = None

    def read(self, buf: List[str], n: int) -> int:

        def fromBuffer(offset, n):
            i = offset 
            tmp = [0]*4
            while i < n:
                r = read4(tmp)
                needed = n-i
                used = min(r, needed)
                if used != r:
                    self.prev = tmp[used:r].copy()
                buf[i:i+used] = tmp[:used]
                i+=used
                if r < 4:
                    break
            return i-offset 

        def fromLocal(n):
            if self.prev == None:
                return 0 

            used = min(n, len(self.prev))
            buf[:used] = self.prev[:used]
            if used != len(self.prev):
                self.prev = self.prev[used:].copy()
            else:
                self.prev = None

            return used


        used = fromLocal(n)
        used2 = fromBuffer(used, n)

        return used + used2
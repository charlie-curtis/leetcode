class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        out = []
        for h in range(12):
            for m in range(60):
                if h.bit_count() + m.bit_count() == turnedOn:
                    if m < 10:
                        out.append(str(h) + ":0" + str(m))
                    else:
                        out.append(str(h) + ":" + str(m))
        return out
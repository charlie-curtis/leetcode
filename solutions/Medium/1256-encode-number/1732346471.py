class Solution:
    def encode(self, num: int) -> str:

        starts = []
        for i in range(34):
            starts.append((1<<i) -1)

        idx = bisect_right(starts, num)-1
        diff = num - starts[idx]

        if idx == 0:
            return ""

        needed_length = idx
        can = bin(diff)[2:]
        if len(can) < needed_length:
            needed = needed_length-len(can)
            can = "0"*needed + can
        return can
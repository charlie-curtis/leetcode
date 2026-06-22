class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:

        d = defaultdict(int)

        for pos, r in lights:
            d[pos-r]+=1
            d[pos+r+1]-=1

        sorted_positions = sorted(d.keys())

        ans = float('inf')

        high = 0
        cur = 0
        for x in sorted_positions:
            cur+=d[x]
            if cur > high:
                high = cur
                ans = x
        return ans



        
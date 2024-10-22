class Solution:
    def minimizeError(self, prices: List[str], target: int) -> str:


        n = len(prices)
        remainders = []
        ints = []
        needed = target
        for x in prices:
            f = float(x)
            whole = math.floor(f)
            if f != whole:
                remainders.append(f - whole)
            needed-=whole

        if needed < 0 or len(remainders) < needed:
            #if needed is 0, that means we already went over budget even when rounding everything down
            #if len(remainders) is less than needed, it means we won't hit our target even if we rounded everything up
            return "-1"
            

        remainders.sort(reverse=True)

        up = remainders[:needed]
        down = remainders[needed:]
        ans = 0

        for x in up:
            ans+=1-x
        for x in down:
            ans+=x
        return("%.3f" % ans)

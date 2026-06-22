class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:

        sd = SortedDict()
        rev = defaultdict(int)
        for i in range(1,m+1):
            sd[i-1] = i-1
            rev[i] =  i-1

        out = []
        for i in queries:
            #get current position
            pos = rev[i]

            #find out how many eles are infront of it
            out.append(sd.bisect_left(pos))

            #move to front and remap pos
            low = sd.peekitem(0)[0]
            rev[i] = low-1
            del sd[pos]
            sd[low-1] = i
        return out
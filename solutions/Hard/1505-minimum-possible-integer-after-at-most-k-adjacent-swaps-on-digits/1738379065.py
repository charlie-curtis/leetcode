class Solution:
    def minInteger(self, num: str, k: int) -> str:

        d = defaultdict(deque)

        for i,x in enumerate(num):
            d[int(x)].append(i)

        out = []
        n = len(num)
        offset = 0
        #0,1,2,3,4,5,6
        #3,0,1,2,4,5,6
        #3,2,0,1,4,5,6
        #3,0,1,2,4,5,6
        sl = SortedList()
        for i in range(n):
            for j in range(0,10):
                if len(d[j]) > 0:
                    bigger = len(sl) - sl.bisect_right(d[j][0])
                    actual = d[j][0] + bigger
                    if actual - i <= k:
                        #we can use it
                        k-=(actual-i)
                        out.append(str(j))
                        sl.add(d[j].popleft())
                        break

        return ''.join(out)
                
        
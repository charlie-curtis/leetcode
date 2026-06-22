class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:

        lasts = defaultdict(int)
        firsts = defaultdict(int)
        for i in range(26):
            l = chr(i+ord('a'))
            lasts[l] = s.rfind(l)
            firsts[l] = s.find(l)
        A = []


        seen = []
        for i in range(26):
            c = chr(ord('a') + i)
            if lasts[c] == -1:
                continue
            stop = lasts[c]
            start = firsts[c]
            cur = start
            good = True
            while cur < stop:
                if firsts[s[cur]] < start:
                    good = False
                    break
                stop = max(stop, lasts[s[cur]])
                cur+=1
            if good:
                seen.append([start, stop])
        
        seen.sort(key=lambda x: x[1])

        #print(seen)

        out = []
        for start,end in seen:
            if not out or out[-1][1] < start:
                out.append([start,end])
        
        return [s[i:j+1] for (i,j) in out]

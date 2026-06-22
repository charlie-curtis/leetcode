class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:

        C = Counter(s)
        if len(C.keys()) == 1:
            return False
        if k == 0: return True
        intervals = []

        d_first = {}
        d_last = {}
        for i in range(26):
            c = chr(i+ord('a'))
            if c not in s:
                continue
            first = s.find(c)
            last = s.rfind(c)
            d_first[c] = first
            d_last[c] = last
            intervals.append([c, first, last])


        filtered = []
        for c, start,end in intervals:
            j = start
            good = True
            while j < end:
                cur = s[j]
                if d_first[cur] < start:
                    good = False
                    break
                end = max(end, d_last[cur])
                j+=1
            if good:
                filtered.append([start, end])


        intervals = filtered
        intervals.sort(key=lambda x: x[1])
        if len(intervals) == 1:
            return False
        #print(intervals)
        good = []
        for s,e in intervals:
            if not good or good[-1][1] < s:
                good.append([s,e])
        #print(good)
        return len(good) >= k
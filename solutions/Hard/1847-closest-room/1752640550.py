class Solution:
    def closestRoom(self, rooms: List[List[int]], queries: List[List[int]]) -> List[int]:

        rooms.sort(key=lambda x: -x[1])

        rooms = deque(rooms)
        Q = []
        sl = SortedList()
        for i,(pref, size) in enumerate(queries):
            Q.append([size, pref, i])
        Q.sort(reverse=True)
        out = [-1]*len(Q)
        INF = 3*10**9
        for size, pref, idx in Q:
            while rooms and rooms[0][1] >= size:
                sl.add(rooms.popleft()[0])
            
            upper = sl.bisect_left(pref)
            lower = sl.bisect_left(pref)-1
            a = b = INF
            if upper < len(sl):
                a = sl[upper]
            if lower >= 0:
                b = sl[lower]
            
            if a == b == INF:
                continue
            if abs(pref-b) <= abs(pref-a):
                out[idx] = b
            else:
                out[idx] = a
        return out




        
        
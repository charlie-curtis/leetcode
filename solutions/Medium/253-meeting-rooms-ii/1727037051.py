class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        d = defaultdict(int)
        rooms = ans = 0
        for start,end in intervals:
            d[start]+=1
            d[end]-=1
        
        for k in sorted(d.keys()):
            rooms+=d[k]
            ans = max(rooms,ans)
        return ans
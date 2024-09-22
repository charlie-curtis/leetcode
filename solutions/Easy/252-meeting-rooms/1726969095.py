class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        d = defaultdict(int)

        for start,end in intervals:
            d[start]+=1
            d[end]-=1
        
        x = 0
        for k,v in sorted(d.items()):
            x+=v
            if x > 1:
                return False
        return True
        
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

        #meetings.sort(key=lambda x: x[1])
        meetings.sort()

        intervals = []
        for s,e in meetings:
            if not intervals or intervals[-1][1] < s:
                intervals.append([s,e])
            else:
                s1,e1 = intervals[-1]
                intervals[-1] = [min(s1,s), min(max(e1,e),days)]

        

        for s,e in intervals:
            days-=(e-s+1)
        return days
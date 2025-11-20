class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        included = []

        print(intervals)
        for start,end in intervals:
            #see if it's in the interval, and if it's not, include the latest 2
            needed = 2
            if included and start <= included[-1] <= end:
                needed-=1
            if len(included) > 1 and start <= included[-2] <= end:
                needed-=1
            
            cur = end
            tmp = []
            while needed:
                if included and cur == included[-1]:
                    cur-=1
                    continue
                needed-=1
                tmp.append(cur)
                cur-=1
            included+=tmp[::-1]
        return len(included)
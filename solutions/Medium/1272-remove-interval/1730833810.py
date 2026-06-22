class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:

        out = []
        remove_start = toBeRemoved[0]
        remove_end = toBeRemoved[1] -1
        for start,end in intervals:

            end-=1 #make it inclusive

            if remove_end < start or end < remove_start:
                #no overlap
                out.append([start,end])
            else:
                #there is atleast some overlap, count it and then filter it later
                out.append([start, remove_start-1])
                out.append([remove_end+1, end])

        return [[x[0], x[1]+1] for x in out if x[1] - x[0] >= 0]
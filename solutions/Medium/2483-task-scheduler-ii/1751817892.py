class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:

        last = {}
        day = 0
        for i,x in enumerate(tasks):
            a = day + 1
            b = last[x] + space +1 if x in last else -1
            day = max(a,b)
            last[x] = day
        return day

        
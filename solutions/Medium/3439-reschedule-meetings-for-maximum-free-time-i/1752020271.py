class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:

        A = [e-s for (s,e) in zip(startTime, endTime)]
        pref = list(accumulate(A, initial =0))
        #print(pref)

        best = 0
        ans = 0
        n = len(endTime)
        for i in range(n):
            l= min(k,i+1)
            t = pref[i+1] - pref[i-l+1]
            #print("reschedulign", l, "meetings with duration", t)
            lower = 0 if i-l < 0 else endTime[i-l]
            upper = eventTime if i+1 >= n else startTime[i+1]

            width = upper-lower
            taken = t
            #print("width was", width, "and i only occupied", taken)
            ans = max(ans, width - taken)
        return ans
        
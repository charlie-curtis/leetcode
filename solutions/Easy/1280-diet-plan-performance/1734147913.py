class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:

        '''
        j = 0
        n = len(calories)
        ans = 0
        ssum = 0
        for i in range(n):
            ssum+=calories[i]
            if i - j + 1 > k:
                ssum-=calories[j]
                j+=1
            if i-j+1 == k:
                if ssum > upper:
                    ans+=1
                elif ssum < lower:
                    ans-=1
        return ans
        '''

        pref = list(accumulate(calories, initial=0))
        ans = 0

        n = len(calories)
        for i in range(n-k+1):
            T = pref[i+k] - pref[i]
            if T > upper:
                ans+=1
            elif T < lower:
                ans-=1
        return ans 
        
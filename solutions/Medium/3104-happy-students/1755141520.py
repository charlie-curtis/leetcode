class Solution:
    def countWays(self, nums: List[int]) -> int:

        ans = 0
        n = len(nums)
        C = Counter(nums)

        selected = 0
        keys = sorted(C.keys())
        m = len(keys)
        for i in range(m):
            #can we include this in our group?
            #in order to do that, the number of selected has to be > keys[i]
            #AND has to be less than keys[i+1]
            v = C[keys[i]]
            selected+=v
            if keys[i] < selected and (i+1 == m or keys[i+1] > selected):
                ans+=1

        if C[0] == 0:
            #if 0 wasn't included in our array, we can always pick it
            ans+=1
        return ans

        
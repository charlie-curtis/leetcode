class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:

        n = len(nums)

        max_reach = [0]*n
        lows = deque()
        highs = deque()
        j = 0
        for i in range(n):
            while lows and nums[lows[-1]] >= nums[i]:
                lows.pop()
            while highs and nums[highs[-1]] <= nums[i]:
                highs.pop()
            
            lows.append(i)
            highs.append(i)

            while nums[highs[0]] - nums[lows[0]] > k:
                j+=1
                if highs[0] < j:
                    highs.popleft()
                if lows[0] < j:
                    lows.popleft()
            max_reach[i] = j

        dp = [0]*(n+1)
        dp[0] = 1
        pref = [0]*(n+2) #shitty indexing
        pref[1] = 1
        MOD = 10**9 + 7

        #dp[i] = number of valid partitions ENDING AT i-1 (1-indexed)
        #pref[i] = number of valid partitions ENDING AT i-2 (2-indexed - or rather - 1 greater than the dp[i] array)
        #the indexing is confusing because they are both padded with 0s and the second is based off the first
        for i in range(n):
            #we know that [L,R] is a valid range b/c of the precomputation that we did
            l = max_reach[i]
            r = i
            dp[i+1] = pref[r+1] - pref[l] + MOD
            dp[i+1]%=MOD
            pref[i+2] = pref[i+1] + dp[i+1]
            pref[i+2]%=MOD
        return dp[n]
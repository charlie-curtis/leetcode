class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:


        ans = j = 0
        n = len(nums)

        freq = Counter()
        freqOfFreq = Counter()
        mx = -1
        for i in range(n):
            x = nums[i]
            if freq[x] > 0:
                freqOfFreq[freq[x]]-=1
            freq[x]+=1
            mx = max(freq[x], mx)


            while mx + k < (i-j+1):
                y = nums[j]
                freqOfFreq[freq[y]]-=1
                if freqOfFreq[freq[y]] == 0:
                    mx-=1
                freq[y]-=1
                if freq[y] > 0:
                    freqOfFreq[freq[y]]+=1
                j+=1

            ans = max(ans, mx)
        return ans

        
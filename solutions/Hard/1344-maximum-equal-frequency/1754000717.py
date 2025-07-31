class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:

        freq = Counter()
        freqOfFreq = Counter()

         #cases
            #Case 1. 4,4,4,1 -> completely eliminate a number
            #Case 2. 1,1,1,1 -> all teh same number, just chop off one
            #Case 3. 4,4,3,3,5,5,5 -> chop off the highest freq
        # case 4. 1,2 or 1,2,3

        def isgood():
            f = freqOfFreq
            #print(f)
            #case2
            if len(freq.keys()) == 1:
                return True

            if len(f.keys()) == 2 and f[1] ==1:
                return True
            if len(f.keys()) == 2:
                mx=max(f.keys())
                mn=min(f.keys())
                if mx-mn==1 and f[mx] == 1:
                    return True
            if len(f.keys()) == 1 and f[1] > 0:
                return True
            return False

        ans = 0
        for i,x in enumerate(nums):
            if freq[x] > 0:
                freqOfFreq[freq[x]]-=1
                if freqOfFreq[freq[x]] == 0:
                    del freqOfFreq[freq[x]]
            freq[x]+=1
            freqOfFreq[freq[x]]+=1
            if isgood(): ans= i+1
        return ans
            
        
class Solution:
    def longestBalanced(self, nums: List[int]) -> int:

        #nums.length = 1500, so at most 750 evens, 750 odds. Do sliding window and consider every window size with 1,2,..750 unique digits


        n = len(nums)
        def check(tolerance):
            j = 0
            odds = Counter()
            evens = Counter()
            best = 0
            for i in range(n):
                x = nums[i]
                if x % 2:
                    odds[x]+=1
                else:
                    evens[x]+=1
                
                while max(len(odds.keys()), len(evens.keys())) > tolerance:
                    y = nums[j]
                    if y % 2:
                        odds[y]-=1
                        if not odds[y]:
                            del odds[y]
                    else:
                        evens[y]-=1
                        if not evens[y]:
                            del evens[y]
                    j+=1
                
                if len(odds.keys()) == len(evens.keys()):
                    best = max(best, i-j+1)
            return best

        return max([check(x) for x in range(n//2+1)])


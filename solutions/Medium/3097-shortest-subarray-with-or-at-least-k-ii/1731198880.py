class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 1

        C = Counter()

        n = len(nums)
        ans = 1e15

        def add(x):
            for i in range(33):
                if x&(1<<i) > 0:
                    C[i]+=1
        def sub(x):
            for i in range(33):
                if x&(1<<i) > 0:
                    C[i]-=1
        def good(x):
            cur = 0
            for kkey, val in C.items():
                if val > 0:
                    cur|=(1<<kkey)
            return cur >= x

        j = 0
        for i in range(n):
            add(nums[i])


            while good(k):
                ans = min(ans, i-j+1)
                sub(nums[j])
                j+=1

        return ans if ans != 1e15 else -1
        
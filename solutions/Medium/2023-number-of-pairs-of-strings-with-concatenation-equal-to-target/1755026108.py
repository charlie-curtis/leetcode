class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        C = Counter(nums)

        ans = 0
        for x in nums:
            m = len(x)
            if m > len(target):
                continue
            if x == target[:m]:
                rest = target[m:]
                ans+=C[rest]
                if x == rest:
                    ans-=1
        return ans

        
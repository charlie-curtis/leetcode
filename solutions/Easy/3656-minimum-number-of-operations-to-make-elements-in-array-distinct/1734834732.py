class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        C = Counter(nums)

        ans = 0
        nums = deque(nums)

        while max(C.values()) > 1:
            for i in range(min(3, len(nums))):
                x = nums.popleft()
                C[x]-=1
            ans+=1
        return ans
        
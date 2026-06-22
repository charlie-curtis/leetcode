class Solution:
    def minUnlockedIndices(self, nums: List[int], locked: List[int]) -> int:

        n = len(nums)
        i = j = -1
        for k,x in enumerate(nums):
            if x == 3 and i == -1:
                i = k
            elif x == 1:
                j = k
        if i != -1 and j > i:
            #there can never be a 1 after a 3
            return -1


        ones = deque([i for i in range(n) if nums[i] == 1])
        twos = deque([i for i in range(n) if nums[i] == 2])
        threes = deque([i for i in range(n) if nums[i] == 3])
        locks = deque([i for i in range(n) if locked[i]])

        d = defaultdict(deque)
        for i,x in enumerate(sorted(nums)):
            d[x].append(i)

        ans = 0
        for i,x in enumerate(nums):

            t = d[x].popleft()
            if t <= i:
                continue
            while locks and locks[0] < i:
                locks.popleft()
            while locks and locks[0] < t:
                ans+=1
                locks.popleft()
        return ans


class Solution:
    def minJumps(self, nums: List[int]) -> int:

        locs = defaultdict(set)
        for i,x in enumerate(nums):
            locs[x].add(i)

        mx = max(nums)
        P = [True]*(mx+1)
        P[0] = P[1] = False
        i = 2
        while i*i <= mx:
            if P[i]:
                j = 2
                while j*i <= mx:
                    P[i*j] = False
                    j+=1
            i+=(1 if i == 2 else 2)


        n = len(nums)
        V = [True] + [False]*(n-1)
        q = deque()
        q.append(0)

        ans = 0
        while q:
            for _ in range(len(q)):
                idx = q.popleft()
                if idx == n-1:
                    return ans
                nxt = [idx-1, idx+1]
                if P[nums[idx]]:
                    P[nums[idx]] = False
                    j = 1
                    while nums[idx]*j <= mx:
                        a = nums[idx]*j
                        for x in locs[a]:
                            nxt.append(x)
                        locs[a] = set()
                        j+=1
                for x in nxt:
                    if 0 <= x < n and not V[x]:
                        V[x] = True
                        q.append(x)
            ans+=1
        return ans
#get prime factor count
cutoff = 10**5
F = [0]*(cutoff+1)

for x in range(2,cutoff+1):
    i = 2
    seen = set()
    y=x
    while i*i <= x:
        while x % i == 0:
            x//=i
            seen.add(i)
        i+=(2 if i % 2 else 1)

    if x != 1:
        seen.add(x)
    F[y] = len(seen)

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        n = len(nums)
        to_left = [0]*n
        to_right = [n-1]*n
        stack = []
        for i in range(n):
            while stack and F[nums[stack[-1]]] < F[nums[i]]:
                    stack.pop()
            if stack:
                #nums[i] will have priority over everything from [to_left[i], i]
                to_left[i] = stack[-1] + 1
            stack.append(i)

        stack = []
        for i in range(n-1,-1,-1):
            while stack and F[nums[stack[-1]]] <= F[nums[i]]:
                    stack.pop()
            if stack:
                #nums[i] will have priority over everything from [to_left[i], i]
                to_right[i] = stack[-1] - 1
            stack.append(i)

        pq = []
        for i in range(n):
            R = to_right[i] - i #num of eles to right, exclusive
            L = i - to_left[i] #num of eles to left, exclusive
            heapq.heappush(pq, [-nums[i], R+L+1 + (L*R)]) # 2nd param is how many times we can select this number

        ans = 1
        MOD = 10**9 + 7
        while pq and k:
            v, cnt = heapq.heappop(pq)
            v = -v
            #print("processing", v, "times", cnt)
            used = min(k, cnt)
            k-=used
            t = pow(v,used, MOD)
            ans*=t
            ans%=MOD
        return ans
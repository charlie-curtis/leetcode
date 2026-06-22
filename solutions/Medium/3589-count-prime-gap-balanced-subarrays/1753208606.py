cutoff = (5*10**4)
P = [True]*(cutoff+1)
P[0] = P[1] = False
i = 2
for i in range(2, int(sqrt(cutoff)) +1):
    if P[i]:
        for j in range(2, int(cutoff//i)+1):
            P[i*j] = False

class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:

        n = len(nums)
        ans = j = 0
        minq = deque()
        maxq = deque()
        dq = deque()
        for i,x in enumerate(nums):
            if P[x]:
                dq.append(i)
                while minq and nums[minq[-1]] >= x:
                    minq.pop()
                minq.append(i)
                while maxq and nums[maxq[-1]] <= x:
                    maxq.pop()
                maxq.append(i)
                
            while len(dq) > 1 and nums[maxq[0]] - nums[minq[0]] > k:
                y = nums[j]
                if P[y]:
                    if dq[0] == y:
                        dq.popleft()
                    if minq[0] == j:
                        minq.popleft()
                    if maxq[0] == j:
                        maxq.popleft()
                j+=1
            
            if len(dq) > 1 and nums[maxq[0]] - nums[minq[0]] <= k:
                #the entire window is good except for the places where there aren't 2 prime numbers -- which we can determine from the dq
                a =(i-j+1) - (i-dq[-2])
                ans+=a
        return ans
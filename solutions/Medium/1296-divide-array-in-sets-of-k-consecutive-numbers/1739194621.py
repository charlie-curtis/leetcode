class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        C=Counter(nums)
        
        d = deque(sorted(nums))
        seen=0
        n = len(nums)
        while seen < n:
            x = d.popleft()
            if C[x] == 0: continue
            for i in range(x,x+k):
                if C[i] == 0: return False
                C[i]-=1
                seen+=1
        return True
            
        
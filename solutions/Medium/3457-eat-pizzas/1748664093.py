class Solution:
    def maxWeight(self, p: List[int]) -> int:


        p.sort()
        p = deque(p)
        moves = len(p)//4

        i = moves//2 + moves % 2
        j = moves//2

        ans = 0
        while i:
            #choose the biggest
            ans+=p.pop();
            p.popleft();
            i-=1
        while j:
            p.pop();
            ans+=p.pop();
            j-=1
        return ans
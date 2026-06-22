class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:

        target = deque(target)
        ans = []
        for i in range(1,n+1):
            if not target:
                break
            if i == target[0]:
                ans.append("Push")
                target.popleft()
            else:
                ans.append("Push")
                ans.append("Pop")
        return ans
            
            
        
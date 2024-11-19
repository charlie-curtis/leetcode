class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:


        maxSeen = 0
        n = len(heights)
        out = []
        for i in range(n-1, -1, -1):
            if heights[i] > maxSeen:
                out.append(i)
            maxSeen = max(heights[i], maxSeen)

        return out[::-1]
        
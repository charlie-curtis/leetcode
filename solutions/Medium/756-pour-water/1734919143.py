class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:

        n = len(heights)

        for i in range(volume):
            #if it flows downwards to the left, we will place it here

            idx = k
            small = heights[k]
            for i in range(k-1, -1, -1):
                if heights[i] > small:
                    break
                if small > heights[i]:
                    idx = i
                    small = heights[i]

            if idx != k:
                heights[idx]+=1
                continue

            idx = k
            small = heights[k]
            #if it flows downards to the right, we will place it here
            for i in range(k+1, n):
                if heights[i] > small:
                    break
                if small > heights[i]:
                    idx = i
                    small = heights[i]

            heights[idx]+=1

        return heights
class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:

        H = []
        for i,y in enumerate(nums):
            if y == x:
                H.append(i)
        
        return [H[x-1] if (x-1 < len(H)) else -1 for x in queries]

        
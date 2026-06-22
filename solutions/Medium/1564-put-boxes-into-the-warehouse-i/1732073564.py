class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        m,n = len(boxes), len(warehouse)
        minSeen = warehouse[0]
        for i in range(1,n):
            minSeen = min(warehouse[i], minSeen)
            warehouse[i] = minSeen

        boxes.sort()

        j = 0
        for i in range(n-1, -1, -1):
            if warehouse[i] >= boxes[j]:
                j+=1
                if j == m:
                    break
        return j


        
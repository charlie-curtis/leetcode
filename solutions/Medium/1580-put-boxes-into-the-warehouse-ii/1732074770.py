class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        boxes.sort()

        n = len(warehouse)
        minSeen = 1e15
        lefts = [0]*n
        rights = [0]*n
        for i in range(n):
            minSeen = min(warehouse[i], minSeen)
            lefts[i] = minSeen

        minSeen = 1e15
        for i in range(n-1, -1, -1):
            minSeen = min(warehouse[i], minSeen)
            rights[i] = minSeen

        for i in range(n):
            warehouse[i] = max(rights[i], lefts[i])

        warehouse.sort()
        m = len(boxes)
        j = 0
        for i in range(n):
            if warehouse[i] >= boxes[j]:
                j+=1
                if j == m:
                    break
        return j
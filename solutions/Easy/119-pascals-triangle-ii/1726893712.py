class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        if rowIndex == 0:
            return [1]
        prev = [1]

        for i in range(1, rowIndex+1):
            cur = []
            for j in range(i+1):
                s = 0
                if j-1 >= 0:
                    s+=prev[j-1]
                if j != i:
                    s+=prev[j]
                cur.append(s)
            prev = cur
        return prev


        
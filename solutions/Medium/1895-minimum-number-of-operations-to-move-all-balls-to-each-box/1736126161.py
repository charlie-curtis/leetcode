class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = []
        l, r = 0, boxes.count('1')
        cur = sum([i if boxes[i] == '1' else 0 for i in range(n)])
        for i in range(n):
            ans.append(cur)
            l+=1 if boxes[i] == '1' else 0
            r-=1 if boxes[i] == '1' else 0
            cur+=l
            cur-=r

        return ans
        
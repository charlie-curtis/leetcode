class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        C = Counter()

        for start,end, val in updates:
            C[start]+=val
            C[end+1]-=val

        out = [0]*length
        cur = 0
        for i in range(length):
            cur+=C[i]
            out[i] = cur
        return out

        
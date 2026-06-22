class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.C = Counter(nums2)
        self.A= nums1.copy()
        self.B=nums2.copy()

    def add(self, index: int, val: int) -> None:
        cur=self.B[index]
        self.B[index]+=val
        self.C[cur]-=1
        self.C[cur+val]+=1

    def count(self, tot: int) -> int:
        out=0
        for x in self.A:
            out+=self.C[tot-x]
        return out


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
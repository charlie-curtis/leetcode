class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:

        H=defaultdict(list)

        for i,x in enumerate(arr):
            H[i%k].append(x)

        def calc(li):
            A=[]
            for x in li:
                idx=bisect_right(A,x)
                if idx==len(A):
                    A.append(x)
                else:
                    A[idx]=x
            return len(li)-len(A)

        return sum(calc(li) for li in H.values())
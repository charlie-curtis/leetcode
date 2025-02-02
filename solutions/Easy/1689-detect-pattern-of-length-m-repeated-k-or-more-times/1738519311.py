class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:


        C = Counter()
        n = len(arr)
        for i in range(n):
            end = i+m*k
            if m*k > n:
                continue
            C = Counter()
            for j in range(i,i+m*k,m):
                s = tuple(arr[j:j+m])
                C[s]+=1
            if C[s] == k:
                return True
        return False
                
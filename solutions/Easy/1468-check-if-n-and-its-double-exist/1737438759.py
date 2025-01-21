class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        C = Counter(arr)
        for x in arr:
            if x == 0 and C[0] > 1:
                print("h1")
                return True
            if x != 0 and C[2*x] >= 1:
                print(x)
                print("h2")
                return True
        return False
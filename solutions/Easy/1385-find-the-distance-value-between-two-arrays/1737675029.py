class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:


        ans = 0
        for i in range(len(arr1)):
            good = True
            for j in range(len(arr2)):
                if abs(arr1[i] -arr2[j]) <=d:
                    good = False
                    break
            if good:
                ans+=1
        return ans
        
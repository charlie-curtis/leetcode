class Solution:
    def numberOfWeakCharacters(self, prop: List[List[int]]) -> int:


        prop.sort(key=lambda x: (-x[0], x[1]))
        ans = 0
        high = -1
        for x,y in prop:
            if y < high:
                ans+=1
            high = max(high, y)
        return ans
            
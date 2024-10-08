class Solution:
    def maxPrice(self, items: List[List[int]], capacity: int) -> float:

        items.sort(key=lambda x: -(x[0]/x[1]))

        ans = 0
        ptr = 0
        while capacity > 0 and ptr < len(items):
            p,c = items[ptr]
            if capacity - c >= 0:
                ans+=p
                capacity-=c
            else:
                #need to split this off
                ans+= (p*(capacity/c))
                capacity = 0
                break
            ptr+=1
        return ans if capacity == 0 else -1
        
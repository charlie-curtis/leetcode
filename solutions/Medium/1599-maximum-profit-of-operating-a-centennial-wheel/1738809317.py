class Solution:
    def minOperationsMaxProfit(self, customers: List[int], p: int, c: int) -> int:

        cur = 0
        best = 0
        idx = -1 
        backlog = 0
        for i,x in enumerate(customers):
            backlog+=x
            avail = min(4, backlog)
            backlog-=avail
            cur+= p*avail - c
            #print(cur)
            if cur > best:
                best = cur
                idx = i+1

        j = len(customers)
        while backlog:
            avail = min(4, backlog)
            backlog-=avail
            cur+= p*avail - c
            #print(cur)
            if cur > best:
                best = cur
                idx = j+1
            j+=1
            
            
        return idx
            
        
        
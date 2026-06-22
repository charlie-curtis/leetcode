class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:


        t = 0
        n = len(customers)
        waitTime = 0
        for arrival,cost in customers:

            actual_start = max(arrival, t)
            finish_time = cost+actual_start
            t = finish_time
            waitTime+=(finish_time - arrival)
        
        return waitTime / n
        
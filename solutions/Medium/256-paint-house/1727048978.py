class Solution:
    def minCost(self, costs: List[List[int]]) -> int:

        n = len(costs)
        red = [1e10]*n
        blue = [1e10]*n
        green = [1e10]*n

        red[0] = costs[0][0]
        blue[0] = costs[0][1]
        green[0] = costs[0][2]
        for i in range(1,n):
            red[i] = costs[i][0] + min(blue[i-1], green[i-1])
            blue[i] = costs[i][1] + min(red[i-1], green[i-1])
            green[i] = costs[i][2] + min(red[i-1], blue[i-1])
        return min(red[n-1], green[n-1], blue[n-1])
        
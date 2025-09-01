class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:

        m,n = len(bikes), len(workers)


        def get_available_bikes(cb):
            r = []
            for i in range(m):
                if (1<<i)&cb == 0:
                    r.append(i)
            return r

        INF = 10**9
        @cache
        def dp(i, bikes_available):

            if i == n:
                #all workers have been assigned
                return 0

            abikes = get_available_bikes(bikes_available)
            if len(abikes) == 0:
                #there are remaining workers, but not enough bikes
                return INF

            ans = INF 
            for next_bike in abikes:
                #distance between next_worker and next_bike
                d = abs(bikes[next_bike][0] - workers[i][0]) + abs(bikes[next_bike][1] - workers[i][1])

                #update the bitmap by marking next_bike and next_worker as unavailable
                rem = dp(i+1, bikes_available|(1<<next_bike))
                score = d + rem
                ans = min(ans, score)
            return ans

        return dp(0,0)

            

        
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:



        #dp(i,j) = max score you can get with age no less than X and score no greater than Y


        #(1,2)
        #(3,2)
        #(5,3)
        #10,4
        #15,5

        #(score,age)

        #15,5  10,4 5,3 3,2 1,2

        #print(sum(scores))


        #i is a prefix of the sorted array (sorted by age desc) and j is the score you must be strictly under in order to not cause conflict
        Z = list(zip(ages, scores))
        Z.sort(key= lambda x: (-x[0], -x[1]))

        n = len(Z)
        #print(Z)
        def dp(i,j, memo):
            if i == n:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            prevScore = Z[j][1] if j != -1 else 1e15 

            #we can either pick this element
            a = b = 0
            if (Z[i][1] <= prevScore):
                a = dp(i+1, i, memo) + Z[i][1]
            b = dp(i+1, j, memo)
            #print("returning", max(a,b), "for i=", i)
            memo[(i,j)] = max(a,b)
            return memo[(i,j)]
        return dp(0, -1, {})
                


            #or not pcik this element
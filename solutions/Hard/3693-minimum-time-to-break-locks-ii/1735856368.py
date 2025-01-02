from scipy.optimize import linear_sum_assignment
import numpy as np
class Solution:
    def findMinimumTime(self, strength: List[int]) -> int:

        '''
        I couldn't figure this out on my own (..because it requires a well-known algorithm that I couldn't derive on my own, lol).
        This is the hungarian method -- used for maximal matching

        What's cool though is I was able to model the problem correctly (e.g. the order in which we process locks will increase/decrease their cost), and
        we want to find a permutation that minimizes the total cost
        '''

        m = len(strength)
        adj = [[0 for _ in range(m)] for _ in range(m)]


        #this is constructing a matrix that says, "If we processed the i-th lock in the j-th order, it would cost X"
        for i in range(m):
            for j in range(m):
                cost = ceil(strength[i]/(j+1))
                adj[i][j] = cost
        
        cost_matrix = np.array(adj)

        row_ind, col_ind = linear_sum_assignment(cost_matrix)
        optimal_cost = cost_matrix[row_ind, col_ind].sum()

        return int(optimal_cost)
class Solution:
    def reachNumber(self, target: int) -> int:


        #1 2 3 4 5 6 -> t = 17
        # 1 + 3 + 4 + 5 + 6

        target = abs(target)
        ssum = 0
        moves = 0
        while (ssum < target) or ((ssum - target) % 2 == 1):
            moves+=1
            ssum+=moves
        
        return moves

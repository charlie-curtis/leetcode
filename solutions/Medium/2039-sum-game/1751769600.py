class Solution:
    def sumGame(self, num: str) -> bool:

        n = len(num)
        leftSum = sum([int(x) if x != '?' else 0 for x in num[:n//2]])
        rightSum = sum([int(x) if x != '?' else 0 for x in num[n//2:]])
        leftCount = len([x for x in num[:n//2] if x == '?'])
        rightCount = len([x for x in num[n//2:] if x == '?'])

        if leftCount == rightCount:
            return leftSum != rightSum
        if (leftCount + rightCount) % 2:
            #alice has the last move, can just make it unequal
            return True
        
        if rightCount > leftCount:
            rightCount,leftCount = leftCount,rightCount
            leftSum, rightSum = rightSum, leftSum

        leftCount-=rightCount
        moves = leftCount//2
        #so we'll have an unequal amount of moves on the left side
        #alice either greedily plays '0' hoping that player1 can't reach rightSum

        #OR alice greedily plays 9 hoping for an overshoot
        return moves*9 + leftSum != rightSum

        #to make more sense, either bob will play 9's, alice plays 0s
        #or vice versa. A win conditions are moves*9 + leftSum < rightSum
        #OR moves*9 + leftSum > rightSum
        #"NO matter what bob does, he'll either overshoot or undershoot unless the equation is equal.
        #If the equation is equal, than no matter what alice does, she cannot shake bob"
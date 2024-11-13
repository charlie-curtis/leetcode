class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], k: int) -> int:


        one_pos = deque()
        zero_pos = deque()

        ans = 0
        for i,x in enumerate(team):
            if x == 0:
                while one_pos and i - one_pos[-1] > k:
                    one_pos.pop()
                if one_pos:
                    one_pos.pop()
                    ans+=1
                else:
                    #we couldn't match
                    zero_pos.appendleft(i)

            else:
                #i'm a 1
                while zero_pos and i - zero_pos[-1] > k:
                    zero_pos.pop()
                if zero_pos:
                    zero_pos.pop()
                    ans+=1
                else:
                    one_pos.appendleft(i)
        return ans

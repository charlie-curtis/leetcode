class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        #brute force - try every permutation of cards. For each permutation, try every combination of operations. For every permutation of cards/combination of operations, try applying them in different orders (to simulate the use of parenthesis)
        def check(cards):
            if len(cards) == 1:
                #handle small rounding errors using a tolerance
                return abs(cards[0] - 24) < .0005

            for op in ['-', '+', '*', '/']:
                for i in range(len(cards)-1):
                    if op == '-':
                        R = cards[i] - cards[i+1]
                    elif op == '+':
                        R = cards[i] + cards[i+1]
                    elif op == '*':
                        R = cards[i] * cards[i+1]
                    else:
                        if cards[i+1] == 0:
                            continue
                        R = cards[i] / cards[i+1]
                    
                    new = cards[:i] + [R]
                    if i+2 < len(cards):
                        new+=cards[i+2:]
                    if check(new):
                        return True
            return False


        for card_perms in permutations(cards):
            if check(list(card_perms)):
                return True
        return False
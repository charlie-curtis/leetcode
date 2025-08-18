class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        #sloppy code for brute forcing. For all operation combinations (e.g. '---', '--+'), etc, run that against all card permutations (3,2,1,0), (2,1,3,0), etc. And for each of those combinations, try executing the operations in different orderings of those operations.
        card_perms = list(permutations(cards))
        op_perms = list(permutations([0,1,2]))

        def do(x,y, op):
            if op == '*':
                return x*y
            if op == '/':
                if y == 0:
                    return False
                return x/y
            if op == '+':
                return x + y
            if op == '-':
                return x-y

        def check2(card_order, ops):
            for op_order in op_perms:

                tmp = list(card_order)

                used = set()
                for i in op_order:
                    used.add(i)
                    if i == 1 and 0 in used:
                        i-=1
                    if i == 2:
                        i = 3-len(used)
                    R = do(tmp[i], tmp[i+1], ops[len(used)-1])
                    if i+2 < len(tmp):
                        tmp = tmp[:i] + [R] + tmp[i+2:]
                    else:
                        tmp = tmp[:i] + [R]
                        
                if abs(tmp[0] - 24) < .0005:
                    return True
            return False

        def check(ops):

            for cardperm in card_perms:
                if check2(cardperm, ops):
                    return True

        def bt(cur):
            if len(cur)==3:
                return check(cur)

            if bt(cur+'-'):
                return True
            if bt(cur+'+'):
                return True
            if bt(cur+'*'):
                return True
            if bt(cur+'/'):
                return True
            return False
        
        return bt('')
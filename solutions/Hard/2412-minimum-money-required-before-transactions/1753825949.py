
#[2,1], [5,0], [4,2]
#cost = 2, delta = 1 [1]
#cost = 5, delta = 5 [0]
#cost = 4, delta = 2 [2]
class Solution:
    def minimumMoney(self, A: List[List[int]]) -> int:
        pos = []
        neg = []
        for cost,cashback in A:
            if cost > cashback:
                delta = cost-cashback
                cost = cost
                neg.append([cost, delta])
            else:
                pos.append(cost)
        #iterate over all the cost, deltas. simulate putting this item last (which means we can't choose the delta for the i-th item, but we can choose the cost for the i-th item)

        Tdelta = sum([x[1] for x in neg])
        can = max([Tdelta + cost-delta for cost,delta in neg] + [0])

        #we could also choose one positive number (the one with the highest cost)
        if pos:
            can = max(can, Tdelta + max(pos))
        return can
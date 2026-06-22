class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:

        d = list(zip(monsters,coins))
        monsters.sort()
        d.sort()

        f = lambda prev, cur: prev + cur[1] 
        pref = list(accumulate(d, f, initial=0))

        #this is the shorthand unreadable way to right this, lol
        return [pref[bisect_right(monsters,x)] for x in heroes]
        
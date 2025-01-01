class Solution:
    def houseOfCards(self, n: int) -> int:


        #how many distinct houses we can make given $cards to use with a base of $base
        @cache
        def dp(cards, base):

            if cards == 0:
                return 1
            if base == 0 or cards < 0:
                #no base to build on or nothing to build with
                return 0


            #we can either stack until we've ran out of base or until we've used all the cards

            #to satisfy the entire base, we'd need 2*b + b-1 cards
            used = 0
            res = 0
            for i in range(base):
                if used > cards:
                    break
                used+=2
                #simulate ending the row here
                res+=dp(cards-used, i)

                #simulate continuing to build on this row
                used+=1

            return res

        return dp(n, 10**6)


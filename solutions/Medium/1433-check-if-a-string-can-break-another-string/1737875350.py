class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:


        def check(s1, s2):
            A = [x for x in s1]
            B = [x for x in s2]
            A.sort()
            B.sort()
            adv = False
            for x,y in zip(A,B):
                if x > y:
                    return False
            return True


        a = check(s1, s2)
        b = check(s2, s1)

        return a or b
        
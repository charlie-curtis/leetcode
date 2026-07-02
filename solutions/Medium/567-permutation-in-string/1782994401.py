class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needed=Counter(s1)
        have=Counter()
        
        l=0
        for i,x in enumerate(s2):
            have[x]+=1
            if sum(have.values()) > sum(needed.values()):
                have[s2[l]]-=1
                l+=1
            if have==needed:
                return True
        return False